// ===== 全局状态 =====
let currentSessionId = null;
let token = localStorage.getItem("token") || "";

// ===== 通用请求封装（自动带 token）=====
async function request(url, options = {}) {
    const headers = { "Content-Type": "application/json" };
    if (token) headers["Authorization"] = "Bearer " + token;
    const res = await fetch(url, { ...options, headers });
    const body = await res.json();
    if (body.code !== 200) throw new Error(body.message);
    return body.data;
}

// ===== 登录 / 注册 / 登出 =====
async function login() {
    const username = document.getElementById("loginUser").value.trim();
    const password = document.getElementById("loginPass").value;
    if (!username || !password) { alert("请输入用户名和密码"); return; }
    try {
        token = await request("/api/login", {
            method: "POST",
            body: JSON.stringify({ username, password })
        });
        localStorage.setItem("token", token);
        showLoggedIn();
        addMessage("ai", "登录成功！");
        await loadSessions();
    } catch (e) {
        addMessage("ai", "登录失败：" + e.message);
    }
}

async function register() {
    const username = document.getElementById("loginUser").value.trim();
    const password = document.getElementById("loginPass").value;
    if (!username || !password) { alert("请输入用户名和密码"); return; }
    try {
        await request("/api/register", {
            method: "POST",
            body: JSON.stringify({ username, password })
        });
        addMessage("ai", "注册成功，现在可以登录了");
    } catch (e) {
        addMessage("ai", "注册失败：" + e.message);
    }
}

function logout() {
    token = "";
    localStorage.removeItem("token");
    document.querySelector(".loginBtns").style.display = "flex";
    document.getElementById("logoutBtn").style.display = "none";
    addMessage("ai", "已退出登录");
}

function showLoggedIn() {
    document.querySelector(".loginBtns").style.display = "none";
    document.getElementById("logoutBtn").style.display = "block";
}

// ===== 消息渲染 =====
function addMessage(role, text) {
    const box = document.getElementById("messages");
    const div = document.createElement("div");
    div.className = "msg " + role;
    div.textContent = text;   // textContent 防止内容被当 HTML 执行
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;   // 滚动到底部
}

// ===== 会话列表 =====
async function loadSessions() {
    const list = await request("/api/sessions");
    const ul = document.getElementById("sessionList");
    ul.innerHTML = "";
    list.forEach(id => {
        const li = document.createElement("li");
        li.textContent = id;
        li.onclick = () => loadSession(id);

        const del = document.createElement("span");
        del.className = "del";
        del.textContent = "✕";
        del.onclick = (e) => { e.stopPropagation(); delSession(id); };

        li.appendChild(del);
        ul.appendChild(li);
    });
}

async function loadSession(id) {
    const data = await request(`/api/sessions/${id}`);
    currentSessionId = id;

    // 高亮当前会话
    [...document.querySelectorAll("#sessionList li")].forEach(li =>
        li.classList.toggle("active", li.textContent.includes(id))
    );

    // 重绘历史消息
    document.getElementById("messages").innerHTML = "";
    data.messages.forEach(m => addMessage(m.role === "user" ? "user" : "ai", m.content));
}

async function newSession() {
    currentSessionId = await request("/api/sessions", { method: "POST" });
    document.getElementById("messages").innerHTML = "";
    await loadSessions();
}

async function delSession(id) {
    await request(`/api/sessions/${id}`, { method: "DELETE" });
    if (id === currentSessionId) currentSessionId = null;
    await loadSessions();
}

// ===== 发消息 =====
async function send() {
    const input = document.getElementById("userInput");
    const text = input.value.trim();
    if (!text) return;
    input.value = "";
    addMessage("user", text);

    // 没有会话就先建一个
    if (!currentSessionId) await newSession();

    const btn = document.getElementById("sendBtn");
    btn.disabled = true;
    try {
        const reply = await request("/api/chat", {
            method: "POST",
            body: JSON.stringify({ session_id: currentSessionId, message: text })
        });
        addMessage("ai", reply);
    } catch (e) {
        addMessage("ai", "出错了：" + e.message);
    }
    btn.disabled = false;
}

// ===== 事件绑定 =====
document.getElementById("sendBtn").onclick = send;
document.getElementById("userInput").onkeydown = (e) => { if (e.key === "Enter") send(); };
document.getElementById("newBtn").onclick = newSession;
document.getElementById("loginBtn").onclick = login;
document.getElementById("registerBtn").onclick = register;
document.getElementById("logoutBtn").onclick = logout;

// ===== 页面加载：拉列表（已登录则保持登录态）=====
(async function init() {
    if (token) showLoggedIn();
    try {
        await loadSessions();
    } catch (e) {
        addMessage("ai", "无法连接后端：" + e.message + "（先启动 FastAPI 服务）");
    }
})();
