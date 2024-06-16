from sentence_transformers import SentenceTransformer
import pandas as pd
import json
import weaviate

model = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder')

input_file = "sample_data/fine_legal_corpus.csv"
output_json_file = "sample_data/fine_legal_corpus_vector.json"

def text2vec(text):
  return str(model.encode(text).tolist())

json_data = []
for chunk in pd.read_csv(input_file, chunksize=10):
    print("Processing a new batch...")
    chunk['Vector'] = chunk['content'].apply(text2vec)
    json_data.extend(chunk.to_dict(orient='records'))
    print(f"Processed batch with {len(chunk)} records")
    
with open(output_json_file, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
