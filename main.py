from fastapi import FastAPI


app = FastAPI()

@app.get("/quote")
def root():
    return { "message": "FastAPI!" }

