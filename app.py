import os
import re
import streamlit as st
from openai import OpenAI
from iso_639_languages import iso_639_languages

st.set_page_config(layout="wide")

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key",
        key="chatbot_api_key",
        type="password",
        help="Enter your OpenAI API key. The key is not stored and is only used for this session.",
        value=os.getenv("OPENAI_API_KEY", "")
    )
    "[How to get an OpenAI API key?](https://platform.openai.com/account/api-keys)"
    custom_api_base = st.text_input(
        "Custom OpenAI Server URL (Optional)",
        key="custom_api_base",
        help="Leave empty to use default OpenAI servers",
        value=os.getenv("CUSTOM_API_BASE", "")
    )
    custom_model = st.text_input(
        "Custom Model (Optional)",
        key="custom_model",
        help="Enter custom model name if different from 'whisper-1'",
        value=os.getenv("CUSTOM_MODEL", "whisper-1")
    )

st.header('Whisper WebUI', divider='violet')
st.caption('created by Education Victory')

st.subheader("What do you want Whisper to do for you?", divider=True)
usecase_option = st.selectbox(
    "transcription or translation",
    ("Create transcription", "Create translation"),
)

st.subheader("Audio file", divider=True)
audio_file = st.file_uploader('Choose an audio file', type=["flac", "m4a", "mp3", "mp4", "mpeg", "mpga", "oga", "ogg", "wav", "webm"])
st.markdown('[How to handle file bigger than 25mb?](https://platform.openai.com/docs/guides/speech-to-text/longer-inputs)')

st.subheader("Option customization", divider=True)
if usecase_option == "Create transcription":
    col1, col2, col3 = st.columns(3)

    with col1:
        language_option = st.selectbox(
            "Input Language (Optional):",
            iso_639_languages.keys()
        )
        st.caption("The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.")
        language_code = iso_639_languages[language_option]

    with col2:
        prompt = st.text_input("Prompt (Optional)", "")
        st.caption("An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language. **For example, 'Generate transcription for this meeting audio'**")

    with col3:
        format_option = st.selectbox(
            "Output Format (Optional):",
            ['json', 'text', 'srt', 'verbose_json', 'vtt']
        )
        st.caption("The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.")

    if audio_file:
        if not openai_api_key:
            st.info("Please add your OpenAI API key in the sidebar to continue.")
            st.stop()
        # Button to start transcription
        if st.button('Transcribe Audio'):
            # Set the OpenAI API key and custom server (if provided)
            if custom_api_base:
                client = OpenAI(api_key=openai_api_key, base_url=custom_api_base)
            else:
                client = OpenAI(api_key=openai_api_key)
            # Call the OpenAI API for transcription
            with st.spinner('Processing...'):
                transcription = client.audio.transcriptions.create(
                    model=custom_model if custom_model else "whisper-1",
                    file=audio_file,
                    language=language_code,
                    prompt=prompt,
                    response_format=format_option,
                )
                if format_option == 'json':
                    with st.container(border=True):
                        st.json(transcription.to_json())
                elif format_option == 'text':
                    container = st.container(border=True)
                    container.write(transcription)
                elif format_option == 'verbose_json':
                    with st.container(border=True):
                        st.json(transcription.to_json())
                elif format_option == 'vtt':
                    container = st.container(border=True)
                    container.write(transcription)
                elif format_option == 'srt':
                    # Provide a download button for the SRT file
                    st.download_button(label='Click To Download SRT File', data=transcription, file_name=audio_file.name + '.srt')

elif usecase_option == "Create translation":
    col1, col2 = st.columns(2)

    with col1:
        prompt = st.text_input("Prompt (Optional)", "")
        st.caption("An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language. **For example, 'Translate this Chinese audio to professional and concise English'**")

    with col2:
        format_option = st.selectbox(
            "Output Format (Optional):",
            ['json', 'text', 'srt', 'verbose_json', 'vtt']
        )
        st.caption("The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.")

    if audio_file:
        if not openai_api_key:
            st.info("Please add your OpenAI API key in the sidebar to continue.")
            st.stop()
        # Button to start translation
        if st.button('Translation Audio'):
            # Set the OpenAI API key and custom server (if provided)
            if custom_api_base:
                client = OpenAI(api_key=openai_api_key, base_url=custom_api_base)
            else:
                client = OpenAI(api_key=openai_api_key)
            # Call the OpenAI API for translation
            with st.spinner('Processing...'):
                translation = client.audio.translations.create(
                    model=custom_model if custom_model else "whisper-1",
                    file=audio_file,
                    prompt=prompt,
                    response_format=format_option,
                )
                if format_option == 'json':
                    with st.container(border=True):
                        st.json(translation.to_json())
                elif format_option == 'text':
                    container = st.container(border=True)
                    container.write(translation)
                elif format_option == 'verbose_json':
                    with st.container(border=True):
                        st.json(translation.to_json())
                elif format_option == 'vtt':
                    container = st.container(border=True)
                    container.write(translation)
                elif format_option == 'srt':
                    # Provide a download button for the SRT file
                    st.download_button(label='Click To Download SRT File', data=translation, file_name=audio_file.name + '.srt')
