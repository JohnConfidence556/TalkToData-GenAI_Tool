# 🤖 TalkToData: Generative AI Analytics Tool

**TalkToData** is an intelligent conversational analytics tool that allows users to "chat" with their structured data. Built with **Streamlit**, **LangChain**, and **Groq**, it transforms static CSV and Excel files into interactive conversations, enabling non-technical users to extract insights using plain English.

---

## 🚀 Features

* **Natural Language Queries:** Ask questions like "What is the total revenue?" or "Plot the sales trend" without writing code.
* **Multi-Format Support:** Compatible with `.csv`, `.xlsx`, and `.xls` files.
* **High-Speed Inference:** Powered by **Groq's LPU** and the **Llama 3.3-70b** model for lightning-fast responses.
* **Autonomous Agent:** Uses LangChain's DataFrame Agent to write, execute, and validate Python code in real-time.
* **Secure:** API keys are managed securely via environment variables and Streamlit Secrets.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM Engine:** [Groq API](https://groq.com/) (Model: `llama-3.3-70b-versatile`)
* **Orchestration:** [LangChain](https://www.langchain.com/) (Agents & Tools)
* **Data Processing:** [Pandas](https://pandas.pydata.org/)
* **Environment:** Python-dotenv

---

## ⚙️ Installation & Local Setup

Follow these steps to run the application on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/TalkToData.git](https://github.com/your-username/TalkToData.git)
cd TalkToData
```
### 2. Create a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
1. Create a file named .env in the root directory.
2. Add your Groq API key:
```bash
GROQ_API_KEY=your_actual_api_key_here

Note: You can get a free API key from the Groq Console.
```

### 5. Run the Application
```bash
streamlit run main.py
```
The app should launch automatically in your browser at http://localhost:8501.
