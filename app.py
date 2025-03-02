import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

# Load environment variables
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

# Streamlit UI
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>SolvusAI: Llama3-Powered PDF Q&A 🚀📄</h1>
    <h4 style='text-align: center; color: #666;'>Upload a PDF and ask questions interactively!</h4>
    <hr>
""", unsafe_allow_html=True)

# Initialize LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Prompt Template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided context only.
    Provide the most accurate response.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

def create_vector_db(pdf_file):
    """Process PDF, extract text, and create vector database."""
    if "vector_store" not in st.session_state:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(pdf_file.read())
            pdf_path = temp_file.name

        st.session_state.embeddings = HuggingFaceEmbeddings(
            model_name='BAAI/bge-small-en-v1.5', model_kwargs={'device': 'cpu'}, encode_kwargs={'normalize_embeddings': True}
        )
        st.session_state.loader = PyPDFLoader(pdf_path)
        st.session_state.text_documents = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_chunks = st.session_state.text_splitter.split_documents(st.session_state.text_documents)
        st.session_state.vector_store = FAISS.from_documents(st.session_state.final_chunks, st.session_state.embeddings)

# Upload PDF Section
pdf_file = st.file_uploader("📂 Upload a PDF", type=['pdf'])

if pdf_file is not None:
    if st.button("🔄 Create Vector DB"):
        create_vector_db(pdf_file)
        st.success("✅ Vector Database is Ready!")

# Q&A Section
if "vector_store" in st.session_state:
    user_question = st.text_input("💬 Ask a question about the PDF")
    if st.button("🚀 Get Answer"):
        if user_question:
            document_chain = create_stuff_documents_chain(llm, prompt)
            retriever = st.session_state.vector_store.as_retriever()
            retrieval_chain = create_retrieval_chain(retriever, document_chain)
            response = retrieval_chain.invoke({'input': user_question})
            st.write(f"**🤖 AI Answer:** {response['answer']}")
        else:
            st.error("❌ Please enter a question!")
