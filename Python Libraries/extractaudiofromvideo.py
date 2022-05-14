'''
pip install moviepy
'''

import moviepy.editor as m

demo_video = m.VideoFileClip("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Python\\assets\\kaka.mp4")
demo_video.audio.write_audiofile("videotoaudio.mp3")
