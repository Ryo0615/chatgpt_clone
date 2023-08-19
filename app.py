import os
import openai
import streamlit as st

openai.api_key = os.environ["OPENAI_API_KEY"]

def get_gpt3_response(messages: list) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response.choices[0].message['content'].strip()

def main():
    st.title("ChatGPT Clone")

    # Session state for retaining messages
    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "私はAIアシスタントです。何かお手伝いしましょうか？"}]

    # Placeholder for chat history
    chat_history_placeholder = st.container()

    # Input for the user message
    user_message = st.text_input("Your Message")

    # If user has entered a new message
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
        gpt3_response = get_gpt3_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": gpt3_response})

    # Display chat history within the placeholder
    with chat_history_placeholder :
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.info(f"{message['content']}", icon = "🙂")
            elif message["role"] == "assistant":
                st.info(f"{message['content']}", icon = "🤖")


if __name__ == "__main__":
    main()
