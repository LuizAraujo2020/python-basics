
# Instalação pip install
# pip install pandas
# pip install openpyxl
# pip install twilio

# pip install --upgrade pip

import pandas as pd

# Passo a passo de Solução 

# Abrir os 6 arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)


#  Para cada arquivo:
#     verificar se algum valor na coluna vendas ddaquele arquivo é maior que 55.000

# Se for maior que 55.000 -> enviar SMS com o nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fará nada...