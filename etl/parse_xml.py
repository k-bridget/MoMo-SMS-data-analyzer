import xml.etree.ElementTree as ET
import os

def parse_sms(xml_file):
    if not os.path.exists(xml_file):
        print(f"File not found: {xml_file}")
        return []

    tree = ET.parse(xml_file)
    root = tree.getroot()

    transactions = []
    for sms in root.findall("sms"):
        transaction = {
            "id": sms.get("id"),
            "type": sms.get("type"),
            "amount": sms.get("amount"),
            "sender": sms.get("sender"),
            "receiver": sms.get("receiver"),
            "timestamp": sms.get("timestamp"),
        }
        transactions.append(transaction)

    return transactions


if __name__ == "__main__":
    file_path = "data/raw/momo.xml"
    records = parse_sms(file_path)

    if not records:
        print("No transactions found or file missing.")
    else:
        print("Parsed Transactions:")
        for r in records:
            print(r)
