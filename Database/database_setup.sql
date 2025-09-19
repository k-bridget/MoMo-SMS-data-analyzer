CREATE DATABASE momo_sms_db;
USE momo_sms_db;


DROP TABLE IF EXISTS System_logs;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Transaction_categories;
DROP TABLE IF EXISTS Users;

-- Create Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    user_type TEXT NOT NULL
);

-- Create Transaction_categories table
CREATE TABLE Transaction_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    category_type TEXT NOT NULL
);

-- Create Transactions table
CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL CHECK (amount >= 0),
    currency TEXT NOT NULL,
    transaction_date TEXT NOT NULL,
    status TEXT NOT NULL,
    sender_id INTEGER NOT NULL,
    receiver_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (sender_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Transaction_categories(category_id) ON DELETE SET NULL
);

-- Create indexes on foreign keys for performance
CREATE INDEX idx_sender ON Transactions(sender_id);
CREATE INDEX idx_receiver ON Transactions(receiver_id);
CREATE INDEX idx_category ON Transactions(category_id);

-- Create System_logs table
CREATE TABLE System_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_stamp TEXT NOT NULL,
    transaction_id INTEGER NOT NULL,
    log_message TEXT NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id) ON DELETE CASCADE
);

CREATE INDEX idx_transaction_log ON System_logs(transaction_id);

-- Insert sample data into Users (5 records)
INSERT INTO Users (name, phone_number, user_type) VALUES
('Alice Umwiza', '0792336548', 'customer'),
('Bob Manzi', '0789433569', 'customer'),
('Bridget Karungi', '0788233465', 'admin'),
('Diakite Muheto', '0788893748', 'customer'),
('Ntwari Enock', '0793442608', 'customer');

-- Insert sample data into Transaction_categories (5 records)
INSERT INTO Transaction_categories (category_name, category_type) VALUES
('Groceries', 'expense'),
('Salary', 'income'),
('Utilities', 'expense'),
('Investment', 'income'),
('Entertainment', 'expense');

-- Insert sample data into Transactions (5 records)
INSERT INTO Transactions (amount, currency, transaction_date, status, sender_id, receiver_id, category_id) VALUES
(1500.00, 'FRW', '2024-06-01 10:00:00', 'completed', 1, 2, 1),
(2000.00, 'Frw', '2024-06-02 09:00:00', 'completed', 3, 1, 2),
(2500.50, 'FRW', '2024-06-03 15:30:00', 'pending', 2, 4, 3),
(1500.00, 'FRW', '2024-06-04 12:00:00', 'completed', 4, 5, 4),
(1200.00, 'FRW', '2024-06-05 18:45:00', 'completed', 5, 1, 5);

-- Insert sample data into System_logs (3 records)
INSERT INTO System_logs (time_stamp, transaction_id, log_message) VALUES
('2024-06-01 10:01:00', 1, 'Transaction completed successfully'),
('2024-06-02 09:05:00', 2, 'Salary payment processed'),
('2024-06-03 15:35:00', 3, 'Transaction pending approval');

-- Basic CRUD operations for testing

-- SELECT all users
-- SELECT * FROM Users;

-- INSERT a new user
-- INSERT INTO Users (name, phone_number, user_type) VALUES ('Frank Green', '678-901-2345', 'customer');

-- UPDATE a user's phone number
-- UPDATE Users SET phone_number = '999-999-9999' WHERE user_id = 1;

-- DELETE a user
-- DELETE FROM Users WHERE user_id = 5;

-- SELECT transactions with sender and receiver details
-- SELECT t.transaction_id, t.amount, t.currency, t.transaction_date, t.status,
--        s.name AS sender_name, r.name AS receiver_name, c.category_name
-- FROM Transactions t
-- JOIN Users s ON t.sender_id = s.user_id
-- JOIN Users r ON t.receiver_id = r.user_id
-- JOIN Transaction_categories c ON t.category_id = c.category_id;

-- End of script

