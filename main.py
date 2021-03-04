import youtube_dl
import re
while True:

    enlace = input("introducir Url del video")
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, enlace) is not None:
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
    else:
        break
