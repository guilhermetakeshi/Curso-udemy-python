# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores

# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Tem que ser um caso onde se chame de volta (recursividade)
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

# Stack Overflow acontece quando o call Stack fica cheio de tarefas a serem executadas, onde
# o sistema quebra como forma de segurança para não acumular mta coisa

def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())
