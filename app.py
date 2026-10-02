import streamlit as st
import google.generativeai as genai

# App Layout
st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")
st.title("🎓 Student AI Chatbot")
st.caption("Ask any questions related to your studies and learning here!")

# API Key Input
api_key = st.text_input("Enter your Google Gemini API key:", type="password")

if api_key:
    # Configure Gemini API
    genai.configure(api_key=api_key)
    
    # Using gemini-1.5-flash for faster responses and lower error rates
    model = genai.GenerativeModel('gemini-1.5-flash')

    # User Input
    user_question = st.text_input("Type your question here...")

    if user_question:
        try:
            with st.spinner("Generating answer..."):
                response = model.generate_content(user_question)
                st.markdown("### Answer:")
                st.write(response.text)
        except Exception as e:
            # Clean error handling to prevent app crashes on 503 or quota limits
            st.error("⚠️ The server is currently busy or the quota limit was reached. Please wait 10–15 seconds and try again.")
else:
    st.info("Please enter your Gemini API key above to start asking questions.")
