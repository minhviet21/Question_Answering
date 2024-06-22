import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

token = "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"
path = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(path, cache_dir="/data/yash/base_models", token = token)
model = AutoModelForCausalLM.from_pretrained(path, device_map='auto', token = token)

def get_answer(response):
    if "ANSWER:" in response:
        start_index = response.index("ANSWER:")
        return response[start_index+8:]
    else:
        return response

def generate(question, context):
    prompt = f"""
CONTEXT: {en_context}

QUESTION: {en_question}
"""
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_new_tokens=200)
    response = tokenizer.decode(outputs[0],skip_special_tokens=True)
    return get_answer(response)
