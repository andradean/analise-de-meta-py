import pandas as pd
from twilio.rest import Client

account_sid = 'ACdf2b6fb9df3845106cf0a210f913a5a2'
auth_token = '1acb37f5d5f04f5852a52f2e5bc7768f'
client = Client(account_sid, auth_token)

list_months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for month in list_months: 
    sales_table = pd.read_excel(f'{month}.xlsx')
    if (sales_table['Vendas'] > 55000).any(): 
        seller = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendedor'].values[0]
        sales = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendas'].values[0]
        print()
        message = client.messages.create(
            to='+5519986039072',
            from_='+14176474035',
            body=f'Nome mês de {month} o vendedor {seller} bateu a meta, com {sales}R$ em vendas') 
        print(message.sid)  
 
        

