from langchain_openai import ChatOpenAI
import streamlit as st

# API 키 직접 입력
api_key = 'sk-proj-GJaRpf5fQvPNY8ixzyquT3BlbkFJlpljATz65AFj7jrnoZWF'

# ChatOpenAI 초기화 시 API 키와 모델 지정
chat_model = ChatOpenAI(api_key=api_key, model="gpt-4o")

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
