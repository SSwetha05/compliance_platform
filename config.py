import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    Db_Host = st.secrets["Db_Host"]
    Db_Name = st.secrets["Db_Name"]
    Db_User = st.secrets["Db_User"]
    Db_Password = st.secrets["Db_Password"]
    Db_Port = st.secrets["Db_Port"]
except Exception:
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