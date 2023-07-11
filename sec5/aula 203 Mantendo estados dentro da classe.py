# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando is True:
            print(f'{self.nome} JÁ está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True 
        # o estado do filmando TRUE faz com q o sistema guarde essa informação
        # e se já estiver filmando, é necessário que avise, ent colocaremos um if antes
        
    # vamos supor que a camera não tire foto enquanto está filmando, ent vamos colocar uma condição
    
    def fotografar(self):
        if self.filmando is True:
            print(f'{self.nome} Não é possível fotografar pois está filmando...')
            return
        
        print(f'{self.nome} está fotografando...')
        
    def parar_de_filmar(self):
        if self.filmando is not True:
            print(f'{self.nome} NÃO está filmando...')
            return
        
        print(f'{self.nome} está PARANDO de filmar...')
        self.filmando = False


cannon = Camera('Cannon')
sony = Camera('Sony')

cannon.filmar()
cannon.filmar()
cannon.fotografar()
cannon.parar_de_filmar()
cannon.fotografar()

print()

sony.parar_de_filmar()
sony.filmar()
sony.filmar()
sony.fotografar()
sony.parar_de_filmar()
sony.fotografar()
