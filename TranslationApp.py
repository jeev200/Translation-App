import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

# Model Initialization
ollama_model = OllamaLLM(model="llama3.2")

# Language translation template
lang_template = "In an easy way translate the following sentences '{sentence}' into {target_language}"
lang_prompt = PromptTemplate(
    input_variables=['sentence', "target_language"],
    template=lang_template
)

# Initialize the LLMChain with the Ollama model and the prompt
llm_chain = LLMChain(llm=ollama_model, prompt=lang_prompt)

# Streamlit interface setup
st.set_page_config(page_title="🌍 Language Translator", page_icon="🌐", layout="wide")
st.title("🌍 Language Translator")
st.write("Effortlessly translate text into multiple languages.")

# Sidebar with enhanced examples
st.sidebar.title("💡 **Examples to Try**")
st.sidebar.markdown(
    """
    ✨ **Everyday Conversations**  
    - "How are you?"  
    - "What is your name?"  
    - "I love programming!"  

    🌎 **Travel Phrases**  
    - "Where is the nearest hotel?"  
    - "How much does this cost?"  
    - "Can you help me?"  

    💼 **Business Communication**  
    - "Can we schedule a meeting?"  
    - "Please send me the report."  
    - "Looking forward to your reply."  
    """
)

# Input text for translation
st.markdown("### 📝 Enter text for translation:")
user_input = st.text_area("Type your text below:", placeholder="Type something here...", height=150)

# Dropdown for target language
st.markdown("### 🌐 Select a target language:")
languages = {
    "Hindi": "hi",
    "Telugu": "te",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "English" : "en"
}
target_language = st.selectbox("Choose from the list:", list(languages.keys()))

# Translation button
if st.button("🔄 Translate Now"):
    if user_input and target_language:
        # Get language code
        target_language_code = languages[target_language]

        # Invoke the model
        response = llm_chain.invoke({'sentence': user_input, 'target_language': target_language_code})

        # Display the translation
        st.markdown("### 🔊 Translated Output:")
        if 'text' in response:
            st.success(response['text'])
        elif 'result' in response:
            st.success(response['result'])
        else:
            st.error("⚠️ Unexpected response format. Please check the input or try again.")
    else:
        st.error("⚠️ Please enter text and select a target language!")

# Footer with styling
st.markdown(
    """
    ---
    👨‍💻 **Built with [Streamlit](https://streamlit.io/) by Jeevana :) **  
    💡 **Tip**: Explore more by trying different languages and phrases!  
    """
)
