class Argentina():
    def capital(self):
        print('Buenos Aires é a capital da Argentina.')
    def lingua_oficial(self):
        print('O espanhol é a língua oficial da Argentina.')
    
class Brasil():
    def capital(self):
        print('Brasília é a capital do Brasil.')
    def lingua_oficial(self):
        print('O português é a língua oficial do Brasil.')
        
obj_arg = Argentina()
obj_bra = Brasil()
print()
print('=' * 50)
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()
print('=' * 50, '\n')