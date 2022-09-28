from fastapi import FastAPI
app = FastAPI() 
@app.get("/") 
async def hello() -> dict: 
    return { "NIM": "18220105", "Nama" : "Made Adi Surya Pramana"} 