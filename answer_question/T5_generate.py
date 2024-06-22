import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

path = "google/flan-t5-xl"
tokenizer = T5Tokenizer.from_pretrained(path)
model = T5ForConditionalGeneration.from_pretrained(path, device_map="auto")

def generate(question, context):
    prompt = f"""
CONTEXT: {context}

QUESTION: {question}
"""
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)
    outputs = model.generate(input_ids, max_new_tokens=200)
    response = tokenizer.decode(outputs[0],skip_special_tokens=True)
    return response
