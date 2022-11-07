import os

def ex_1(video_file):

    # Guardem el que se'ns mostra a un fitxer de text
    os.system('ffmpeg -i '+str(video_file)+'.mp4 2> info.txt')

    # Obrir el fitxer de text previament guardat i n'agafem les línies
    with open('info.txt') as fragment:
        information = fragment.readlines()

    # De cada línia, busquem la paraula desitjada per tal que surtin 3 conceptes rellevants del container
    for conc in information:
        if conc.__contains__("Video"):
            print(conc)

# Cridem a la funció amb el BBB video
ex_1("bbbVideo")