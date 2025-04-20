from pydantic import BaseModel, Field #インポート
from datetime import datetime

# pydanticのBaseModelを継承(引数として使う)
class Contact(BaseModel): 
    id: int
    name: str
    email: str
    url: str
    gender: int
    message: str
    is_enabled: bool
    created_at: datetime