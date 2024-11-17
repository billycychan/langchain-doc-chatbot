from backend.core import run_llm, MODEL_NAME
import streamlit as st
from streamlit_chat import message


# Configure the Streamlit page
st.set_page_config(
    page_title="AI Langchain Documentation Helper", page_icon="💻", layout="centered"
)

# Custom CSS for dark mode
st.markdown(
    """
<style>
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #FFFFFF;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #1E88E5;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    
    .stButton button:hover {
        background-color: #1565C0;
    }
    
    /* Text input styling */
    .stTextInput input {
        background-color: #1E1E1E;
        color: #FFFFFF;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 10px;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    
    /* Divider styling */
    hr {
        border-color: #333333;
    }
    
    /* Info box styling */
    .stAlert {
        background-color: #1E1E1E;
        border: 1px solid #333333;
        color: #FFFFFF;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Add sidebar with user information
with st.sidebar:
    st.title("👤 User Profile")

    # Display Billy Chan's information
    st.image(
        "https://media.licdn.com/dms/image/v2/D5603AQFXyZxjrK1Usw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1725337766268?e=1737590400&v=beta&t=77hxviuvRAiTCrryVSieaWl9PsPwgISZjILLhaDu_Hw",
        width=100,
    )
    st.write("👋 Welcome, Billy Chan!")
    st.write("📧 chanc187@mcmaster.ca")
    st.write("[LinkedIn](https://www.linkedin.com/in/billycychan/)")
    st.write("[Github](https://github.com/billycychan)")
    # Add a divider
    st.divider()

# Main content
st.header("AI Langchain Documentation Helper")
st.subheader("A work of smart.")
st.write(
    "A chatbot for the [Langchain documentation  (v0.3)](https://python.langchain.com/api_reference/)"
)

# User input
prompt = st.text_input("Prompt", placeholder="Enter your prompt here...")
if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_answers_history"] = []
    st.session_state["chat_history"] = []


def create_sources_string(source_urls: set[str]) -> str:
    if not source_urls:
        return ""
    source_list = list(source_urls)
    source_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(source_list):
        sources_string += f"{i + 1}, {source}\n"
    return sources_string


if prompt:
    with st.spinner(f"Generating response with 🦙 {MODEL_NAME}..."):
        import time

        time.sleep(3)
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )
        sources = set(
            [doc.metadata["source"] for doc in generated_response["source_documents"]]
        )
        formatted_response = (
            f"{generated_response['result']} \n\n {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))


if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
