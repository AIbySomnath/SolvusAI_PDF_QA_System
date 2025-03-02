# SolvusAI: Llama3-Powered PDF Q&A 🚀📄

## 📌 Introduction
SolvusAI is an advanced AI-powered PDF Q&A system leveraging **Llama3** and **Groq API** to enable intelligent document processing. This application allows users to **upload PDF files**, **extract insights**, and **interact via a chatbot** to receive accurate and context-aware responses.

With **cutting-edge Retrieval-Augmented Generation (RAG)** and **state-of-the-art embeddings**, this system efficiently processes large PDF documents, retrieves relevant information, and provides precise answers to user queries.

---

## 🎯 Key Features
✅ **Smart PDF Processing** – Converts PDF content into structured data.  
✅ **Llama3-Powered Q&A** – AI-driven responses based on document content.  
✅ **Fast Vector Search** – Utilizes FAISS for efficient document retrieval.  
✅ **Interactive UI** – Seamlessly interact through a user-friendly **Streamlit** interface.  
✅ **Scalable & Optimized** – Leverages **Groq API** for fast and accurate inference.  
✅ **Secure & Private** – No data storage; responses are generated in real-time.  
✅ **Multi-Format Support** – Handles PDF, DOC, text, and even image-based documents.  

---

## 📂 Technologies Used
🚀 **Python** – Backend logic & processing.  
🚀 **Streamlit** – Interactive web UI for seamless interaction.  
🚀 **LangChain** – LLM orchestration & response generation.  
🚀 **FAISS** – High-performance vector search for document retrieval.  
🚀 **Groq API** – Fast LLM inference for Q&A generation.  
🚀 **Hugging Face Embeddings** – For text chunk embedding & retrieval.  
🚀 **PyPDFLoader** – Efficient PDF content extraction.  

---

## 📌 How It Works
1️⃣ **Upload a PDF** – The system processes the document and converts it into embeddings.  
2️⃣ **Vector Database Creation** – Extracted text is chunked and stored in **FAISS** for fast retrieval.  
3️⃣ **Ask Questions** – Type a query related to the uploaded PDF.  
4️⃣ **Llama3 Responds** – The system retrieves relevant content and generates an accurate response.  

---

## 🚀 Live Demo
🔗 Try it out here: [SolvusAI Live Demo](https://solvusaipdfappsystem-ekuropqqzraatdzzjjz8yn.streamlit.app/)  
🎥 **Demo Video:** [Click Here](streamlit-app-2024-07-14-01-07-88.mp4)  

---

## ⚡ Challenges & General Problems Solved

### 🏆 Overcoming OCR & Low-Quality Document Limitations
Many AI-powered document processing tools, including **ChatGPT, Gemini, and other LLMs**, struggle with low-quality, blurred, or handwritten PDFs. **Traditional OCR models often fail to extract meaningful data**, leading to incomplete or incorrect responses. However, SolvusAI has been designed to **excel in low-quality and multi-format document processing** by:

✅ **Leveraging Multimodal Capabilities** – Unlike other models, SolvusAI can process PDFs, DOC files, plain text, and even images with embedded text.  
✅ **Advanced OCR Integration** – Our pipeline enhances **text recognition** and **information extraction**, ensuring reliable results even for **blurred, noisy, or handwritten** documents.  
✅ **Robust Preprocessing** – Implementing **image enhancement and adaptive thresholding** to improve OCR accuracy before embedding creation.  
✅ **Optimized for Real-World Use** – Works well with scanned contracts, historical records, invoices, and other complex documents where standard OCR fails.  

This unique capability sets SolvusAI apart from other LLM-powered PDF Q&A solutions and ensures **high reliability in diverse scenarios**.  

---

## 🛠️ Installation & Setup
### Prerequisites:
- Python 3.8+
- Groq API Key
- Required dependencies (Install via `requirements.txt`)

### Installation Steps:
```bash
# Clone the repository
git clone https://github.com/your-repo/SolvusAI_QA.git
cd SolvusAI_QA

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Setting Up API Key
To securely store the **Groq API Key**, follow these steps:
1️⃣ **Using Streamlit Secrets Manager**  
   - Open your Streamlit app → **Settings** → **Secrets**  
   - Add the following entry:  
     ```ini
     GROQ_API_KEY = "your-api-key-here"
     ```
2️⃣ Alternatively, use environment variables:  
   ```bash
   export GROQ_API_KEY=your-api-key-here
   ```

---

## 🔍 Evaluation Criteria
✅ **OCR Accuracy** – How well the text is extracted from PDFs.  
✅ **Summarization Quality** – The ability to generate concise and meaningful document summaries.  
✅ **Chatbot Response Quality** – Relevance and correctness of AI-generated answers.  
✅ **Code Structure & Maintainability** – Clean, efficient, and well-documented code.  
✅ **Error Handling & Robustness** – Graceful handling of failures and unexpected inputs.  
✅ **RAG Implementation** – Effectiveness of retrieval and response generation.  

---

## 🤝 Contributing
We welcome contributions! Feel free to fork the repo, raise issues, or submit pull requests to enhance the functionality of **SolvusAI**.

---

## 📩 Support
For any queries or issues, please contact:  
📧 **Email:** support@solvusai.com  
🌐 **Website:** [SolvusAI.com](https://solvusai.com)  

---

🔥 **Transform Your PDFs into Actionable Insights – Try SolvusAI Today!** 🔥

