import os
from dotenv import load_dotenv

load_dotenv()

Db_Host = os.getenv("Db_Host")
Db_Name = os.getenv("Db_Name")
Db_User = os.getenv("Db_User")
Db_Password = os.getenv("Db_Password")
Db_Port = os.getenv("Db_Port")

Upload_Folder = "uploads"

os.makedirs(
    Upload_Folder,
    exist_ok=True
)