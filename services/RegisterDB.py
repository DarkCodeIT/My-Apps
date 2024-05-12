from pymongo import MongoClient
import os


def register_user_db() -> None:
	cluster = MongoClient(
		f"mongodb+srv://{os.getenv("USER")}:{os.getenv("PASSWORD")}@cluster0.48ahq5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
	)
	print(cluster)

	collection = cluster.App.user
	print(collection.find_one({'username' : "admin"}))

register_user_db()