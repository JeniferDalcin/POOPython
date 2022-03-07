from pessoa import Pessoa

p1 = Pessoa('Luiz', 27)
p2 = Pessoa('João', 32)

p1.comer('Pão')

p2.comer('azeitona')
p2.parar_comer()
p2.falar('Poo')
p1.falar('guerra')

print(p1.get_ano_nascimento())
