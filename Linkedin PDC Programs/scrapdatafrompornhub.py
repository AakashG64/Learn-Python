'''
pip install phlib
'''

from phlib import PornHub, Category, Video

ph = PornHub()

print(ph.categories)
print(ph["example category"])
# cat = Category

# cat.videos(max=25)
# ph.search("some search term")
# video = Video
# video.download(block=True)

for video in ph['college'].videos(max=25):
    print(video.__dict__)
    video.download(block=True)