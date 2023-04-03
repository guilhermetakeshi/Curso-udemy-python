# exercicio para validar CPF

import sys

cpf_usuario = str(input('Digite o CPF: ')).replace('.', '').replace('-', '').replace(' ', '')
#usado o replace para substituir os pontos, traços e espaços por nada, afim de n haver erros
#cpf_usuario = '42768642835' 
nove_digitos = cpf_usuario[:9]
cont_regressivo_1 = 10
cont_regressivo_2 = 11
soma_multidigitos_1 = 0
soma_multidigitos_2 = 0

#ate aqui declarei algumas variaveis

entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

for digito_1 in nove_digitos:
    soma_multidigitos_1 += (int(digito_1)*cont_regressivo_1)
    cont_regressivo_1 -= 1 # for para a variavel digito_1 passar pelos digitos

resto_1 = (soma_multidigitos_1 * 10) % 11
resto_1 = 0 if resto_1 > 9 else resto_1

print('O Primeiro dígito do CPF é: {}'.format(resto_1))

dez_digitos = nove_digitos + str(resto_1)

for digito_2 in dez_digitos:
    soma_multidigitos_2 += int(digito_2)*cont_regressivo_2
    cont_regressivo_2 -= 1

resto_2 = (soma_multidigitos_2 * 10) % 11
resto_2 = resto_2 if resto_2 <=9 else 0

print('O Segundo dígito é: {}'.format(resto_2))

cpf_gerado_pelo_calculo = f'{nove_digitos}{resto_1}{resto_2}'

if cpf_usuario == cpf_gerado_pelo_calculo:
    print('O CPF é válido')
else:
    print('O CPF é INVÁLIDO')

