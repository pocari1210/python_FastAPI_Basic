# ルーティング設定用のクラス
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import schemas.contact as contact_schema # スキーマをimport
import cruds.contact as contact_crud
from database import get_db

from datetime import datetime

# インスタンス化
router = APIRouter()

# 一覧表示
# 第二引数にレスポンスのモデルを指定
@router.get("/contacts", response_model=list[contact_schema.ContactList]) 

# AsyncSessionでデータベースに接続
async def get_contact_all(db: AsyncSession = Depends(get_db)):
    return await contact_crud.get_contact_all(db)
    
# 保存
@router.post("/contacts",response_model=contact_schema.ContactCreate)
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await contact_crud.create_contact(db, body)

# 詳細表示
@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail) 
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db, id)

    # 登録していないidを選択した時の処理
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

# 更新
@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(id: int, body: contact_schema.ContactCreate):
    return contact_schema.Contact(id, **body.model_dump())

# 削除
# idを指定すればモデルは不要の為、response_modelをNoneとする
@router.delete("/contacts/{id}", response_model=None)
async def delete_contact(id: int):
    return