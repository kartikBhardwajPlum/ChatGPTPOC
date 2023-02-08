import streamlit as st
import requests

st.set_page_config(page_title="Streamlit API Example", page_icon=":guardsman:", layout="wide")

def api_call(query):
    response = requests.post(url="http://localhost:5051/api/v1/chat/question?question="+query, headers={"x-plum-internal-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImthcnRpay5iQHBsdW1ocS5jb20iLCJmaXJzdE5hbWUiOiJLYXJ0aWsiLCJsYXN0TmFtZSI6IkJoYXJkd2FqIEgiLCJvcmdhbmlzYXRpb25JZCI6IkROb0QzQWw2NTZqMEE0emJpUENpIiwidWlkIjoiN2FrS0pobEwxc09LUWRLY3VpeFlLUDBQOWF3MiIsInBob25lTnVtYmVyIjoiOTA5NDQ5NTQwMCIsIndpdGhvdXRNZW1iZXJzaGlwIjpmYWxzZSwicmVtb3ZlZCI6ZmFsc2UsImFkbWluIjp0cnVlLCJzdXBlciI6ZmFsc2UsImludml0ZUlkIjoiMzBjYWZiNzYtZTNmNy00ZWIyLTlkOWEtZjU4NzljNjc5OTA4IiwiZWlkIjoiUDM4NSIsImlzT1RQdmVyaWZpZWQiOnRydWUsIndoYXRzYXBwT3B0SW4iOiJPUFRfSU4iLCJlbnJvbGxtZW50U3RhdHVzIjoiQ09NUExFVEUiLCJnZW5kZXIiOiJNQUxFIiwiZGF0ZU9mQmlydGgiOnsiZGF0ZSI6MTUsIm1vbnRoIjoiRmVicnVhcnkiLCJtb250aE51bWJlciI6MiwieWVhciI6MjAwMX0sIm1lbWJlcklkIjoiN3JvVkpZZUJRWEk3a2JHS0tubnEiLCJzb3VyY2UiOiJNRU1CRVJTIiwiZW1haWxJZCI6ImthcnRpay5iQHBsdW1ocS5jb20iLCJpYXQiOjE2NzU3NjQzNjQsImV4cCI6MTcyMjc3NjQzNjR9.H4fUofd7gmRdD_54fus0BsdjeE12uC9U_kGwJZJZFrg"})
    return response.json()

def main():
    st.title("CHAT GPT POC")
    query = st.text_input("Enter a question regarding your plum policy and benefits")
    submit = st.button("Submit")
    if submit:
        result = api_call(query)
        st.write("Result:", result['choices'][0]['text'])

if __name__ == '__main__':
    main()
