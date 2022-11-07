import os

def ex_4(video_file):

    # Mostrem per pantalla tots els àudios que té el video entrat
    os.system("ffprobe -i "+str(video_file)+".mp4 2>&1 | grep 'Stream.*Audio'")

    # Guardem el que se'ns mostra a un fitxer de text
    os.system('ffmpeg -i ' + str(video_file) + '.mp4 2> info_ex4.txt')

    # Analitzem el fitxer de text
    with open('info.txt') as fragment:
        information = fragment.readlines()

    # Llegim cada línia i busquem el tipus d'àudio
    for audio in information:

        #Depenent de l'àudio, decidirem quin broadcasting standard hi adjudicarem
        if audio.__contains__("aac"):
            print("The ISDB or DTMB broadcasting standrards are the ones that can fit better with the aac audio")

        elif audio.__contains__("ac3"):
            print("The ATSC or DTMB broadcasting standrards are the ones that can fit better with the ac3 audio")

        elif audio.__contains__("dra"):
            print("The broadcasting standard that better fits is the DTMB with the dra audio")

# Cridem a la funció amb el BBB video
ex_4("bbbVideo")