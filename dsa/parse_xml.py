# dsa/parse_xml.py
"""
Parse modified_sms_v2.xml into JSON transactions list.
Expected XML structure per record (example):
<sms>
  <id>123</id>
  <type>credit</type>
  <amount>5000</amount>
  <sender>+2507...</sender>
  <receiver>+25078...</receiver>
  <timestamp>2025-09-20T12:34:56</timestamp>
  <text>Payment received</text>
</sms>
"""

import xml.etree.ElementTree as ET
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))  # project root
XML_FILE = os.path.join(ROOT, "modified_sms_v2.xml")
OUT_FILE = os.path.join(ROOT, "api", "transactions.json")

def element_to_dict(elem):
    d = {}
    for child in elem:
        d[child.tag] = child.text
    # ensure id exists as string
    if "id" in d:
        d["id"] = str(d["id"])
    return d

def parse(xml_path=XML_FILE, out_path=OUT_FILE):
    if not os.path.exists(xml_path):
        print("XML file not found:", xml_path)
        return []
    tree = ET.parse(xml_path)
    root = tree.getroot()
    transactions = []
    # if root contains many <sms> children
    for sms in root.findall(".//sms"):
        d = element_to_dict(sms)
        if "id" in d:
            transactions.append(d)
    # save as JSON
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(transactions, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(transactions)} transactions to {out_path}")
    return transactions

if __name__ == "__main__":
    parse()
