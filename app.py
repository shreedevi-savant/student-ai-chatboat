import streamlit as st
import google.generativeai as genai

# App Layout
st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")
st.title("🎓 Student AI Chatbot")
st.caption("Ask any questions related to your studies and learning here!")

# API Key Input
api_key = st.text_input("Enter your Google Gemini API key:", type="password")

# User Input
user_question = st.text_input("Type your question here...")

if user_question:
    if not api_key:
        st.error("Please enter a valid Gemini API Key first!")
    else:
        try:
            # Configure API key only when user asks a question
            genai.configure(api_key=api_key.strip())
            
            # Using the stable fast model
            model = genai.GenerativeModel('gemini-1.5-flash-8b')
            
            with st.spinner("Generating answer..."):
                response = model.generate_content(user_question)
                st.markdown("### Answer:")
                st.write(response.text)
                
        except Exception as e:
            st.error("The server is currently busy or the quota limit was reached. Please check your API key or wait a few seconds.")
