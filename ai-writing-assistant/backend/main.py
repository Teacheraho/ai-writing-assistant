from fastapi import FastAPI
import uvicorn
app = FastAPI(title="AI写作辅助后端接口")
# 用户、文档、AI生成接口路由挂载
@app.get("/")
def index():
    return {"msg":"后端服务正常运行"}
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)