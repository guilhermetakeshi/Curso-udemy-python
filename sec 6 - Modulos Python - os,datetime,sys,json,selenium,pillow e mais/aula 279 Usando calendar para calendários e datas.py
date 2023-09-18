# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# Usando o módulo calendar para imprimir um calendário completo para o ano de 2022
# print(calendar.calendar(2022))

# Usando o módulo calendar para imprimir um calendário específico para o mês de dezembro de 2022
# print(calendar.month(2022, 12))

# Usando o módulo calendar para obter o número do primeiro dia da semana e o último dia do mês de dezembro de 2022
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)

# Usando o módulo calendar para obter uma lista dos nomes dos dias da semana
# e seus números correspondentes (onde 0 é segunda-feira e 6 é domingo)
# nomes_dias_semana = list(enumerate(calendar.day_name))
# print(nomes_dias_semana)

# Usando o módulo calendar para obter o nome do dia da semana correspondente ao primeiro dia do mês de dezembro de 2022
# nome_primeiro_dia = calendar.day_name[numero_primeiro_dia]

# Usando o módulo calendar para obter o nome do dia da semana correspondente ao último dia do mês de dezembro de 2022
# nome_ultimo_dia = calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)]

# Usando o módulo calendar para iterar sobre as semanas do mês de dezembro de 2022 e imprimir os dias do mês
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue  # Ignora os dias que não pertencem ao mês (dias em branco)
        print(day)  # Imprime o dia do mês
