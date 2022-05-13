'''
pip install moviepy
'''

import moviepy.editor as m

demo_video = m.VideoFileClip("/Linkedin PDC Programs\\assets\\kaka.mp4")
demo_video.audio.write_audiofile("videotoaudio.mp3")
