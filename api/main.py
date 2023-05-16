from fastapi import FastAPI

app = FastAPI() # 创建API实例

@app.get("/")
async def root():
    return {"message": "Hello World"}