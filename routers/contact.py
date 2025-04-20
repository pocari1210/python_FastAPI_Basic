# ルーティング設定用のクラス
from fastapi import APIRouter

# スキーマをimport
import schemas.contact as contact_schema

from datetime import datetime

# インスタンス化
router = APIRouter()

# 一覧表示
# 第二引数にレスポンスのモデルを指定
@router.get("/contacts", response_model=list[contact_schema.Contact])
async def get_contact_all():
    
    # 試しにデータを登録
    dummy_date = datetime.now()

    return [contact_schema.Contact(
        id=1,
        name="山田",
        email="test@test.com",
        url="http://test.com",
        gender=1,
        message="テスト",
        is_enabled=False,
        created_at=dummy_date
        )]

# 保存
@router.post("/contacts")
async def create_contact():
    pass

# 詳細表示
@router.get("/contacts/{id}")
async def get_contact():
    pass

# 更新
@router.put("/contacts/{id}")
async def update_contact():
    pass

# 削除
@router.delete("/contacts/{id}")
async def delete_contact():
    pass