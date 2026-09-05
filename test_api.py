# test_api.py - pytest 测试 first_api.py 的 GET 接口（不动数据）
from fastapi.testclient import TestClient
from first_api import app

client = TestClient(app)

def test_root():
    """测试根路径：GET / 返回 200"""
    r = client.get("/")
    assert r.status_code == 200
    assert "msg" in r.json() # 至少有 msg 字段就行

def test_list_riddles():
    """测试获取谜题列表：GET /api/riddles 返回 list"""
    r = client.get("/api/riddles")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_get_one_riddle():
    """测试单条接口：GET /api/riddles/1 返回 200 或 404（取决于数据）"""
    r = client.get("/api/riddles/1")
    assert r.status_code in (200, 404) # 两种都算接口工作正常def test_get_missing_404():
    """测试不存在的 id：应该返回 404"""
    r = client.get("/api/riddles/999999")
    assert r.status_code == 404


def test_get_missing_404():
    r = client.get('/api/riddles/999999')
    assert r.status_code == 404
