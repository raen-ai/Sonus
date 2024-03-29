# 🤖 Sonus
An open source tool to summarize voice notes. 

This application is designed to summarize audio files using the Gemini AI model. Users can upload audio files of various formats or record live and generate a summary based on the content of the audio.

## 🔨 Features
1.  **Live Recording:** Users can record audio live for generating a summary.
2.  **File Uploader:** Supports uploading audio files in formats such as 'flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', and 'webm'.
3.  **Generate Summary:** Generates a summary for the uploaded or recorded audio file using the Google Gemini Pro model. Users can view the summary and download it as a text document.

## 💻 Usage
1.  **Live Recording:**
    -   Use the `streamlit_mic_recorder` package to enable live recording.
    -  The transcription of the recorded audio will be displayed in the expander section
2.  **File Uploader:**
    -   Upload your audio file using the file upload component.
    -   The transcription of the uploaded audio will be displayed in the expander section.
3.  **Generate Summary:**
    -   After uploading/recording the audio file, click the "Generate summary" button to create a summary.
    -   The summary will be generated using the Gemini Pro model and displayed in the expander section.
    -   You can also download the summary as a text document using the "Download summary" button.

## 🕵🏻 Testing
The application includes unit tests to ensure its functionality. The `test_app.py` file contains unit tests for different components of the application.
