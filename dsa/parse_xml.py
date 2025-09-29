import xml.etree.ElementTree as ET
import re

def parse_sms_body(body):
    # Initialize defaults
    transaction_type = 'unknown'
    amount = 0.0
    sender = ''
    receiver = ''
    
    # Patterns for different transaction types
    received_pattern = r"You have received (\d+(?:,\d+)?(?:\.\d+)?) RWF from ([^()]+)"
    payment_pattern = r"Your payment of (\d+(?:,\d+)?(?:\.\d+)?) RWF to ([^()]+)"
    transfer_pattern = r"(\d+(?:,\d+)?(?:\.\d+)?) RWF transferred to ([^()]+).*from (\d+)"
    deposit_pattern = r"A bank deposit of (\d+(?:,\d+)?(?:\.\d+)?) RWF has been added"
    
    if re.search(received_pattern, body):
        match = re.search(received_pattern, body)
        amount = float(match.group(1).replace(',', ''))
        sender = match.group(2).strip()
        transaction_type = 'received'
    elif re.search(payment_pattern, body):
        match = re.search(payment_pattern, body)
        amount = float(match.group(1).replace(',', ''))
        receiver = match.group(2).strip()
        transaction_type = 'payment'
    elif re.search(transfer_pattern, body):
        match = re.search(transfer_pattern, body)
        amount = float(match.group(1).replace(',', ''))
        receiver = match.group(2).strip()
        # sender could be extracted from 'from' but it's an ID, so leave as ''
        transaction_type = 'transfer'
    elif re.search(deposit_pattern, body):
        match = re.search(deposit_pattern, body)
        amount = float(match.group(1).replace(',', ''))
        transaction_type = 'deposit'
    
    return {
        'type': transaction_type,
        'amount': amount,
        'sender': sender,
        'receiver': receiver
    }

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    transactions = []
    for i, sms in enumerate(root.findall('sms'), 1):
        body = sms.get('body', '')
        parsed = parse_sms_body(body)
        transaction = {
            'id': i,
            'type': parsed['type'],
            'amount': parsed['amount'],
            'sender': parsed['sender'],
            'receiver': parsed['receiver'],
            'timestamp': sms.get('date', '')
        }
        transactions.append(transaction)
    return transactions
