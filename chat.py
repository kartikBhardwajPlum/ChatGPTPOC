import streamlit as st
import requests

st.set_page_config(page_title="PlumChatBot", page_icon=":guardsman:", layout="wide")

def api_call(query):
    response = requests.post(url="https://employee-experience-service-uydiiifsnq-el.a.run.app/api/v1/chat/question?question="+query,headers={"x-plum-internal-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6IlZnUEg4SFNNYzBrVlZDYWZRRzRyIiwic291cmNlIjoiTUVNQkVSUyIsImVtYWlsSWQiOiJrZWVydGhpLnNpZGRlc2h3YXIrc3R1QHBsdW1ocS5jb20iLCJpYXQiOjE2NzU4NTk0NjEsImV4cCI6MTcyMjc4NTk0NjF9.hQtQeIlIpSyy1C2WkbaGZvcQEFWOq_JDzWb_Rwh0Mig"})
    return response.json()

def main():
    st.title("PIKU OP ")
    st.markdown("Ask a question about your policy.")
    st.write("Here are some prompts:")
    st.markdown("`* What is my maternity coverage?`")
    st.markdown("`* How to file a claim in plum app?`")
    st.markdown("`* Do I have any waiting periods?`")
    st.markdown(">Tip: Assume you are new to insurance and plum, then ask questions about your coverages, or ask explanations of any terms and conditions. ")
    query = st.text_input("Enter your question")
    if st.button("Ask"):
        with st.spinner("Generating response..."):
            result = api_call(query)
        st.write("Tokens used:"+ str(result['tokens']))
        st.markdown(result['answer'].replace('\n', '<br>'), unsafe_allow_html=True)

if __name__ == '__main__':
    main()
