from collections import defaultdict
from minio import Minio


class PythonMinIOUtils:
    def __init__(self, endpoint: str, access_key: str, secret_key: str, secure: bool, bucket_name: str):
        # Initialize MinIO client
        self.minio_client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure  # Set to False for insecure connections (http instead of https)
        )

        # Define the bucket name
        self.bucket_name = bucket_name

    def download_file(self, folder_name, file_name, download_path):
        try:
            # Download file from the bucket
            self.minio_client.fget_object(
                self.bucket_name,
                f"{folder_name}/{file_name}",
                download_path
            )
            print('File downloaded successfully.')
        except Exception as err:
            print(f'Error downloading file: {err}')

    def upload_file(self, folder_name, file_path, file_name):
        try:
            # Upload file to the bucket
            self.minio_client.fput_object(
                self.bucket_name,
                f"{folder_name}/{file_name}",
                file_path
            )
            print('File uploaded successfully.')
        except Exception as err:
            print(f'Error uploading file: {err}')

    def list_files_in_folder(self, folder_name):
        try:
            # List all files in the specified folder
            objects = self.minio_client.list_objects(self.bucket_name, prefix=folder_name, recursive=True)
            for obj in objects:
                print(obj.object_name)
        except Exception as err:
            print(f'Error listing files: {err}')

    def list_files_grouped_by_folder(self):
        try:
            # Dictionary to hold files grouped by folder
            files_by_folder = defaultdict(list)

            # List all objects in the bucket
            objects = self.minio_client.list_objects(self.bucket_name, recursive=True)
            for obj in objects:
                folder = '/'.join(obj.object_name.split('/')[:-1])
                files_by_folder[folder].append(obj.object_name)

            # Print files grouped by folder
            for folder, files in files_by_folder.items():
                print(f'Folder: {folder}')
                for file in files:
                    print(f'  {file}')
        except Exception as err:
            print(f'Error listing files: {err}')

# Example usage:
# minio_utils = PythonMinIOUtils('play.min.io', 'access_key', 'secret_key', True, 'my-bucket')
# minio_utils.upload_file('/path/to/local/file.txt', 'folder/file.txt')
# minio_utils.list_files_in_folder('folder/')
