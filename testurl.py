import urllib.request
import re

words = "the feels twice".split()

searchlink = "http://www.youtube.com/results?search_query=" + '+'.join(words)
html = urllib.request.urlopen(searchlink)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])