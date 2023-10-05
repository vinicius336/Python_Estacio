from threading import Thread
from time import sleep

def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da tarefa {nome_tarefa}')

t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))
t1.start()
t2.start()
t1.join()   #   Esperar até completar a execução da thread 1
t2.join()   #   Esperar até completar a execução da thread 2
print('A execição foi concluída!')