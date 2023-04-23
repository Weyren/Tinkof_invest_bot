import data
from tinkoff.invest import Client
from tinkoff.invest.constants import INVEST_GRPC_API
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

import quotes_collection


def main():
    with Client(data.token_read_only) as client:
        quotes_collection.shares()


if __name__ == '__main__':
    main()

