from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=aKrHPhrqoZw')
print(yt.title)
stream = yt.streams.first()
stream.download()