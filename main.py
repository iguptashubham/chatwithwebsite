import streamlit as st 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from langchain_core.messages import AIMessage,HumanMessage
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import google.generativeai as geminiai
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv

#-------------------api configuration............
load_dotenv()
geminiai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#-----------------------Web app page confirguration---------------------------
st.set_page_config(page_title='AI RAG Chat with Website', layout='wide')
st.title(":blue[AI RAG] Chat with Website")
st.write("An AI RAG (Retrieval-Augmented Generation) chat with a website is a sophisticated tool that enhances user interactions by combining retrieval-based methods with generative AI models. Users can input queries, and the system retrieves relevant information from a vast database, then generates coherent and contextually accurate responses. This makes the interaction more informative and engaging, essentially acting like a supercharged search engine that not only finds information but also presents it in a conversational manner. ")

#------------------all Function...........

def get_vector_store_from_url(url):
    loader = WebBaseLoader(url)
    document = loader.load()
    #split document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(documents=document)
    vector_store = Chroma.from_documents(documents=document_chunks,
                                         embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001'))
    return vector_store

def get_context_retriver(vector_store):
    llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro',temperature=0.3)
    retriver = vector_store.as_retriever()
    prompt = ChatPromptTemplate.from_messages([
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
      ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    ])
    
    retriver_chain = create_history_aware_retriever(llm=llm, retriever=retriver, prompt=prompt)
    return retriver_chain

def get_conversation_rag(retriver_chain):
    llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro',temperature=0.3)
    rag_prompt = ChatPromptTemplate.from_messages([
      ("system", "Answer the user's questions based on the below context:\n\n{context}"),
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
    ])
    stuff_chain = create_stuff_documents_chain(llm=llm,prompt=rag_prompt)
    return create_retrieval_chain(retriver_chain,stuff_chain,)



#-------------------Chat-history---------------


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[
    AIMessage(content='Hi how are you'),
]
#--------------------Columns--------------------
c1,c2 = st.columns([0.25,0.75])

#------------column_1................

with c1:
    with st.container(border=True):
        link1=st.text_input(label='Paste link here',help='Paste the website link you want to chat')
        if link1:
            vector_store1 = get_vector_store_from_url(url=link1)
            retriver_chain = get_context_retriver(vector_store=vector_store1)
            rag_conversation = get_conversation_rag(retriver_chain)
    with st.container(border=True):
        c3,c4 = st.columns([0.3,0.7])
        st.markdown('##### Built By')
        with c3:
            st.write("##### Shubham Gupta")
        with c4:
            st.write("GenAI/ML Engineer, Data Scientist")

#------------column_2.......

with c2:
    with st.container(border=True):
        user_query = st.chat_input('Enter Question Heres')
        if user_query:
            response= rag_conversation.invoke({
                "chat_history":st.session_state.chat_history,
                "input":'user_query'
            })
            st.session_state.chat_history.append(HumanMessage(content=user_query))
            st.session_state.chat_history.append(AIMessage(content=response['answer']))
            
#---------------conversation.............

with c2:
    with st.container(border=True):
        for message in st.session_state.chat_history:
            if isinstance(message,AIMessage):
                with st.chat_message('ai'):
                    st.write(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message('human'):
                    st.write(message.content)
                    
#----------------Chat History............
    
with c1:
    with st.expander('Chat History'):
        st.write(st.session_state.chat_history)
        
        