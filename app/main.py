import streamlit as st
import pandas as pd
from chatbot import process_query
from charts import revenue_chart
from charts import net_income_chart

st.set_page_config(
    page_title="Financial Analyst",
    layout="wide"
)

# Load data at the top so it's available for all tabs
df = pd.read_excel(
    "data/BCG_GenAI_Financial_Data_Extraction_Example.xlsx",
    sheet_name="Extracted Data"
)

# Sidebar for overall navigation context
with st.sidebar:
    st.title("📊 Financial Analyst")
    st.markdown(
        """
        Analyze Microsoft, Apple and Tesla
        using financial data extracted from
        their 10-K reports.
        """
    )
    st.info("Navigate through the tabs on the right to interact with the AI, view the dashboard, or inspect the raw data.")

# Main navigation using Tabs
tab1, tab2, tab3 = st.tabs(["💬 AI Chatbot", "📈 Dashboard", "🗄️ Raw Data"])

with tab1:
    st.subheader("Financial Analyst Copilot")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    query = st.chat_input("Ask a financial question...")

    if query:
        # Add user message to state
        st.session_state.messages.append({"role": "user", "content": query})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(query)
            
        # Get AI response
        answer = process_query(query)
        
        # Add AI message to state
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        # Display AI message immediately
        with st.chat_message("assistant"):
            st.markdown(answer)

with tab2:
    st.subheader("Financial Performance Dashboard")
    
    # Place charts side-by-side using columns for a better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(revenue_chart(df), use_container_width=True)
        
    with col2:
        st.plotly_chart(net_income_chart(df), use_container_width=True)

with tab3:
    st.subheader("Raw Financial Dataset")
    st.dataframe(df, use_container_width=True)
