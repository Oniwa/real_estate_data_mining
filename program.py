import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('------------------------------------')
    print('    REAL ESTATE DATA MINING APP')
    print('------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):  # : list[Purchase])
    # if data was sorted by price:
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print(f'The most expensive house is ${high_purchase.price:,} with '
          f'{high_purchase.beds} beds and {high_purchase.baths} baths')

    # least expensive house?
    low_purchase = data[0]
    print(f'The least expensive house is ${low_purchase.price:,} with '
          f'{low_purchase.beds} beds and {low_purchase.baths} baths')

    # average price house?
    prices = [
        p.price for p in data
    ]

    avg_price = statistics.mean(prices)
    print(f"The average home price is ${int(avg_price):,}")

    # average price of 2 bedroom houses?
    two_bedroom_homes = (
        p for p in data if announce(p, f'2-bedrroms, found {p.beds}') and p.beds == 2
    )

    homes = []
    for h in two_bedroom_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    avg_sq = statistics.mean((p.sq__ft for p in homes))
    print(f"The average price of a 2-bedroomn home is ${int(avg_price)}, "
          f"baths={avg_baths}, sq ft={int(avg_sq)}")


def announce(item, msg):
    print(f"Pulling item {item} for {msg}")
    return item


if __name__ == '__main__':
    main()
