from time import sleep
from threading import Thread

def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {mensagem}')

x = Thread(target=tarefa, args=(5, 'Thread em execução'))
x.start()
print('\nAguardando pela execução da Thread...')
x.join()
print('A execução foi concluída!\n')