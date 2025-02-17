import random

def gerar_cpf(): #função para gerar cpfs
    return "".join([str(random.randint(0,9)) for _ in range(9)])

def gerar_subconjunto(conjunto,tamanho_min=10,tamanho_max=50): #funçao para gerar subconjuntos de tamanho aleatorio
    tamanho= random.randint(tamanho_min, min(tamanho_max, len(conjunto)))
    return set(random.sample(list(conjunto), tamanho))

cpfs = set()
while len(cpfs) <= 100:
    cpfs.add(gerar_cpf())

modalidades = ['Vôlei de praia','Ginástica','Surfe','Judô']
subconjunto = {modalidade: gerar_subconjunto(cpfs) for modalidade in modalidades}

total_cpf= len(cpfs)

def calcular_probabilidade(): #Função para calcular as probabilades
    judo_ou_surfe = subconjunto['Judô'].union(subconjunto['Surfe'])
    probabilidade_a = len(judo_ou_surfe) / total_cpf

    pelo_menos_duas_modalidades = set()
    for cpf in cpfs:
        cont = sum(cpf in subconjunto[modalidade] for modalidade in modalidades)
        if cont >= 2:  
            pelo_menos_duas_modalidades.add(cpf)
    probabilidade_b = len(pelo_menos_duas_modalidades) / total_cpf

    todas_modalidades = set.intersection(*subconjunto.values())
    probabilidade_c = len(todas_modalidades) / total_cpf

    nenhuma_modalidade = cpfs.difference(set.union(*subconjunto.values()))
    probabilidade_d = len(nenhuma_modalidade) / total_cpf

    return probabilidade_a, probabilidade_b, probabilidade_c, probabilidade_d

probabilidade_a, probabilidade_b, probabilidade_c, probabilidade_d = calcular_probabilidade()

print(f"A) Judô ou Surfe: {probabilidade_a:.2%}")
print(f"B) Pelo menos dois esportes: {probabilidade_b:.2%}")
print(f"C) Todos os esportes: {probabilidade_c:.2%}")
print(f"D) Nenhum esporte: {probabilidade_d:.2%}")
