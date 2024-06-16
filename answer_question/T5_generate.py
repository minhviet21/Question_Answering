import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

path = "google/flan-t5-large"
tokenizer = T5Tokenizer.from_pretrained(T5_path)
model = T5ForConditionalGeneration.from_pretrained(T5_path, device_map="auto")

def generate(text):
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_new_tokens=100, temperature = 0.001, early_stopping = True)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response