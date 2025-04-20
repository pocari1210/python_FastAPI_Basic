# ルーティング設定用のクラス
from fastapi import APIRouter

# インスタンス化
router = APIRouter()

# 一覧表示
@router.get("/contacts") 
async def get_contact_all():
    pass

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