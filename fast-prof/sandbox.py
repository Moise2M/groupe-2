import os
from fastapi import FastAPI, Header, File, Request, UploadFile, HTTPException
from minio import Minio
from dotenv import load_dotenv


load_dotenv(".env")

s3 = Minio(
    endpoint=os.getenv("S3_ENDPOINT_URL"),
    access_key=os.getenv("S3_ACCESS_KEY"),
    secret_key=os.getenv("S3_SECRET_KEY"),
    region=os.getenv("S3_REGION"),
)
s3.fput_object(
    bucket_name=os.getenv("S3_BUCKET_NAME"),
    object_name="model222.txt",
    file_path=os.getenv("MODEL_FILE_PATH"),
)
