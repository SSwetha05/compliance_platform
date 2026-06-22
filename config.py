import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    Db_Host = st.secrets["DB_HOST"]
    Db_Name = st.secrets["DB_NAME"]
    Db_User = st.secrets["DB_USER"]
    Db_Password = st.secrets["DB_PASSWORD"]
    Db_Port = st.secrets["DB_PORT"]
except Exception:
    Db_Host = os.getenv("DB_HOST")
    Db_Name = os.getenv("DB_NAME")
    Db_User = os.getenv("DB_USER")
    Db_Password = os.getenv("DB_PASSWORD")
    Db_Port = os.getenv("DB_PORT")

Upload_Folder = "uploads"

os.makedirs(
    Upload_Folder,
    exist_ok=True
)