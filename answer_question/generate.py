import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

T5_path = "google/flan-t5-large"
T5_tokenizer = T5Tokenizer.from_pretrained(T5_path)
T5_model = T5ForConditionalGeneration.from_pretrained(T5_path, device_map="auto")

token = "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"
llama_path = "meta-llama/Llama-2-7b-chat-hf"
Llama_tokenizer = AutoTokenizer.from_pretrained(llama_path, cache_dir="/data/yash/base_models", token = token)
Llama_model = AutoModelForCausalLM.from_pretrained(llama_path, device_map='auto', token = token)

def T5_generate(text):
    with torch.no_grad():
        inputs = T5_tokenizer(text, return_tensors="pt").to(device)
        outputs = T5_model.generate(**inputs, max_new_tokens=100, temperature = 0.001, early_stopping = True)
        response = T5_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def get_difference(input ,response):
    return response[len(input)-1:]

def Llama_generate(text):
    with torch.no_grad():
        inputs = Llama_tokenizer(text, return_tensors="pt").to(device)
        outputs = Llama_model.generate(**inputs, max_new_tokens=100, temperature = 0.001, early_stopping = True)
        response = Llama_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return get_difference(text, response)