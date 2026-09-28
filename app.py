import streamlit as st
from google import genai

st.set_page_config(page_title="Student AI Chatbot", page_icon="🎓")

st.title("🎓 Student AI Chatbot")
st.write("Ask any questions related to your studies and learning here!")

# API Key input
api_key = st.text_input("Enter your Google Gemini API Key:", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display prior chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Type your question here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response using Gemini
        with st.chat_message("assistant"):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                answer = response.text
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Please enter your Google Gemini API Key to continue.")

