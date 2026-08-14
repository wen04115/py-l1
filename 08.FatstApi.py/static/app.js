// ===== 全局状态 =====
let currentSessionId = null;

// ===== 通用请求封装（后端统一返回 {code, message, data}）=====
async function request(url, options = {}) {
    const res = await fetch(url, {
        headers: { "Content-Type": "application/json" },
        ...options
    });
    const body = await res.json();
    if (body.code !== 200) throw new Error(body.message);
    return body.data;
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
    currentSessionId = data.current_session;

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

// ===== 页面加载：拉列表 + 新建会话 =====
(async function init() {
    try {
        await loadSessions();
        await newSession();
    } catch (e) {
        addMessage("ai", "无法连接后端：" + e.message + "（先启动 FastAPI 服务）");
    }
})();
