from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
# #     This line will mess with our autograders, but might be useful when debugging
#     print( "Connected to Ethereum node" )

# else:
#     print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx = w3.eth.get_transaction(tx)
    return tx

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    transaction = get_transaction(tx)
    gas_price =  transaction.gasPrice #YOUR CODE HERE
    
    return gas_price

def get_gas(tx):
    gas = w3.eth.get_transaction_receipt(tx).gasUsed
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas_price(tx) * get_gas(tx) #YOUR CODE HERE
    # print(get_gas_price(tx))
    # print(get_gas(tx))
    return tx_cost
# get_transaction_cost('0x9a29da1ec35f0ccc9fbebfba5d93ea16fd1edbde8070967de7b7cd5b6b01a82f')

def get_block_cost(block_num):
    block = w3.eth.get_block(block_num)
    block_cost = HexBytes('0') #YOUR CODE HERE
    for x in block.transactions:
        block_cost = x+block_cost
    return block_cost
# print("BLOCK: ",get_block_cost(2000000))

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    return max_tx
