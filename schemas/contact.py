from pydantic import BaseModel, Field, EmailStr, HttpUrl #インポート
from datetime import datetime

# pydanticのBaseModelを継承(引数として使う)
# class Contact(BaseModel): 
#     id: int
#     name: str = Field(..., min_length=2, max_length=50) # 必須, 2文字～50文字
#     email: EmailStr # メール
#     url: HttpUrl | None = Field(default=None) # urlか空
#     gender: int = Field(..., strict=True, ge=0, le=2) # 必須, 0, 1, 2
#     message: str = Field(..., max_length=200) # 必須、最大200文字
#     is_enabled: bool = Field(default=False) # デフォルト値指定
#     created_at: datetime

# 一覧表示用のクラス
class ContactList(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    created_at: datetime
    class Config:
        from_attributes = True

# 保存用のクラス
class ContactBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    class Config: # ORMと紐づけを行う
        from_attributes = True

# 詳細表示用のクラス
class ContactDetail(ContactBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# 新規作成用のクラス
class ContactCreate(ContactBase):
    pass

