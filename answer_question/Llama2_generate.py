import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

token = "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"
path = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(path, cache_dir="/data/yash/base_models", token = token)
model = AutoModelForCausalLM.from_pretrained(path, device_map='auto', token = token)

def get_difference(input ,response):
    return response[len(input)-1:]

def generate(text, max_new_tokens=100, temperature=0.7, top_k=50, top_p=0.9):
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt").to(device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            eos_token_id=tokenizer.eos_token_id,
            early_stopping=True
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return get_difference(text, response)
