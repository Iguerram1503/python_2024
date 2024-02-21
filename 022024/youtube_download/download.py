from pytube import YouTube

url = 'https://www.youtube.com/watch?v=nCkpzqqog4k'

youtube = YouTube(url)

stream = youtube.streams.get_highest_resolution()

download_path = '/c/Developments/COURSE_2401/python_2024/022024'
file_name = "I'm not the only one.mp4"
stream.download()

