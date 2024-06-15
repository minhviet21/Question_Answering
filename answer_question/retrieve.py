import weaviate

client = weaviate.Client(
    url = "https://project2-f1prkf5g.weaviate.network",  # Replace with your Weaviate endpoint
    auth_client_secret=weaviate.auth.AuthApiKey(api_key="OdVkRlISRMtBNYgd1FZFWCMCm3SuuBstNtbZ"),  # Replace with your Weaviate instance API key
)

def vector_search(vector):
    nearVector = {"vector": vector}
    result = client.query.get("test1", ["law_id","article_id","title", "index", "content"]
                        ).with_near_vector(nearVector).with_limit(1).with_additional(['certainty']).do()
    return result['data']['Get']['Test1'][0]['content']