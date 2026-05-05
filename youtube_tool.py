from youtube_transcript_api import YouTubeTranscriptApi
from crewai.tools import tool

def extract_video_id(url: str):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")

@tool("YouTube Transcript Fetcher")
def get_transcript(url: str) -> str:
    """
    Fetch the transcript of a YouTube video using the video URL.
    Returns the full transcript as a single string.
    """
    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    full_text = " ".join([t.text for t in transcript])
    return full_text
