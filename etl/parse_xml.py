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
            "id": sms.get("date"),  # using "date" as unique ID
            "type": sms.get("type"),  # 1 = received, 2 = sent (we can map later)
            "amount": None,  # will extract from body
            "sender": sms.get("address"),
            "receiver": None,  # may also come from body
            "timestamp": sms.get("readable_date"),
            "body": sms.get("body")  # keep full SMS text for later parsing
        }
        transactions.append(transaction)

    return transactions

if __name__ == "__main__":
    file_path = "data/raw/modified_sms_v2.xml"
    records = parse_sms(file_path)

    if not records:
        print("No transactions found or file missing.")
    else:
        print(f"Parsed {len(records)} transactions")
        for r in records[:5]:  # print first 5
            print(r)
