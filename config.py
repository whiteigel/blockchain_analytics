import os

from dotenv import load_dotenv

load_dotenv()

api = {
"ethereum": os.getenv('ethereum'),
"scroll": os.getenv('scroll'),
"zksync": os.getenv('zksync'),
"bsc": os.getenv('bsc'),
"arbitrum": os.getenv('arbitrum')
}

url = {
"ethereum": "https://api.etherscan.io/api",
"scroll": "https://api.scrollscan.com/api",
"zksync": "https://api-era.zksync.network/api",
"bsc": "https://api.bscscan.com/api",
"arbitrum": "https://api.arbiscan.io/api"
}