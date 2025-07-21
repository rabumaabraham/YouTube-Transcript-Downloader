YouTube Transcript Downloader

A simple Python script to fetch and save the transcript of a YouTube video using the youtube_transcript_api library.

---

Overview

This project provides a straightforward way to extract the transcript of any YouTube video (if available) by specifying the video ID. The transcript text is saved into a local file (transcript.txt) for easy access, reading, or further processing.

---

Features

- Fetches the transcript of a YouTube video by video ID.
- Saves the transcript as a plain text file (transcript.txt).
- Handles exceptions gracefully and informs the user if an error occurs (e.g., transcript not available).
- Lightweight and easy to use with minimal dependencies.

---

Prerequisites

- Python 3.6 or above installed on your system.
- youtube_transcript_api Python package installed.

Installation

You can install the required package using pip:

pip install youtube-transcript-api

---

Usage

1. Clone or download this repository.

2. Open the script and replace the video_id variable with the ID of the YouTube video you want the transcript for. For example:

video_id = 'EjxL2oB7J-o'

3. Run the script:

python your_script_name.py

4. If the transcript is available, it will be saved to a file named transcript.txt in the same directory.

---

Example

For the video with ID EjxL2oB7J-o, running the script will generate a transcript.txt file with the full transcript text extracted from the video.

---

Error Handling

- If a transcript is not available for the specified video, or the video ID is invalid, the script will catch the error and print an appropriate message.
- Common errors include:
  - NoTranscriptFound: No transcript available for the video.
  - VideoUnavailable: Video is private or removed.
  - Network or connection errors.

---

Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page on GitHub.

---

License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Acknowledgments

- This script utilizes the open-source youtube-transcript-api developed by jdepoix.
- Thanks to the YouTube community for making transcripts available on many videos.

---

Contact

For any questions or support, please open an issue or contact me at your-email@example.com.

---

Happy Transcribing! 🎥📝
