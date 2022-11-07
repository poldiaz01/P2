import os

def ex_3(video_file):

    # Demanem a l'usuari les dimensions que ens interessen
    X = int(input('Dimensió amplada: '))
    Y = int(input('Dimensió alçada: '))

    # Si les dimensions no són múltiples de dos, tornem a demanar a l'usuari les dimensions
    while X % 2 != 0 or Y % 2 != 0:
        print("Les dimensions han de ser divisibles per 2. Torna-hi")
        X = int(input('Dimensió amplada: '))
        Y = int(input('Dimensió alçada: '))

    # Un cop les dimensions ja són múltiples de 2, ja podem obtenir el video resized
    os.system("ffmpeg -i "+str(video_file)+".mp4 -vf scale=" + str(X) + ":" + str(Y) + " ex_3_resized.mp4")

# Cridem a la funció amb el BBB video
ex_3("bbbVIdeo")







