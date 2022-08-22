from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress #this module contains the built in progress bar. 
print("Enter youtuve url:")

itag = 22 # to get 720p
pl = input()
# i = Playlist("https://www.youtube.com/playlist?list=PL6gx4Cwl9DGCkg2uj3PxUWhMDuTw3VKjM")
i = Playlist(pl)

#yt = YouTube(i,on_progress_callback=on_progress)

#print( 'Video Title :',title,'\n')
#print( 'ThumbnailUrl:',yt.thumbnail_url)
print("Total of videos:",len(i.video_urls))
line = 0
for url in i.video_urls:
    line += 1
    #print("\n",line,url)
    yt = YouTube(url,on_progress_callback=on_progress)
    print("Current video:",yt.title)
    
    strm = yt.streams.get_by_itag(itag)
    print("Downlod (Video 720p) url:",strm.url,"\n")
    #strm.download()