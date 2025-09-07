# 🎥 yt-batch-downloader

A Python script that automates downloading YouTube playlists and videos in **best quality** using [yt-dlp](https://github.com/yt-dlp/yt-dlp).  
Each playlist is saved in a **separate folder**, keeping downloads clean and organized.

---

## 🚀 Features
- Download **entire playlists** or single videos.
- Automatically creates a **folder per playlist**.
- Always downloads the **best video + best audio**, then merges them into a single `.mp4`.
- Handles **timeouts and retries** gracefully.
- Works on **Windows, Linux, and macOS**.

---

## 📦 Requirements

Make sure you have installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
  Install via pip:
  ```bash
  pip install yt-dlp
