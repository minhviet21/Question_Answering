import weaviate
import json
import ast
import requests

client = weaviate.Client(
    url = "",  # Replace with your Weaviate endpoint
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=""),  # Replace with your Weaviate instance API key
)
class_obj = {"class": "test2", "vectorizer": None,}
client.schema.create_class(class_obj)

with open('Question_Ansering\sample_data\legal_corpus.json', 'r', encoding = "utf-8") as file:
    data = json.load(file)

client.batch.configure(batch_size=100)
with client.batch as batch:
    for i, d in enumerate(data):
        print(f"importing articles: {i+1}")
        properties = {
            "law_id": d["law_id"],
            "article_id": d["article_id"],
            "title": d["title"],
            "index": d["index"],
            "content": d["content"]
        }
        batch.add_data_object(properties, "test2", vector = ast.literal_eval(d["Vector"]))