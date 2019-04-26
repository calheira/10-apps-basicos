"""
Aplicativos Simples para Aprender Python
App 03
Calcula tempo até o aniversário
Conceitos: funcoes, datas, python-em-pt-br
Autor: Bruno Calheira
"""
import datetime

def abertura():
    print("-"*20)
    print("(^-^) Calcula Niver")
    print("-"*20)
    print()


def recebe_niver():
    print("Quando você nasceu?")
    ano = int(input("Ano [AAAA]: "))
    mes = int(input("Mes [MM]: "))
    dia = int(input("Dia [DD]: "))

    niver = datetime.date(ano, mes, dia)
    return niver


def calcula_dias_ate_hoje(data_inicial, data_atual):
    niver_este_ano = datetime.date(data_atual.year, data_inicial.month, data_inicial.day)
    dias = niver_este_ano - data_atual
    return dias.days

def mostra_resultado(dias):
    if (dias < 0):
        dias = -dias
        print(f"O seu aniversário foi há {dias} dia(s) atrás.\nMeus parabéns atrasados!")
    elif (dias == 0):
        print(f"O seu aniversário é hoje!\nParabéns!")
    else:
        print(f"Faltam {dias} para o seu aniversário.\nJá pensou como vai comemorar?")


def main():
    abertura()
    niver = recebe_niver()
    hoje = datetime.date.today()
    dias = calcula_dias_ate_hoje(niver, hoje)
    mostra_resultado(dias)

main()
