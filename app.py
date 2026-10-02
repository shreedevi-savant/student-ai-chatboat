import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")
st.title("🎓 Student AI Chatbot")
st.caption("Ask any questions related to your studies and learning here!")

# User inputs
api_key = st.text_input("Enter your Google Gemini API key:", type="password")
user_question = st.text_input("Type your question here...")

if user_question:
    if not api_key:
        st.error("Please enter a valid Gemini API Key first!")
    else:
        clean_key = api_key.strip()
        genai.configure(api_key=clean_key)
        
        # Priority list of supported model endpoints
        candidate_models = [
            'gemini-2.0-flash',
            'gemini-1.5-flash-latest',
            'gemini-pro'
        ]
        
        success = False
        last_error = ""
        
        with st.spinner("Generating answer..."):
            for model_name in candidate_models:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content(user_question)
                    if response and response.text:
                        st.markdown("### Answer:")
                        st.write(response.text)
                        success = True
                        break
                except Exception as e:
                    last_error = str(e)
                    continue
        
        if not success:
            st.error(f"Error Details: {last_error}")
