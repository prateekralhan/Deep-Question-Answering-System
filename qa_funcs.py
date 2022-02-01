import streamlit as st
import re
import fitz
import docx
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def generate_answer(plain_text,ques_text):
    nlp = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')
    question_set = {
                    'question':ques_text,
                    'context':plain_text
                   }
    results = nlp(question_set)
    return results['answer']

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def extract_text_txt(uploaded_txt_file,downloaded_txt_file):
    with open(uploaded_txt_file) as intxt:
        data = intxt.read()

    data = re.findall('[aA-zZ]+', data)
    with open(downloaded_txt_file, 'w') as outtxt:
        outtxt.write('\n'.join(data))
    return ' '.join(data)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def extract_text_pdf(uploaded_pdf_file):
    with fitz.open(uploaded_pdf_file) as intxt:
        text = ""
        for page in intxt:
            text += page.getText()
    return text

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def extract_text_docx(uploaded_docx_file):
    doc = docx.Document(uploaded_docx_file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ' '.join(fullText)
