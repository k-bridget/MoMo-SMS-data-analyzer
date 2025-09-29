import time
import random
import xml.etree.ElementTree as ET

# Parse XML and extract transactions
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    transactions = []
    for i, record in enumerate(root.findall('.//record'), 1):  # Assuming records are under some tag
        transaction = {
            'id': i,
            'type': record.find('type').text if record.find('type') is not None else 'unknown',
            'amount': float(record.find('amount').text) if record.find('amount') is not None else 0.0,
            'sender': record.find('sender').text if record.find('sender') is not None else '',
            'receiver': record.find('receiver').text if record.find('receiver') is not None else '',
            'timestamp': record.find('timestamp').text if record.find('timestamp') is not None else ''
        }
        transactions.append(transaction)
    return transactions

# Generate additional transactions if needed to reach at least 20
def generate_additional(transactions, n=20):
    while len(transactions) < n:
        transactions.append({
            'id': len(transactions) + 1,
            'type': 'generated',
            'amount': random.uniform(10, 1000),
            'sender': f'sender{len(transactions)}',
            'receiver': f'receiver{len(transactions)}',
            'timestamp': '2023-01-01'
        })
    return transactions

# Linear Search: O(n)
def linear_search(transactions, target_id):
    for transaction in transactions:
        if transaction['id'] == target_id:
            return transaction
    return None

# Dictionary Lookup: O(1) average
def dict_lookup(trans_dict, target_id):
    return trans_dict.get(target_id, None)

# Main function to compare
def main():
    # Parse XML
    try:
        transactions = parse_xml('modified_sms_v2.xml')
    except FileNotFoundError:
        print("XML file not found, using generated data.")
        transactions = []

    # Ensure at least 20 transactions
    transactions = generate_additional(transactions, 20)
    print(f"Using {len(transactions)} transactions.")

    # Choose a random target ID to search
    target_id = random.choice([t['id'] for t in transactions])
    print(f"Searching for transaction with ID: {target_id}")

    # Linear Search
    start_time = time.time()
    result_linear = linear_search(transactions, target_id)
    linear_time = time.time() - start_time

    # Dictionary Lookup
    trans_dict = {t['id']: t for t in transactions}
    start_time = time.time()
    result_dict = dict_lookup(trans_dict, target_id)
    dict_time = time.time() - start_time

    # Results
    print(f"Linear Search Time: {linear_time:.6f} seconds")
    print(f"Dictionary Lookup Time: {dict_time:.6f} seconds")
    if dict_time > 0:
        print(f"Dictionary is {linear_time / dict_time:.2f} times faster")
    else:
        print("Dictionary lookup instantaneous")

    # Verify results are the same
    assert result_linear == result_dict, "Results should match"
    print("Results match:", result_linear)

    # Reflection
    print("\nReflection:")
    print("Dictionary lookup is faster than linear search because it uses a hash table for average O(1) time complexity,")
    print("while linear search has O(n) time complexity, scanning each element sequentially.")
    print("For large datasets, this difference becomes significant.")
    print("\nAnother data structure/algorithm: Binary search on a sorted list (O(log n)), or a balanced BST like AVL tree for O(log n) insertions and lookups.")

if __name__ == "__main__":
    main()
