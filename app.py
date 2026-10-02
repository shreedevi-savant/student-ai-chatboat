import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")
st.title("🎓 Student AI Chatbot")
st.caption("Ask any questions related to your studies and learning here!")

# User Input Fields
api_key = st.text_input("Enter your Google Gemini API key:", type="password")
user_question = st.text_input("Type your question here...")

# Process Question
if user_question:
    if not api_key:
        st.error("Please enter a valid Gemini API Key first!")
    else:
        try:
            # Configure API key only when requested
            genai.configure(api_key=api_key.strip())
            
            # List of models to try in case one hits quota limits
            fallback_models = [
                'gemini-1.5-flash-8b',
                'gemini-2.5-flash',
                'gemini-1.5-flash'
            ]
            
            response = None
            success = False
            
            # Loop through models until one responds
            for model_name in fallback_models:
                try:
                    model = genai.GenerativeModel(model_name)
                    with st.spinner(f"Generating answer using {model_name}..."):
                        res = model.generate_content(user_question)
                        if res and res.text:
                            st.markdown("### Answer:")
                            st.write(res.text)
                            success = True
                            break
                except Exception:
                    continue  # Try the next model if this one fails
            
            if not success:
                st.error("Quota limit reached across all models. Please generate a NEW API key from a new project in Google AI Studio.")

        except Exception as e:
            st.error(f"Error connecting to Gemini API: {str(e)}")
