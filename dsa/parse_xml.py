import xml.etree.ElementTree as ET
import os
import re

def parse_sms(xml_file):
    if not os.path.exists(xml_file):
        print(f"File not found: {xml_file}")
        return []

    tree = ET.parse(xml_file)
    root = tree.getroot()
    transactions = []

    for sms in root.findall("sms"):
        body = sms.get("body", "")
        
        # Extract Transaction ID
        txn_id_match = re.search(r"Financial Transaction Id[: ]+(\d+)|TxId[: ]+(\d+)", body)
        txn_id = txn_id_match.group(1) or txn_id_match.group(2) if txn_id_match else ""

        # Extract amount
        amount_match = re.search(r"(\d[\d,]*)\s*RWF", body)
        amount = amount_match.group(1).replace(",", "") if amount_match else ""

        # Extract sender name
        sender_match = re.search(r"from ([\w\s]+) \(", body)
        sender = sender_match.group(1) if sender_match else ""

        # Extract receiver name (optional)
        receiver_match = re.search(r"to ([\w\s]+)(?: \d+)?", body)
        receiver = receiver_match.group(1) if receiver_match else ""

        # Timestamp
        timestamp = sms.get("readable_date") or sms.get("date")

        transaction = {
            "id": txn_id,
            "type": sms.get("type", ""),
            "amount": amount,
            "sender": sender,
            "receiver": receiver,
            "timestamp": timestamp
        }
        transactions.append(transaction)

    return transactions

if _name_ == "_main_":
    file_path = "data/raw/modified_sms_v2.xml"
    records = parse_sms(file_path)

    if not records:
        print("No transactions found or file missing.")
    else:
        print("Parsed Transactions:")
        for r in records[:10]:  # print first 10 for brevity
            print(r)
