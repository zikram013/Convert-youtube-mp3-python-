import youtube_dl

enlace = input("introducir Url del video")

video = youtube_dl.YoutubeDL().extract_info(url=enlace, download=False)
tituloVideo = video["title"]

opciones = {
    "format": "bestaudio/best",
    "outtmpl": f"E:/{tituloVideo}.mp3",
    "postprocesosors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
    }],
}

with youtube_dl.YoutubeDL(opciones)as ydl:
    ydl.download([enlace])
