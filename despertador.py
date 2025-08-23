import webbrowser
import datetime
import time
"INPUTS"
print('Hora de programar o seu alarme!')
horario = input('Digite a horário do seu alarme no modelo HH:MM: ').split(':')
video = input('Informe a URL do vídeo desejado: ')
hora = int(horario[0])
minuto = int(horario[1])
"ALARME"
"Transforma o input em uma lista, mudar para int e coloca a primeira parte como hora e a segunda como minuto"
alarme = datetime.time(hora,minuto,0)
while True:
    atual = datetime.datetime.now().time().replace(second=0,microsecond=0)
    if atual == alarme:
        webbrowser.open(video)
        break
    else:
        time.sleep(1800)
        print(f'O seu alarme está programado para às {horario}')
        time.sleep(1800)
        print(f'Aguardando a hora de te acordar com um sorriso')
    time.sleep(1)