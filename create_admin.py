import os
from database import SessionLocal
from models.admin_model import Admin
from utils.auth_utils import get_password_hash
from database import engine
from models import admin_model

def create_initial_admin():
    # Ensure tables are created
    admin_model.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    admin_exists = db.query(Admin).filter(Admin.username == "admin").first()
    if admin_exists:
        print("Admin user already exists.")
        return
    
    hashed_password = get_password_hash("admin123")
    new_admin = Admin(username="admin", password_hash=hashed_password)
    db.add(new_admin)
    db.commit()
    print("Default admin created successfully! Username: admin, Password: admin123")
    db.close()

if __name__ == "__main__":
    create_initial_admin()
