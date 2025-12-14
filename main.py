import pandas as pd
import streamlit as st
import os  # NEW: To read environment variables
from dotenv import load_dotenv  # NEW: To load the .env file
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq

# NEW: Load environment variables from .env file
load_dotenv()

# Streamlit web app configuration
st.set_page_config(
    page_title="DF Chat",
    page_icon="💬",
    layout="centered"
)


def read_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)


st.title("🤖 TalkToData: Generative AI Analytics Tool")

# --- REMOVED: Sidebar input is no longer needed ---

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "df" not in st.session_state:
    st.session_state.df = None

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    st.session_state.df = read_data(uploaded_file)
    st.write("DataFrame Preview:")
    st.dataframe(st.session_state.df.head())

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Ask LLM...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content": user_prompt})

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    # UPDATED PART HERE:
    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        st.session_state.df,
        verbose=True,
        # Use string "openai-tools" instead of AgentType.OPENAI_FUNCTIONS
        agent_type="openai-tools",
        allow_dangerous_code=True
    )

    try:
        response = pandas_df_agent.invoke({"input": user_prompt})
        assistant_response = response["output"]

        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error(f"Error: {e}")