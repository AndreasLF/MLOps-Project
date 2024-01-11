from fastapi import FastAPI, Request
from MLOps_Project.predict_model import predict

app = FastAPI()

# ===================== Routes =====================
@app.get("/")
def read_root(request: Request):
    return {"Hello": "World"}   

@app.get("/test_dst")
def dst_test():
    return {
        "Message": "This is a test message - please ignore me."
    }