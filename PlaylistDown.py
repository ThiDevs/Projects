from pytube import Playlist
from pytube import YouTube
from threading import Thread


def main():
    pl = Playlist('https://www.youtube.com/playlist?list=PL95lHvAv3fEkldbLqR0Ur9EX5JmmtrBfr')
    i = 0
    for item in pl.parse_links():
        print('youtube.com' + item)
        youtube = YouTube('youtube.com' + item)
        #print(youtube.title)
        #print(youtube.thumbnail_url)
        #a = Th(youtube)
        i+= 1
        print(i)
       # a.start()


class Th(Thread):

    def __init__(self, youtube):
        Thread.__init__(self)
        self.youtube = youtube

    def run(self):
        print("Hello ")
        self.youtube.streams.first().download("C:\\Users\\Thiago\\Desktop\\Playlist")

main()