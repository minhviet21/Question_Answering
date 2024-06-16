from pyvi import ViTokenizer

def tokenize(text):
    return ViTokenizer.tokenize(text)

def remove_stopwords(text):
    filepath = 'Question_Answering\\tokenized_stopwords.txt'
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = set(line.strip() for line in file)
    return ' '.join([word for word in text.split() if word.lower() not in stopwords])

def untokenize(text):
    return text.replace('_', ' ')