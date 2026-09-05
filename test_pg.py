from sqlalchemy import create_engine, text

# 把「你的密码」替换成安装 PG 时设的密码
引擎 = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/hanzi_box")

with 引擎.connect() as 连接:
    # 写一行
    连接.execute(text("INSERT INTO sessions (session_id, messages) VALUES (:sid, :msg)"),
                 {"sid": "test_001", "msg": '{"messages": []}'})
    连接.commit()

    # 读出来
    行 = 连接.execute(text("SELECT session_id, messages FROM sessions WHERE session_id = :sid"),
                      {"sid": "test_001"}).fetchone()
    print("连上了！读到的数据：", 行)

    # 删掉测试行
    连接.execute(text("DELETE FROM sessions WHERE session_id = :sid"), {"sid": "test_001"})
    连接.commit()
    print("测试行已清理")
