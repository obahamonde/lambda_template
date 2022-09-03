from uuid import uuid4
from datetime import datetime

def get_id()->str:
    return str(uuid4())

def get_date()->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_avatar()->str:
    return f"htttps://www.dicebear.com/api/avataaars/{uuid4()}.svg"