# 🤖 Sonus


![enter image description here](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=fff)

![enter image description here](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

![Static Badge](https://img.shields.io/badge/build-Open%20Soruce-brightgreen?style=flat&label=Type) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
***

> This project was created for the Google AI Hackathon 2024. This
> project is  proof of concept and can be scaled to a wider audience and
> integrated with multiple platforms.

*** 
## 💼 Business Use Case: Enhancing Productivity in Corporate Meetings with Sonus

**Background:**

In the fast-paced corporate world, efficiency and productivity are paramount. Companies are constantly seeking solutions that can save time and improve the quality of work. One of the significant challenges businesses face is managing the vast amount of information shared during meetings. Important insights and decisions often get buried in hours of recordings, making it hard for teams to capture the essence of discussions and act upon them promptly.

**Problem Statement:**

The manual process of summarizing key points from lengthy meeting recordings is time-consuming and prone to errors. This inefficiency leads to delayed decision-making, overlooked information, and a general decrease in productivity. There is a pressing need for an automated solution that can quickly and accurately distill the important information from audio recordings of meetings.

**Solution: Sonus - AI-powered Voice Note Summarization Tool:**

Sonus provides an innovative solution to the problem of managing and summarizing audio content from corporate meetings. Utilizing the Google Gemini Pro AI model, Sonus offers a suite of features tailored to enhance productivity and information management in a business setting:

1. **Live Recording for Instant Summarization:** Teams can record live meetings directly through Sonus. This feature ensures that all discussions are captured in real-time, allowing for immediate summarization and review.

2. **Comprehensive File Uploader:** Sonus supports a wide range of audio formats, enabling teams to upload recordings from various sources. This flexibility ensures that no matter how the audio was captured, it can be easily imported and processed.

3. **Automated Summary Generation:** With the push of a button, Sonus generates concise and accurate summaries of the uploaded or recorded audio. This feature harnesses the power of the Gemini Pro model to extract key points and decisions from the discussions, significantly reducing the manual effort required.

4. **Easy Access and Distribution:** The generated summaries can be viewed directly within Sonus and downloaded as text documents. This convenience allows for easy distribution among team members, ensuring everyone is on the same page and can quickly refer back to the important points discussed.

**Business Impact:**

- **Increased Efficiency:** By automating the process of summarizing meeting recordings, Sonus significantly reduces the time and effort required to extract actionable insights from meetings.
- **Improved Decision Making:** With easy access to concise summaries, teams can make informed decisions more quickly, accelerating the business process.
- **Enhanced Collaboration:** Sonus facilitates better communication among team members by providing a clear and accessible record of discussions and decisions.
- **Cost Savings:** Reducing the manual effort involved in summarizing meetings translates into direct labor cost savings for businesses.


Sonus revolutionizes the way businesses handle information from meetings, transforming hours of audio into concise, actionable summaries. By integrating Sonus into their workflow, companies can enhance productivity, streamline decision-making processes, and foster a more collaborative work environment.

  

## 🔨 Features

1.  **Live Recording:** Users can record audio live for generating a summary.

2.  **File Uploader:** Users can upload audio for generating a summary. Supports uploading audio files in formats such as 'flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', and 'webm'.

3.  **Generate Summary:** Generates a summary for the uploaded or recorded audio file using the Google Gemini Pro model. Users can view the summary and download it as a text document.

  

## 💻 Usage

1.  **Live Recording:**

- Use the `streamlit_mic_recorder` package to enable live recording.

- The transcription of the recorded audio will be displayed in the expander section

2.  **File Uploader:**

- Upload your audio file using the file upload component.

- The transcription of the uploaded audio will be displayed in the expander section.

3.  **Generate Summary:**

- After uploading/recording the audio file, click the "Generate summary" button to create a summary.

- The summary will be generated using the Gemini Pro model and displayed in the expander section.

- You can also download the summary as a text document using the "Download summary" button.
4. **Running:**
- To run the application simply install the requirement files. Then type `streamlit run app.py`

  
## 🕵🏻 Testing

The application includes unit tests to ensure its functionality. The `test_app.py` file contains unit tests for different components of the application.