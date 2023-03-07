from random import choice


def dicionario_ppt(x):
    dict_pedra_papel_tesoura = {'r': 'Pedra',
                                'p': 'Papel',
                                't': 'Tesoura'}
    return dict_pedra_papel_tesoura[x]


def jogar():
    usuario = str(input("""
    Escolha um para jogar: 
    [R] - Pedra
    [P] - Papel
    [T] - Tesoura
    --> """)).strip().lower()
    computador = choice(['r', 'p', 't'])

    print(f"""
Computador |  Usuario
{dicionario_ppt(computador)}\t   X  {dicionario_ppt(usuario)}""")

    if usuario == computador:
        return '\033[1;33;40m Empate \033[m'
    if vitoria(usuario, computador):
        return "\033[1;32;40m Usuario Ganhou \033[m"

    return "\033[1;31;40m Computador Ganhou \033[m"


def vitoria(jogador, adversario):
    if (jogador == 'r' and adversario == 't') or (jogador == 't' and adversario == 'p') \
            or (jogador == 'p' and adversario == 'r'):
        return True


print(jogar())