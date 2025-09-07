import yt_dlp

# List of all playlists and single videos
URLS = [
 "https://www.youtube.com/watch?v=VIDEO_ID",
    "https://www.youtube.com/playlist?list=PLAYLIST_ID"
]

# Download options
ydl_opts = {
    # Best video + best audio (highest quality)
    "format": "bestvideo+bestaudio/best",

    # Merge into MP4 (requires ffmpeg)
    "merge_output_format": "mp4",

    # Networking / retries
    "socket_timeout": 60,
    "retries": 10,
    "fragment_retries": 10,
    "continuedl": True,  # resume broken downloads

    # Save files into separate folders
    "outtmpl": "%(playlist_title|Single_Videos)s/%(title)s.%(ext)s",

    # Progress bar in terminal
    "progress_hooks": [lambda d: print(f"[{d['status']}] {d.get('filename','')}")],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
