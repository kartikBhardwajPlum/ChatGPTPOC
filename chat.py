import streamlit as st
import requests

st.set_page_config(page_title="Streamlit API Example", page_icon=":guardsman:", layout="wide")

def api_call(query):
    response = requests.post(url="https://employee-experience-service-uydiiifsnq-el.a.run.app/api/v1/chat/question?question="+query, headers={"x-plum-internal-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IlZnUEg4SFNNYzBrVlZDYWZRRzRyIiwic291cmNlIjoiTUVNQkVSUyIsImVtYWlsSWQiOiJrZWVydGhpLnNpZGRlc2h3YXIrc3R1QHBsdW1ocS5jb20iLCJpYXQiOjE2NzU4NTk0NjEsImV4cCI6MTcyMjc4NTk0NjF9.hQtQeIlIpSyy1C2WkbaGZvcQEFWOq_JDzWb_Rwh0Mig"})
    return response.json()

def main():
    st.title("PIKU x GPT ")
    query = st.text_input("Enter a question regarding your plum policy and benefits")
    submit = st.button("Submit")
    if submit:
        result = api_call(query)
        st.write("Tokens used:"+ str(result['tokens']))
        st.markdown(result['answer'].replace('\n', '<br>'), unsafe_allow_html=True)

if __name__ == '__main__':
    main()
