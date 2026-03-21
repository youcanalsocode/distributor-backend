import os
import shutil
import uuid
from typing import Optional
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

def save_upload_file(upload_file: UploadFile) -> str:
    """Saves an uploaded file to the upload directory with a unique name and returns the relative path."""
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    # Generate a unique filename to avoid collisions
    file_extension = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb+") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
        
    return f"/{UPLOAD_DIR}/{unique_filename}"

def delete_upload_file(file_url: Optional[str]):
    """Deletes a file from the upload directory given its relative path (starting with /uploads/)."""
    if not file_url:
        return
        
    # Remove leading slash if present
    if file_url.startswith("/"):
        file_path = file_url[1:]
    else:
        file_path = file_url
        
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
