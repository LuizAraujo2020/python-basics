
# Instalação pip install
# pip install pandas
# pip install openpyxl
# pip install twilio

# pip install --upgrade pip

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC620e412b2361fe740a3d7a7c6774b700"
# Your Auth Token from twilio.com/console
auth_token = "fee7e510b15f23c68ba40c2612a87698"
client = Client(account_sid, auth_token) #conecta


# Abrir os 6 arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.')
        sms = f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.'
        message = client.messages.create(
            to="+5561983737860",
            from_="+12156081242",
            body=sms
        )
        print(message.sid)

#  Para cada arquivo:
#     verificar se algum valor na coluna vendas ddaquele arquivo é maior que 55.000

# Se for maior que 55.000 -> enviar SMS com o nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fará nada...




