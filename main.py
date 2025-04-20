from fastapi import FastAPI

# FastAPIのクラスを変数appにインスタンス化
app = FastAPI()

# URLを指定
@app.get("/")

# 「/」のURLにアクセスしたら、メソッドが実行される
async def root():
    return {"message": "Hello World"}