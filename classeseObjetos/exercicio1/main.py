# 1. Crie uma classe que modele o objeto "carro".
# 2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# 4. Crie uma instância da classe carro.
# 5. Faça o carro "andar" utilizando os métodos da sua classe.
# 6. Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = "preto"
        self.modelo = "gol"
        self.velocidade = 0
        self.velocidade_max = 220
        self.velocidade_min = 0


    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 100

    def desacelerar(self):
        if not self.ligado:
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= 50

# Criando um carro
carro = Carro()

def ligar():
    global carro
    carro.ligar()
    print(f'O carro está: {carro.ligado}')
    while carro.velocidade < carro.velocidade_max: 
        carro.acelerar()
        print(f'O carro foi acelerado: {carro.velocidade:.1f}')
    
    
def desligar():
    global carro
    while carro.velocidade > carro.velocidade_min: 
        carro.desacelerar()
        print(f'O carro foi desacelerado: {carro.velocidade:.1f}')

    carro.desligar()
    print(f'O carro está: {carro.ligado}')

ligar()
desligar()
