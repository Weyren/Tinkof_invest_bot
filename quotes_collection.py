import data
import datetime
from tinkoff.invest import Client
#from tinkoff.invest import InfoInstrument
import time
import ta
#from main.

def shares():   #zabor kotirovok
    with Client(data.token_read_only) as client:
        # a = client.users.get_accounts().accounts
        # print(a)
        # b = client.operations.get_operations(
        #     account_id=data.account_id_read_only,
        #     from_ = datetime.datetime(2020, 1, 1),
        #     to= datetime.datetime.now()
        #     )
        # print(b)

        # c = client.instruments.bonds().instruments
        # print(c[0])
        #
        # d = client.instruments.bond_by(class_code='TQCB')
        # print(d)
        # b = client.operations.get_portfolio(account_id='2001914084')
        # print(b)
        # #[print(l) for l in b]
        a = client.instruments.shares().instruments
        for i in range(0, len(a)):




    return 0
