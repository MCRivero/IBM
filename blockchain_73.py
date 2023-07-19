genesis_block = {
        'previous_hash': '', 
        'index': 0,
        'transactions': []
}
blockchain = [genesis_block]

# 1. Necesitamos manejar una lista de transacciones
open_transactions = []
owner = 'Carmen'

def hash_block(block):
    return '-'.join([str([block[key]])  for key in block])

def get_last_blockchain_value():
    # Control sobre la blockchain para saber si esta vacia 
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain
    
        Arguments:
        :sender: the sender of the coins
        :recipient: the recipient of the coins
        :amount: the amount of coins sent with the transaction (default = 1.0)
    """
    # Queremos añadir una nueva transaction a la lista de transacciones abiertas 
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }

    # Para que esto funcione tenemos que trabajar en nuestro USER INPUT "waiting_for_input - get_transaction_value"
    open_transactions.append(transaction)
 
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    
""" Para no repetir el código, definimos una funcion ==> get_transaction_value() <== que será llamada en el while"""
def get_transaction_value():
    # Get the user input, transform it from a string to a float and store it
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))

    # Retornamos los datos y aqui podemos usar TUPLE
    # TUPLE puede ser creada sin () y entonces retornamos tx_recipient y tx_amount
    # tenemos dos tipos de datos, string, y float, pero esto es el uso comun en una TUPLE
    # TUPLE debe ser creada con paraentesis, para crear una TUPLE de un solo valor 
    # usaremos (tx_recipient, )

    return tx_recipient, tx_amount

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
   for (index, block) in enumerate(blockchain):
       if index == 0:
           continue
       if block['previous_hash'] != hash_block(blockchain[index - 1]):
           return False
   else:
        return True
       
waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit!')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # TUPLE UNPACKING
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '', 
                'index': 0,
                'transactions': [{'sender': 'Gloria', 'recipient': 'Manolo', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print('User left!')
print('Done!')