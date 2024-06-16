from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

en2vi_model_name = "vinai/vinai-translate-en2vi-v2"
tokenizer_en2vi = AutoTokenizer.from_pretrained(en2vi_model_name, src_lang="en_XX")
model_en2vi = AutoModelForSeq2SeqLM.from_pretrained(en2vi_model_name)

vi2en_model_name = "vinai/vinai-translate-vi2en-v2"
tokenizer_vi2en = AutoTokenizer.from_pretrained(vi2en_model_name, src_lang="vi_VN")
model_vi2en = AutoModelForSeq2SeqLM.from_pretrained(vi2en_model_name)

def translate_vi2en(text):
    input_ids = tokenizer_vi2en(text, padding=True, return_tensors="pt")
    output_ids = model_vi2en.generate(
        **input_ids,
        decoder_start_token_id=tokenizer_vi2en.lang_code_to_id["en_XX"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer_vi2en.batch_decode(output_ids, skip_special_tokens=True)[0]

def translate_en2vi(text):
    input_ids = tokenizer_en2vi(text, padding=True, return_tensors="pt")
    output_ids = model_en2vi.generate(
        **input_ids,
        decoder_start_token_id=tokenizer_en2vi.lang_code_to_id["vi_VN"],
        num_return_sequences=1,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer_en2vi.batch_decode(output_ids, skip_special_tokens=True)[0]
