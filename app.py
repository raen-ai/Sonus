import streamlit as st
from openai import OpenAI
import google.generativeai as genai
import textwrap
from streamlit_mic_recorder import mic_recorder
import io
from requests.exceptions import Timeout, HTTPError
from dotenv import load_dotenv
import os

# loading env variables
load_dotenv()

if "OPENAI_API_KEY" in st.secrets:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
else:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


Supported_formats= ['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm']
# configuring api key
genai.configure(api_key=GEMINI_API_KEY)
# initialising text_doc as None
text_doc = None

# Initialising session variables
if 'live' not in st.session_state:
    st.session_state['live'] = False
if 'upload' not in st.session_state:
    st.session_state['upload'] = False

# returns final prompt
def make_prompt(relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = textwrap.dedent("""You are a helpful and informative bot that sumamrise the below PASSAGE. \
  PASSAGE: '{relevant_passage}'

    ANSWER:
  """).format(relevant_passage=escaped)

  return prompt

# addnig streamlit elements
st.subheader('AI-Powered Audio Summarization Tool', divider='rainbow')
audio_type = st.radio(
    "Choose your audio type",
    ["Live Recording", "File upload"]
    )

# switch the session state based on st.radio output
if audio_type =="Live Recording":
    st.session_state['live']=True
    st.session_state['upload']=False
elif audio_type =="File upload":
    st.session_state['upload']=True
    st.session_state['live']=False

# code for handling upload
if st.session_state['upload']:
    # adding file uploader
    audio=st.file_uploader("upload your audio file",type=Supported_formats)
    if audio is not None:
        # extracting the file extension
        file_format = audio.name.split('.')[-1].lower()

        if file_format in Supported_formats:
            client = OpenAI(api_key=OPENAI_API_KEY)
            # genertaing audio transcription using openai whisper
            result = client.audio.transcriptions.create(model="whisper-1", file=audio)
            if result:
                with st.expander("See Transcription"):
                    # display the transcription
                    st.write(result.text)
                    # writing the contents to global vraiable text_doc
                    text_doc=result.text
        else:
            st.error("Unsupported file format.")

# code for live recording
if st.session_state['live'] :

    st.write("Record your voice:")
    # recorder to recrd the audio live
    audio = mic_recorder(start_prompt="⏺️ Start Recording", stop_prompt="⏹️ End Recording", key='recorder',format='wav')

    if audio:
        st.audio(audio['bytes'])
        # converting to bytesio
        audio_bio = io.BytesIO(audio['bytes'])
        audio_bio.name = 'audio.wav'
        if audio:
            client = OpenAI(api_key=OPENAI_API_KEY)
            # genertaing audio transcription using openai whisper
            result = client.audio.transcriptions.create(model="whisper-1", file=audio_bio)
            if result:
                with st.expander("See Transcription"):
                    # display the transcription
                    st.write(result.text)
                    # writing the contents to global vraiable text_doc
                    text_doc=result.text
        else:
            st.error("Unsupported file format.")

# code to generate summary
if st.button("Generate summary"):
    if text_doc is not None:
        with st.spinner("Summarising..."):
            try:
                prompt = make_prompt(text_doc)
                # using genai model gemini-pro
                model = genai.GenerativeModel('gemini-pro')
                # generate response for the final prompt
                response = model.generate_content(prompt)
            except Timeout:
                st.error("Timeout of 60.0s exceeded. Status code 503. Please Retry.")
            except Exception as e:
                st.error(f"An error occurred. {e}")
                
        with st.expander("See Summary"):
            # display the response contents
            st.write(response.text)

        # button to download the summary
        st.download_button('Download summary', response.text)

    else:
        st.error("Please add your audio.")