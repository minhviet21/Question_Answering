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

def BM25_search(query):
    result = client.query.get("test1", ["law_id","article_id","title", "index", "content"]
                        ).with_bm25(
                          query=question,
                          properties=["content"]
                        ).with_limit(1).with_additional(['certainty']).do()
    return result['data']['Get']['Test1'][0]['content']

def hybrid_search(query, vector):
    result = client.query.get("test1", ["law_id","article_id","title", "index", "content"]
                          ).with_hybrid(
                              query=query,
                              properties=["content"], 
                              vector = vector 
                              ).with_limit(1).with_additional(['certainty']).do()
    return result['data']['Get']['Test1'][0]['content']

def vector_to_BM25_search(vector, question, k):
    nearVector = {"vector": vector}
    top_results = client.query.get("test1", ["law_id", "article_id", "title", "index", "content", "_additional { id }"]
                        ).with_near_vector(nearVector).with_limit(k).with_additional(['certainty']).do()
    top_results = top_results['data']['Get']['Test1']
    
    id_list = [obj["_additional"]["id"] for obj in top_results]
    
    where_filter = {"path": "id", "operator": "ContainsAny", "valueStringArray": id_list}
    
    result = client.query.get("test1", ["law_id", "article_id", "title", "index", "content", "_additional { id }"]
                        ).with_where(where_filter
                        ).with_bm25(
                          query=question,
                          properties=["content"]
                        ).with_limit(1).with_additional(['certainty']).do()
    
    return result['data']['Get']['Test1'][0]['content']

def BM25_to_vector_search(vector, question, k):
    top_results = client.query.get("test1", ["law_id", "article_id", "title", "index", "content", "_additional { id }"]
                        ).with_bm25(
                          query=question,
                          properties=["content"]
                        ).with_limit(k).with_additional(['certainty']).do()
    top_results = top_results['data']['Get']['Test1']
    
    id_list = [obj["_additional"]["id"] for obj in top_results]
    
    where_filter = {"path": "id", "operator": "ContainsAny", "valueStringArray": id_list}
    
    nearVector = {"vector": vector}
    result = client.query.get("test1", ["law_id", "article_id", "title", "index", "content", "_additional { id }"]
                        ).with_where(where_filter
                        ).with_near_vector(nearVector).with_limit(1).with_additional(['certainty']).do()
    return result['data']['Get']['Test1'][0]['content']
