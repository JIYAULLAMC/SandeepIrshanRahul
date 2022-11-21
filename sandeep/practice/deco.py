import os

# folder path
dir_path = r'D:\TUTORIAL_VIDEO(do not delete)\django_geeky_shows_videos'

# list file and directories
fiename = ""
res = os.listdir(dir_path)
for index, file in enumerate(res):
    print(index, file)