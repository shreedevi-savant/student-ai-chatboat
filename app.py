import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")
st.title("🎓 Student AI Chatbot")
st.caption("Ask any questions related to your studies and learning here!")

api_key = st.text_input("Enter your Google Gemini API key:", type="password")
user_question = st.text_input("Type your question here...")

if user_question:
    if not api_key:
        st.error("Please enter a valid Gemini API Key first!")
    else:
        try:
            genai.configure(api_key=api_key.strip())
            model = genai.GenerativeModel('gemini-1.5-flash-8b')
            
            with st.spinner("Generating answer..."):
                response = model.generate_content(user_question)
                st.markdown("### Answer:")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
