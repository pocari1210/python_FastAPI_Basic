from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLiteの非同期対応
DB_URL = "sqlite+aiosqlite:///fastapi-app.db"

engine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()

"""
★sessionmakerの引数について★
sessionmaker・・DBセッションを作成
autocommit=False・・コミットするまでDBに反映されない
autoflush=False・・セッションの変更が即時実行されない
bind=engine・・DBセッションが扱うDBエンジン指定
class_=AsyncSession・・扱うセッションクラスの指定
"""

db_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

"""
★get_db関数★
データベースと接続する関数を作成

with・・DB接続などで使われる セッションの開始と終了を自動的に管理
yield session・・呼び出し元にセッションを提供 (ジェネレータ)

"""
async def get_db():
    async with db_session() as session:
        yield session