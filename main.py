from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/")
async def read_root():
    return FileResponse("index.html")
