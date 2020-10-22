import matplotlib.pyplot as plt

Mes = list()
Vendas = list()
Temp_Mes_e_Valor = list()
Mes_e_Valor = list()

Mes_Completo = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                'Outubro', 'Novembro', 'Dezembro']
Mes_Abreviado = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']


def Numero_Mes(Mes):
    
    if Mes == 'Jan':
        Numero_M = 1

    if Mes == 'Fev':
        Numero_M = 2

    if Mes == 'Mar':
        Numero_M = 3

    if Mes == 'Abr':
        Numero_M = 4

    if Mes == 'Mai':
        Numero_M = 5

    if Mes == 'Jun':
        Numero_M = 6

    if Mes == 'Jul':
        Numero_M = 7

    if Mes == 'Ago':
        Numero_M = 8

    if Mes == 'Set':
        Numero_M = 9

    if Mes == 'Out':
        Numero_M = 10

    if Mes == 'Nov':
        Numero_M = 11

    if Mes == 'Dez':
        Numero_M = 12

    return Numero_M


Começar = str(input('Digite o Mês Que Quer Começar (Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez): ')).title()
while Começar not in Mes_Abreviado:
    Começar = str(input(
        'Erro Na Digitação. Digite o Mês Que Quer Começar (Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez): ')).title()

Mes_Dos_Valores = Maior_Valor = Menor_Valor = 0
Mes_Copia = Copia_Mes_Contagem = Numero_Mes(Começar)

print('=-' * 30)
while True:
    if Mes_Copia >= 12:
        Mes_Copia = 0
        Copia_Mes_Contagem = 0

    Valor_Das_Vendas = str(
        input(f'Valor das vendas foi feitas no mês de {Mes_Completo[Mes_Copia - 1]}: R$')).strip().replace(',', '.')
    Temp_Mes_e_Valor.append(Mes_Completo[Mes_Copia - 1])

    try:
        Valor_Das_Vendas = float(Valor_Das_Vendas)

        Vendas.append(Valor_Das_Vendas)  # VALORES no GRAFICO
        Temp_Mes_e_Valor.append(Valor_Das_Vendas)  # ESSE É DO MAIOR E MENOR

        continuar = str(input('Continuar (S/N): ')).upper().strip()
        while continuar != 'S' and continuar != 'N':
            continuar = str(input('Continuar (S/N): ')).upper().strip()

        Mes_Copia = str(Mes_Copia)
        Mes_Copia = Mes_Copia.replace(Mes_Copia, Mes_Abreviado[Copia_Mes_Contagem - 1])
        Mes.append(Mes_Copia)  # MES

        Mes_Copia = int(Copia_Mes_Contagem)
        Copia_Mes_Contagem += 1
        Mes_Copia += 1
        Mes_Dos_Valores += 1
        if len(Mes_e_Valor) == 0:
            Menor_Valor = Maior_Valor = Temp_Mes_e_Valor[1]
        else:
            if Temp_Mes_e_Valor[1] > Maior_Valor:
                Maior_Valor = Temp_Mes_e_Valor[1]  # Maior Valor
            if Temp_Mes_e_Valor[1] < Menor_Valor:
                Menor_Valor = Temp_Mes_e_Valor[1]  # Menor Valor
        Mes_e_Valor.append(Temp_Mes_e_Valor[:])
        Temp_Mes_e_Valor.clear()

        if continuar == 'N':
            break

    except:
        print('Algo deu errado, corrija por favor!')
        Temp_Mes_e_Valor.clear()

print('=-' * 24)
print(f'Melhor Venda:\t---> R${max(Vendas)} no Mês de ', end='')
for Maior in Mes_e_Valor:
    if Maior[1] == Maior_Valor:
        print(f'[{Maior[0]}] ', end='')
print()

print(f'Menor  Venda:\t---> R${min(Vendas)} no Mês de ', end='')
for Menor in Mes_e_Valor:
    if Menor[1] == Menor_Valor:
        print(f'[{Menor[0]}] ', end='')
print()

print(f'A soma de todos os valores dos {Mes_Dos_Valores} meses é R${sum(Vendas)}\nCarregando gráfico...')

plt.title('Gráfico Das Vendas', color='blue')
plt.xlabel('Mês Das Vendas', color='black')
plt.ylabel('Valor Das Vendas', color='black')
plt.grid(True)

plt.scatter(Mes, Vendas, color='red')
plt.plot(Mes, Vendas, color='black')

plt.show()
print('=-' * 30)
