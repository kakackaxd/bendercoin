from flask import json
from .util import from_dict
from .transaction import Transaction

TRANSACTIONS = []

def load_transactions():
    global TRANSACTIONS
    TRANSACTIONS = []
    with open("transactions.json") as f:
        data = json.load(f)
    for item in data:
        tx = from_dict(Transaction, item)
        TRANSACTIONS.append(tx)

    return TRANSACTIONS


def save_transactions():
    global TRANSACTIONS
    with open("transactions.json", "w") as f:
        json.dump(TRANSACTIONS, f, indent=4)
