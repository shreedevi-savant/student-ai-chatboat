import streamlit as st
import google.generativeai as genai

# Page setup
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
        try:
            clean_key = api_key.strip()
            genai.configure(api_key=clean_key)
            
            # Automatically find active models supported by your API key
            available_models = [
                m.name for m in genai.list_models() 
                if 'generateContent' in m.supported_generation_methods
            ]
            
            if not available_models:
                st.error("No valid models found for this API key.")
            else:
                # Use the first available supported model
                selected_model = available_models[0]
                model = genai.GenerativeModel(selected_model)
                
                with st.spinner("Generating answer..."):
                    response = model.generate_content(user_question)
                    st.markdown("### Answer:")
                    st.write(response.text)
                    
        except Exception as e:
            st.error(f"Error Details: {str(e)}")
