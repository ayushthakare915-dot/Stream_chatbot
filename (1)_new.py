
# import streamlit as st

# st.title("My GenAI App")
# st.write("Hello Ayush! 🚀")
# st.header("Heyyyyy")
# name=st.text_input("Enter you're name")
# st.write(name)
# if st.button("Click me"):
#     st.write("Button is clickked")
# age=st.number_input("Enter the num")
# age=st.slider("Enter age",1,100)
# course=st.selectbox("Choose your course",["Java","python","C"])
# agree = st.checkbox("I agree")
# disclaimer = st.checkbox("Disclaimer")
# radio=st.radio("Choose your gender",["male","female"])
# txt=st.text_area("txt box.....")
# st.file_uploader("Upload file",type=("txt","pdf"))
# st.sidebar.title("On left plss..")
# upload=st.sidebar.checkbox("hii")
# select=st.sidebar.text_area("feed me")
# col1,col2=st.columns(2) #-------------------------mention before creating column(2)
# with col1:
#     st.header("Header")
# with col2:
#     st.header("Footer")
# input=st.chat_input("Sayy dadddy")
# if input:
#     with st.chat_message("user"): #------------------(Imp)-----always user with Same spell for chatbot
#         st.write(input)
#     with st.chat_message("assistant"): #-------------(Imp)-----||---------------------------
#         st.write("Heyy This is this your assistance")


# # Ollama Import in Vs code:
# import ollama
# question=input("Ask your question  ")
# response=ollama.chat(
#     model="llama3.2",
#     messages=[
#         {
#             "role":"user",
#             "content":question
#         }
#     ]
# )
# answer=response["message"]["content"] # it means we want content to print in msg
# print(answer)


# Integrate ollama and streamlit {chatbot}:
# import streamlit as st
# import ollama
# st.title("Chat with ollama")
# question=st.text_input("Ask daddyy.....")
# response=ollama.chat(
#     model="llama3.2",
#     messages=[
#         {
#             "role":"user",
#             "content":question
#         }
#     ]
# )
# answer=response["message"]["content"]
# st.write(answer)

# Chat gpt clone project :
import streamlit as st
import ollama
question=st.chat_input("Ask daddyy.....")
if question:
    with st.chat_message("user"):
        st.write(question)
response=ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":question
        }
    ]
)
answer=response["message"]["content"]
with st.chat_message("assistant"):
    st.write(answer)