from pymongo import MongoClient
from dotenv import load_dotenv
import os


def register_user_db(username: str, email: str, password: str):
	load_dotenv()

	cluster = MongoClient(
		f"mongodb+srv://{os.getenv("USER")}:{os.getenv("PASSWORD")}@cluster0.48ahq5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
	)

	collection = cluster.App.user
	name_exists = collection.count_documents({"username" : username})
	email_exists = collection.count_documents({"email" : email})

	if name_exists != 0 or email_exists != 0:
	
		return "Error: Account already exists"
	
	else:
		collection.insert_one({
			"username" : username,
			"email" : email,
			"password" : password
		})
		
		return "Done"
