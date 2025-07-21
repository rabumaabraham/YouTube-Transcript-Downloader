from youtube_transcript_api import YouTubeTranscriptApi

# ✅ CORRECT: Just the video ID, not the whole URL
video_id = 'EjxL2oB7J-o'

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    with open("transcript.txt", "w", encoding="utf-8") as file:
        for entry in transcript:
            file.write(entry['text'] + '\n')
    
    print("Transcript saved to transcript.txt")
except Exception as e:
    print("Error:", e)
