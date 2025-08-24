import webbrowser
import datetime
import time

# INPUTS
print('Hora de programar o seu alarme!')
data = input('Informe a data do alarme (DD/MM/AAAA): ').split('/')
horario = input('Digite a horário do seu alarme no modelo HH:MM: ').split(':')
video = input('Informe a URL do vídeo desejado: ')

# separando data
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

# separando horário
hora = int(horario[0])
minuto = int(horario[1])

# váriavel de controle para verificar se a mensagem já foi mostrada
mensagem_mostrada = False


"ALARME"
"Transforma o input em uma lista, mudar para int e coloca a primeira parte como hora e a segunda como minuto"
alarme = datetime.datetime(ano,mes,dia,hora,minuto,0)

while True:
    atual = datetime.datetime.now().replace(second=0,microsecond=0)
    diferenca = alarme - atual
    minute = diferenca.total_seconds() / 60
    if atual == alarme:
        webbrowser.open(video)
        break
    elif minute == 1 and not mensagem_mostrada:
        print(f'O seu alarme está programado para às {hora}:{minuto} do dia {dia}/{mes}/{ano}')
        print(f'Aguardando a hora de te acordar com um sorriso')
        mensagem_mostrada = True
    time.sleep(1)