from fastapi import FastAPI

# パッケージ読込(routersフォルダ下のcontact.pyをimport)
from routers import contact 

# FastAPIのクラスを変数appにインスタンス化
app = FastAPI()

# URLを指定
# @app.get("/")
# 「/」のURLにアクセスしたら、メソッドが実行される
# async def root():
#     return {"message": "Hello World"}

# パッケージ内のルーター(インスタンス)を読み込み
app.include_router(contact.router)