# given youtube playlist url, get all the urls of the videos
import sys
import openpyxl

from pytube import Playlist


def get_urls(url):
    try:
        playlist = Playlist(url)
        urls_dict = {}
        for video in playlist.videos:
            urls_dict[video.title] = video.watch_url
            print("{} : {}".format(video.title, video.watch_url))
        print(urls_dict)
        return urls_dict
    except:
        print("Error: Invalid Playlist URL")
        sys.exit(1)

playlist_url = input("Enter playlist url: ")
urls_dict = get_urls(playlist_url)

# save dictionary to excel file

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Title", "URL"])
ws.append(["", ""])
for key, value in urls_dict.items():
    ws.append([key, value])

wb.save("playlist_urls.xlsx")
