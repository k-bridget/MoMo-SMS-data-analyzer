-- Creating the database
CREATE DATABASE IF NOT EXISTS momo_sms_db;
USE momo_sms_db;

-- Drop tables if they exist (to avoid conflicts when rerunning the script)
DROP TABLE IF EXISTS System_logs;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Transaction_categories;
DROP TABLE IF EXISTS Users;

-- Creating Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    user_type ENUM('customer', 'admin') NOT NULL
);

-- Creating Transaction_categories table
CREATE TABLE Transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    category_type ENUM('income', 'expense') NOT NULL
);

-- Creating Transactions table
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL CHECK (amount >= 0),
    currency VARCHAR(10) NOT NULL,
    transaction_date DATETIME NOT NULL,
    status ENUM('completed', 'pending', 'failed') NOT NULL,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    category_id INT,
    FOREIGN KEY (sender_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Transaction_categories(category_id) ON DELETE SET NULL
);

-- Creating indexes on foreign keys for performance
CREATE INDEX idx_sender ON Transactions(sender_id);
CREATE INDEX idx_receiver ON Transactions(receiver_id);
CREATE INDEX idx_category ON Transactions(category_id);

-- Creating System_logs table
CREATE TABLE System_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    time_stamp DATETIME NOT NULL,
    transaction_id INT NOT NULL,
    log_message VARCHAR(255) NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES Transactions(transaction_id) ON DELETE CASCADE
);

CREATE INDEX idx_transaction_log ON System_logs(transaction_id);

-- Inserting sample data into Users
INSERT INTO Users (name, phone_number, user_type) VALUES
('Alice Umwiza', '0792336548', 'customer'),
('Bob Manzi', '0789433569', 'customer'),
('Bridget Karungi', '0788233465', 'admin'),
('Diakite Muheto', '0788893748', 'customer'),
('Ntwari Enock', '0793442608', 'customer');

-- Inserting sample data into Transaction_categories
INSERT INTO Transaction_categories (category_name, category_type) VALUES
('Groceries', 'expense'),
('Salary', 'income'),
('Utilities', 'expense'),
('Investment', 'income'),
('Entertainment', 'expense');

-- Inserting sample data into Transactions
INSERT INTO Transactions (amount, currency, transaction_date, status, sender_id, receiver_id, category_id) VALUES
(1700.00, 'FRW', '2024-06-01 10:00:00', 'completed', 1, 2, 1),
(2000.00, 'FRW', '2024-06-02 09:00:00', 'completed', 3, 1, 2),
(2500.50, 'FRW', '2024-06-03 15:30:00', 'pending', 2, 4, 3),
(1700.00, 'FRW', '2024-06-04 12:00:00', 'completed', 4, 5, 4),
(1900.00, 'FRW', '2024-06-05 18:45:00', 'completed', 5, 1, 5);

-- Inserting sample data into System_logs
INSERT INTO System_logs (time_stamp, transaction_id, log_message) VALUES
('2024-06-01 10:01:00', 1, 'Transaction completed successfully'),
('2024-06-02 09:05:00', 2, 'Salary payment processed'),
('2024-06-03 15:35:00', 3, 'Transaction pending approval');
