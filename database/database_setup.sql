-- Create the MoMo Database
CREATE DATABASE momo_transactions_db;
USE momo_transactions_db;
-- This script creates tables, constraints, indexes, inserts sample data, and includes basic CRUD operations for testing.

-- Drop tables if they exist to start fresh
DROP TABLE IF EXISTS System_logs;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Transaction_categories;
DROP TABLE IF EXISTS Users;

-- Create Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Primary key: Unique user identifier',
    name VARCHAR(50) NOT NULL COMMENT 'User full name',
    phone_number VARCHAR(13) NOT NULL COMMENT 'User phone number',
    user_type VARCHAR(20) NOT NULL COMMENT 'Type of user (e.g., admin, customer)'
) ENGINE=InnoDB;

-- Create Transaction_categories table
CREATE TABLE Transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Primary key: Unique category identifier',
    category_name VARCHAR(50) NOT NULL COMMENT 'Name of the transaction category',
    category_type VARCHAR(50) NOT NULL COMMENT 'Type of category (e.g., expense, income)'
) ENGINE=InnoDB;

-- Create Transactions table
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Primary key: Unique transaction identifier',
    amount DECIMAL(15,2) NOT NULL CHECK (amount >= 0) COMMENT 'Transaction amount, must be non-negative',
    currency VARCHAR(50) NOT NULL COMMENT 'Currency code (e.g., USD, EUR)',
    transaction_date DATETIME NOT NULL COMMENT 'Date and time of the transaction',
    status VARCHAR(20) NOT NULL COMMENT 'Transaction status (e.g., pending, completed)',
    sender_id INT NOT NULL COMMENT 'Foreign key: User who sent the transaction',
    receiver_id INT NOT NULL COMMENT 'Foreign key: User who received the transaction',
    category_id INT NOT NULL COMMENT 'Foreign key: Category of the transaction',
    CONSTRAINT fk_sender FOREIGN KEY (sender_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_receiver FOREIGN KEY (receiver_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES Transaction_categories(category_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Create indexes on foreign keys for performance
CREATE INDEX idx_sender ON Transactions(sender_id);
CREATE INDEX idx_receiver ON Transactions(receiver_id);
CREATE INDEX idx_category ON Transactions(category_id);

-- Create System_logs table
CREATE TABLE System_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Primary key: Unique log entry identifier',
    time_stamp DATETIME NOT NULL COMMENT 'Timestamp of the log entry',
    transaction_id INT NOT NULL COMMENT 'Foreign key: Related transaction',
    log_message VARCHAR(255) NOT NULL COMMENT 'Log message details',
    CONSTRAINT fk_transaction_log FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE INDEX idx_transaction_log ON System_logs(transaction_id);

-- Insert sample data into Users (5 records)
INSERT INTO Users (name, phone_number, user_type) VALUES
('Alice Johnson', '123-456-7890', 'customer'),
('Bob Smith', '234-567-8901', 'customer'),
('Carol White', '345-678-9012', 'admin'),
('David Brown', '456-789-0123', 'customer'),
('Eve Davis', '567-890-1234', 'customer');

-- Insert sample data into Transaction_categories (5 records)
INSERT INTO Transaction_categories (category_name, category_type) VALUES
('Groceries', 'expense'),
('Salary', 'income'),
('Utilities', 'expense'),
('Investment', 'income'),
('Entertainment', 'expense');

-- Insert sample data into Transactions (5 records)
INSERT INTO Transactions (amount, currency, transaction_date, status, sender_id, receiver_id, category_id) VALUES
(150.00, 'USD', '2024-06-01 10:00:00', 'completed', 1, 2, 1),
(2000.00, 'USD', '2024-06-02 09:00:00', 'completed', 3, 1, 2),
(75.50, 'USD', '2024-06-03 15:30:00', 'pending', 2, 4, 3),
(500.00, 'USD', '2024-06-04 12:00:00', 'completed', 4, 5, 4),
(120.00, 'USD', '2024-06-05 18:45:00', 'completed', 5, 1, 5);

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
