import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")
st.title("🎓 Student AI Chatbot")
st.caption("Ask any questions related to your studies and learning here!")

# User inputs
api_key = st.text_input("Enter your Google Gemini API key:", type="password")
user_question = st.text_input("Type your question here...")

# Process user prompt
if user_question:
    if not api_key:
        st.error("Please enter a valid Gemini API Key first!")
    else:
        try:
            genai.configure(api_key=api_key.strip())
            
            # List of active models to try
            models_to_try = [
                'gemini-2.0-flash',
                'gemini-1.5-flash-latest',
                'gemini-pro'
            ]
            
            response = None
            success = False
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    with st.spinner("Generating answer..."):
                        response = model.generate_content(user_question)
                        if response and response.text:
                            st.markdown("### Answer:")
                            st.write(response.text)
                            success = True
                            break
                except Exception:
                    continue  # Fallback to the next model if 404 or error occurs
            
            if not success:
                st.error("Unable to generate a response. Please double-check your API key.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
