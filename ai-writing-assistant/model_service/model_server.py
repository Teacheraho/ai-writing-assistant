from fastapi import FastAPI
app = FastAPI(title="AIGC模型推理服务")
@app.post("/ai/generate")
def generate_text(prompt:str):
    # 模拟Qwen-7B文本生成逻辑，课程原型简化代码
    return {"result":"AI生成文本内容"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("model_server:app", port=8001)