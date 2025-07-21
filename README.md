# YouTube Transcript Downloader

**YouTube Transcript Downloader** is a simple and efficient Python script that fetches the transcript of any public YouTube video by its video ID. It saves the transcript into a readable plain text file, enabling easy access, analysis, or further processing of video subtitles.

---

## 🚀 Project Overview

This tool leverages the [`youtube_transcript_api`](https://github.com/jdepoix/youtube-transcript-api) to retrieve the captions from YouTube videos without the need for manual copying or third-party downloaders. Perfect for researchers, content creators, or developers looking to automate transcript extraction.

---

## 🧠 Core Features

- **Transcript Extraction by Video ID**  
  Provide just the YouTube video ID to download the transcript (no full URL required).

- **Save Transcript as Text File**  
  Automatically writes the full transcript into a `transcript.txt` file with clean formatting.

- **Robust Error Handling**  
  Gracefully informs users if a transcript is unavailable or if any error occurs during retrieval.

- **Minimal Dependencies**  
  Uses only the lightweight `youtube_transcript_api` Python package.

---

## ⚙️ Installation & Setup

# Clone this repository  
git clone https://github.com/rabumaabraham/YouTube-Transcript-Downloader.git

# Change directory into the project folder  
cd YouTube Transcript Downloader


# Install the required Python package  
pip install youtube-transcript-api

---

## 💡 Usage Guide

1. Open the Python script and set the `video_id` variable with the desired YouTube video ID (the part after `v=` in a YouTube URL).

video_id = 'EjxL2oB7J-o'

2. Run the script:

python youtube_transcript.py

3. If available, the transcript will be saved in the file `transcript.txt` in the current directory.

4. If the transcript is not found or an error occurs, an appropriate message will be displayed.

---

## ⚠️ Error Handling

- **NoTranscriptFound**: Transcript not available for the video.  
- **VideoUnavailable**: Video is private, deleted, or otherwise inaccessible.  
- Network issues or invalid video IDs will also be handled gracefully with error messages.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- Submit bug reports or feature requests via [Issues](https://github.com/rabumaabraham/YouTube-Transcript-Downloader/issues) on GitHub.  
- Fork the repo and submit Pull Requests with improvements or fixes.  
- Suggest enhancements or optimizations.

---


## 🙏 Acknowledgements

- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) for providing the core transcript extraction functionality.  
- Thanks to the open-source Python community for making tools like this possible.

---

> Extract, analyze, and utilize YouTube video transcripts effortlessly with **YouTube Transcript Downloader**.
