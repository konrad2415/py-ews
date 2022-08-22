from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress #this module contains the built in progress bar. 

# Progressbar color variable
#fuchsia = '\033[38;2;255;00;255m'   #  color as hex #FF00FF
#reset_color = '\033[39m'


print("Enter youtuve url:")
i = input()
#i = "www.youtube.com/watch?v=31crA53Dgu0"

print(f'URL:{i}')
yt = YouTube(i,on_progress_callback=on_progress)

title = yt.title+".mp4"
#print(fuchsia + 'Video Title :',title,'\n')
print( 'Video Title :',title,'\n')
print(yt.thumbnail_url)

# Get downloadable video+audio listing

# this line shows itag and stream values Corresponding to downloadable videos 
video = yt.streams.filter(progressive=True)
audio = yt.streams.filter(only_audio=True, abr="128kbps")

print(f"Video with audio streaming file:\n")
for mp4 in video:
    print(mp4)

print(f"\n\nAudio only streaming file:\n")
for mp3 in audio:
    print(mp3)
print(f"\n")
# progressive property shows video+audio and resolution prop limits the list to desired resolution
filter360 = yt.streams.filter(progressive=True,resolution="360p") # for 360p resolution

filter720 = yt.streams.filter(progressive=True,resolution="720p") # for 720p resolution

# list 720p resolution downloadable video + audio  
#for mp4 in filter760:
#    print(mp4)

# Resolution desired by itag
# itag 17  - to 140p
# itag 18  - to 360p
# itag 22  - to 720p
# itag 140 - to only-audio 

itag = 22 # to get 720p

strm = yt.streams.get_by_itag(22)
print("Downlod (Video 720p) url:",strm.url,"\n")

#strm = yt.streams.get_by_itag(140)
#print("Downlod (OnlyAudio) url:",strm.url,"\n" + reset_color)
strm.download()
