import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

languages = [
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean",
    "Russian", "Italian", "Portuguese", "Arabic", "Hindi", "Bengali", "Turkish",
    "Vietnamese", "Thai", "Filipino", "Malay", "Czech"]

st.set_page_config(page_title="Translator Agent", layout="centered")
st.title("AI Translator Agent")
st.write("Created by **Suleman Sehar** Translate your English text to various languages")

text = st.text_area("Enter text to translate:", height=150)
lang = st.selectbox("Select target language:", languages)
btn = st.button("Translate")

if btn and text:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")  # Updated model name
        prompt = f"Translate the following text to {lang}:\n\n {text}"
        # Add safety settings to avoid blocking
        response = model.generate_content(prompt)
        st.success(f"✅ Translation in {lang}:")
        st.markdown(f"**{response.text}**")
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("Common fixes: 1) Check API key 2) Verify model name 3) Review safety settings")