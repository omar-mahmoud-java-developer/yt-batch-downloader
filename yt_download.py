import yt_dlp

# List of all playlists and single videos
URLS = [
    "https://youtube.com/playlist?list=PL69159617CC4D4BCA&si=UAm1fDkIcLjZ6lwp",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhyS7_hi2I5D7CH2sACsPjFW&si=bhcitnMJOOSmOkHh",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhypDcfYdsiIJb1Z9ShSIGvy&si=dK7nQjo3SNpgMBJX",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhxGApYMDH9g5uEMvZPMtDRk&si=rWJg3A37nhIqlqoy",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhydGVYxMEJr9FyTr9WhbG6q&si=qtOeF5BGen4zz2j7",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhyWsdIHT6DKzwzDA6_mkrjb&si=qCLyNetpXVth0oRc",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhwHfjJYNuktH7qKZse2JPpf&si=w-bpEEOT5JXRSZLN",
    "https://youtube.com/playlist?list=PLSUcSqxe9RhzbP2F4xTE9GCrIUUEuFJoa&si=FgjKMvo3JSWizOxS",
    "https://youtube.com/playlist?list=PL8qNfNNjw6adY3X8jUz2zEmSk5s4ELIAR&si=nczO664AlCbnJQZh",
    "https://youtu.be/f0AHyAhNulc?si=zgiDa39OszDA8QvN",
    "https://youtu.be/63_AOCldyXo?si=nFzvLn34d_rX3GwU",
    "https://youtu.be/Pfj4niPP0DY?si=BHX2V_kQFrkhwUml",
    "https://youtu.be/s6wq5Rz3qzM?si=_1-PjLr04UM1JQ7j",
    "https://youtu.be/UGhyuKbIgG4?si=zeubpRfFRSCkN-bl",
    "https://youtu.be/zpyyPw54i4E?si=43kLJ25zkU2qAohm",
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
