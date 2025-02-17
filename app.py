import yt_dlp

link = ""

yt_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(yt_opts) as ydl:  # Corrigido aqui
    ydl.download([link])
