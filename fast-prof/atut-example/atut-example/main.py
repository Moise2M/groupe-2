import os
from fastapi import FastAPI, Header, File, Request, UploadFile, HTTPException
from minio import Minio
from dotenv import load_dotenv


load_dotenv(".env")


def get_model(a, b):
    def f(x):
        return a * x + b
    return f


def lifespan(app: FastAPI):
    print("Starting")
    app.s3 = Minio(
        endpoint=os.getenv("S3_ENDPOINT_URL"),
        access_key=os.getenv("S3_ACCESS_KEY"),
        secret_key=os.getenv("S3_SECRET_KEY"),
        region=os.getenv("S3_REGION"),
    )
    model_path = os.getenv("MODEL_FILE_PATH")
    file_path = "tmp/" + model_path

    objs = app.s3.list_objects(os.getenv("S3_BUCKET_NAME"))
    print("++++")
    for obj in objs:
        print("===========")
        print(obj.object_name)
    print("----")

    app.s3.fget_object(
        bucket_name=os.getenv("S3_BUCKET_NAME"),
        object_name=model_path,
        file_path=file_path
    )

    # Load the model
    app.model = None
    with open(file_path, "rb") as f:
        app.model = f.read()
    # split model by comma and convert to float
    app.weights = [float(i) for i in app.model.decode().split(",")]
    app.model = get_model(*app.weights)

    print("Model loaded")
    print(app.model)

    yield
    print("Stopping")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def health():
    return {"status": "ok"}


@app.get("/predict")
async def predict(request: Request, x: float):
    if app.model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    return {"y": app.model(x)}
