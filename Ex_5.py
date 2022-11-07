import os

class ex_5:

    #Inicialitzem els outputs de cada exercici
    #Dels exercicis 1 i 4 no n'inicialitzem cap perquè el resultat es mostra per la terminal
    def __init__(self,ex2_output,ex3_output,video_file):
        self.ex2_output = ex2_output
        self.ex3_output = ex3_output
        self.video_file = video_file

    #Demanem a l'usuari l'exercici que vol dur a terme
        ex = int(input("Introdueix el número de l'exercici (1,2,3 o 4) : "))

    #Per a cada exercici, cridem a la funció corresponent
        if ex == 1:
            self.ex_1()
        elif ex == 2:
            self.ex_2()
        elif ex == 3:
            self.ex_3()
        elif ex == 4:
            self.ex_4()

    #Redefinim les funcions prèviament creades per tal de poder-les utilitzar a la classe

    # EXERCICI 1
    def ex_1(self):

        # Guardem el que se'ns mostra a un fitxer de text
        os.system('ffmpeg -i ' + str(self.video_file) + '.mp4 2> info.txt')

        # Analitzem el fitxer de text i busquem els conceptes rellevants
        with open('info.txt') as fragment:
            information = fragment.readlines()

        for conc in information:
            if conc.__contains__("Video"):
                print(conc)

    # EXERCICI 2
    def ex_2(self):

        # Tallem el video 1 minut
        os.system("ffmpeg -i" + str(self.video_file) + ".mp4 -ss 0 -t 60 -c:v copy -c:a copy ex_1.mp4")

        # Extreiem l'audio del video en mp3
        os.system("ffmpeg -i ex_1.mp4 ex_1_mp3.mp3")

        # Extreiem l'audio del video en aac
        os.system("ffmpeg -i ex_1.mp4 -acodec aac -ab 115k -vcodec copy ex_2_aac.aac")

        # Generem el nou container
        os.system("ffmpeg -i ex_1_mp3.mp3 -i ex_2_aac.aac -c:v copy " + str(self.ex2_output) + ".mp4")

    # EXERCICI3

    def ex_3(self):

        # Demanem a l'usuari les dimensions que ens interessen
        X = int(input('Dimensió amplada: '))
        Y = int(input('Dimensió alçada: '))

        # Si les dimensions no són múltiples de dos, tornem a demanar a l'usuari les dimensions
        while X % 2 != 0 or Y % 2 != 0:
            print("Les dimensions han de ser divisibles per 2. Torna-hi")
            X = int(input('Dimensió amplada: '))
            Y = int(input('Dimensió alçada: '))

        # Un cop les dimensions ja són múltiples de 2, ja podem obtenir el video resized
        os.system("ffmpeg -i " + str(self.video_file) + ".mp4 -vf scale=" + str(X) + ":" + str(Y) + " " + str(
            self.ex3_output) + ".mp4")


    # EXERCICI 4

    def ex_4(self):

        # Mostrem per pantalla tots els àudios que té el video entrat
        os.system("ffprobe -i " + str(self.video_file) + ".mp4 2>&1 | grep 'Stream.*Audio'")

        # Guardem el que se'ns mostra a un fitxer de text
        os.system('ffmpeg -i ' + str(self.video_file) + '.mp4 2> info_ex4.txt')

        # Analitzem el fitxer de text
        with open('info.txt') as fragment:
            information = fragment.readlines()

        # Llegim cada línia i busquem el tipus d'àudio
        for audio in information:

            # Depenent de l'àudio, decidirem quin broadcasting standard hi adjudicarem
            if audio.__contains__("aac"):
                print("The ISDB or DTMB broadcasting standrards are the ones that can fit better with the aac audio")

            elif audio.__contains__("ac3"):
                print("The ATSC or DTMB broadcasting standrards are the ones that can fit better with the ac3 audio")

            elif audio.__contains__("dra"):
                print("The broadcasting standard that better fits is the DTMB with the dra audio")


# Generem una instància de la classe creada per tal de poder-la executar
ex_5 = ex_5("ex_2_output", "ex_3_output", "bbbVideo")




