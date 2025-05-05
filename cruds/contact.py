from typing import List, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import models.contact as contact_model
from datetime import datetime

async def create_contact(db: AsyncSession, contact: contact_schema.ContactCreate ) -> contact_model.Contact:
    
    """
    DBに保存
    引数:
        db: DBセッション
        AsyncSession: 非同期接続を行う
        contact: 作成するコンタクトのデータ
    戻り値:
        contact_model.Contact: 作成されたORMモデルの情報を返している
    """

    # model_dumpメソッドで、モデルを辞書形式 (dict) に変換
    contact_data = contact.model_dump()

    # URLが入っていたら文字形式に変換するという処理
    if contact_data["url"] is not None:
        contact_data["url"] = str(contact_data["url"])
    
    # DBに登録するためのORMモデルを取得 ※db保存はsqlalchemyのモデル
    db_contact = contact_model.Contact(**contact_data)

    # 追加の処理を行う
    db.add(db_contact) 

    # コミット (反映) 
    # ※非同期関数で処理をおこなっているため、awaitを記述するのがベター
    await db.commit() 

    # DBに登録された最新の情報を反映させる
    await db.refresh(db_contact)

    # 関数の戻り値を指定
    return db_contact

"""
一覧表示
id,name,createdのカラムを指定し、
uvicornに疎通させる

"""

async def get_contact_all(db: AsyncSession) -> List[Tuple[int, str, datetime]]:

    # DBのexecuteの結果が変数resultにはいる
    result : Result = await db.execute(

        # selectメソッドで取得するカラムを指定
        select(
            contact_model.Contact.id,
            contact_model.Contact.name,
            contact_model.Contact.created_at
        )
    )
    return result.all()

"""
詳細一覧表示
idを指定し、1件だけ表示させる

"""

async def get_contact(db: AsyncSession, id: int) -> contact_model.Contact | None:
    query = select(contact_model.Contact).where(contact_model.Contact.id == id)
    result : Result = await db.execute(query)

    # 1件目のデータを取得する
    return result.scalars().first()

"""
更新処理
idを指定し登録している情報を変更する

"""

async def update_contact(
        db: AsyncSession, 
        contact: contact_schema.ContactCreate, # 更新したい情報
        original: contact_model.Contact # 登録済みの情報
        ) -> contact_model.Contact:
    original.name = contact.name
    original.email = contact.email
    if original.url is not None:
        original.url = str(contact.url)
    original.gender = contact.gender
    original.message = contact.message
    db.add(original) # 追加
    await db.commit() # コミット (反映)
    await db.refresh(original) # # DBに登録された最新の情報を反映させる
    return original

