# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Definir o valor do empréstimo e a data de início
valor_emprestimo = 1_000_000  # Valor do empréstimo em reais (R$ 1.000.000)
data_inicio_emprestimo = datetime(2020, 12, 20)  # Data de início do empréstimo

# Calcular a data de término do empréstimo (5 anos após o início)
prazo_emprestimo_anos = 5
data_final_emprestimo = data_inicio_emprestimo + relativedelta(years=prazo_emprestimo_anos)

# Inicializar uma lista para armazenar as datas de vencimento das parcelas
datas_de_vencimento = []
data_vencimento_atual = data_inicio_emprestimo

# Calcular as datas de vencimento das parcelas mensais
while data_vencimento_atual < data_final_emprestimo:
    datas_de_vencimento.append(data_vencimento_atual)
    data_vencimento_atual += relativedelta(months=+1)

# Calcular o número de parcelas e o valor de cada parcela
numero_parcelas = len(datas_de_vencimento)
valor_parcela = valor_emprestimo / numero_parcelas

# Exibir as datas de vencimento e o valor de cada parcela
print("Datas de Vencimento e Valores das Parcelas:")
for data in datas_de_vencimento:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# Exibir informações gerais sobre o empréstimo
print()
print(
    f'Você pegou R$ {valor_emprestimo:,.2f} para pagar '
    f'em {prazo_emprestimo_anos} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)
