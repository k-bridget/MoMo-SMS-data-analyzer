import sqlite3
import os

# Path to the SQL file
sql_file = 'database_setup_sqlite.sql'

# Database file
db_file = 'momo_sms.db'

# Remove existing db if any
if os.path.exists(db_file):
    os.remove(db_file)

# Connect to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Read and execute the SQL file
with open(sql_file, 'r') as f:
    sql_script = f.read()

# Split the script into statements (basic split by semicolon)
statements = sql_script.split(';')

for statement in statements:
    statement = statement.strip()
    if statement:
        try:
            cursor.execute(statement)
        except sqlite3.Error as e:
            print(f"Error executing statement: {statement}")
            print(f"Error: {e}")

conn.commit()

# Now, test the database with some queries
print("Testing database...")

# Test SELECT all users
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
print("Users:")
for user in users:
    print(user)

# Test SELECT transactions with joins
cursor.execute("""
SELECT t.transaction_id, t.amount, t.currency, t.transaction_date, t.status,
       s.name AS sender_name, r.name AS receiver_name, c.category_name
FROM Transactions t
JOIN Users s ON t.sender_id = s.user_id
JOIN Users r ON t.receiver_id = r.user_id
JOIN Transaction_categories c ON t.category_id = c.category_id
""")
transactions = cursor.fetchall()
print("\nTransactions:")
for trans in transactions:
    print(trans)

# Test INSERT a new user
cursor.execute("INSERT INTO Users (name, phone_number, user_type) VALUES ('Test User', '111-222-3333', 'customer')")
conn.commit()
print("\nInserted new user.")

# Test UPDATE
cursor.execute("UPDATE Users SET phone_number = '999-999-9999' WHERE name = 'Test User'")
conn.commit()
print("Updated user phone.")

# Test DELETE
cursor.execute("DELETE FROM Users WHERE name = 'Test User'")
conn.commit()
print("Deleted user.")

# Close connection
conn.close()

print("Database test completed successfully.")

