import requests
from config import api, url
from wallets import wallets

def get_tx(wallet, api, url):
    url = (f"{url}"
            f"?module=account"
            f"&action=txlist"
            f"&address={wallet}"
            f"&startblock=0"
            f"&endblock='latest'"
            f"&page=1"
            f"&offset=1000&sort=asc"
            f"&apikey={api}")
    result = requests.get(url).json()
    return result

def handle_menu_choice(choice):
    if choice == "1":
        for wallet in wallets:
            txs = get_tx(wallet, api, url)
            for tx in txs['result']:
                if tx["from"].lower() == wallet.lower():
                    print(wallet, tx)

    elif choice == "2":
        for wallet in wallets:
            txs = get_tx(wallet, api, url)
            total_fee = 0
            tx_num = len(txs['result'])
            for tx in txs['result']:
                total_fee += (int(tx["gasUsed"]) * int(tx["gasPrice"])) / 10 ** 18
            print(f"Wallet: {wallet} | Gas burnt: {total_fee} | TXs: {tx_num}")

    elif choice == "3":
        for wallet in wallets:
            txs = get_tx(wallet, api, url)
            total_fee = 0
            tx_num = len(txs['result'])
            for tx in txs['result']:
                if tx["to"].lower() == contract_to_check.lower():
                    print(f"Wallet: {wallet} | Tx hash: {tx['hash']}")

    elif choice == "q":
        print("Exiting...")
        return True
    else:
        print("Invalid choice. Please try again.")
    return False

def main_menu():
    print("===== Main Menu =====")
    print("1. Get list of txs")
    print("2. Get total gas burnt and txs count")
    print("3. Get contract call by address")
    print("q. Quit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if handle_menu_choice(choice.lower()):
            break

if __name__ == '__main__':
    contract_to_check = "0x00000000000E1A99dDDd5610111884278BDBda1D" #Clusterz contract on Ethereum
    network = ("ethereum")
    api = api[network]
    url = url[network]
    main()
