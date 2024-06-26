import streamlit as st
from answer_question.text2vec import embed_question
from answer_question.translate import translate_en2vi, translate_vi2en
from answer_question.search import vector_to_BM25_search
from answer_question.Llama2_generate import generate
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>Hỏi đáp hình phạt trong pháp luật Việt Nam</h1>", unsafe_allow_html=True)

if 'submitted_question' not in st.session_state:
    st.session_state.submitted_question = ''

question = st.text_area("Nhập câu hỏi", st.session_state.submitted_question, height = 50)
confirm_button = st.button("Xác nhận")

if confirm_button and question:
    st.session_state.submitted_question = question

if st.session_state.submitted_question:
    vi_question = st.session_state.submitted_question
    vector = embed_question(vi_question)
    vi_context = vector_to_BM25_search(vi_question, vector, 30)
    en_question = translate_vi2en(vi_question)
    en_context = translate_vi2en(vi_context)
    en_response = generate(en_question, en_context)
    vi_response = translate_en2vi(en_response)
    st.text_area("Câu trả lời cho câu hỏi của bạn:",vi_response,height = 100)
