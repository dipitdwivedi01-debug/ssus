from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://dipitdwivedi01_db_user:Dipit%40gsp@dipit.ia1lrwb.mongodb.net/?appName=Dipit"

    client = MongoClient(MONGO_URI)

    client.andmin.command("ping")
    
    db = client["ssus"]
    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_report"]

    print("MongoDB connected Successfully!")
except Exception as e:
    print("MongoDB error:",e)



