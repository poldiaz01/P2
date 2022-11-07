import os

def ex_2(video_file):

    # Tallem el video 1 minut
    os.system("ffmpeg -i"+str(video_file)+".mp4 -ss 0 -t 60 -c:v copy -c:a copy ex_1.mp4")

    # Extreiem l'audio del video en mp3
    os.system("ffmpeg -i ex_1.mp4 ex_1_mp3.mp3")

    # Extreiem l'audio del video en aac
    os.system("ffmpeg -i ex_1.mp4 -acodec aac -ab 115k -vcodec copy ex_2_aac.aac")

    # Generem el nou container
    os.system("ffmpeg -i ex_1_mp3.mp3 -i ex_2_aac.aac -c:v copy newContainer_ex2.mp4")

# Cridem la funció amb el BBB video
ex_2("bbbVideo")