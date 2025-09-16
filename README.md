# MoMo-SMS-data-analyzer

**Team name:**
Team 14

**Member list**

1. Ntwari Enock
2. Muheto Mohammed Diakite
3. Karungi Bridget

**Project Description**

This project is an enterprise-level full-stack application that processes MoMo SMS data in XML format, cleans and categorizes the data, stores it in a relational database, and builds a frontend interface to analyze and visualize the data.

**Architecture Diagram link**
https://drive.google.com/file/d/1K0mqCrwEBYd1XCdkQUQJX3CplMUvC0OH/view?usp=sharing

**ERD documentation**
The Entity Relationship Diagram (ERD) of the MoMo SMS data processing system was designed for technical as well as business requirements with the advantage of data scalability and data integrity. The database is centered around four main entities: Users, Transactions, Transaction Categories, and System Logs. The entities were chosen to cover the majority of necessary features of a mobile money ecosystem and provide mature transactional data analysis.

Users table contains data of the receivers and senders of a transaction. Name, phone number, and type of user (agent, customer, or merchant) enable us to segment the participants and permit future segmentation or customization of services. The backbone of the system is the Transactions table with minimum data like amount, currency, date of the transaction, and status. It is also referenced to sender, receiver, and type of transaction via foreign keys in a way that tracing of all is feasible.

Transaction Categories entity has been added in order to classify transactions as a type of payment, transfer, or airtime purchase. This allows reporting and analysis by being able to view patterns between types of transactions with queries. System Logs entity helps keep data transparent during processing by logging errors and significant system events and relating them to specific transactions as required.

ERD relationships were defined in simple language: one user can have many transactions, one category can be applied to many transactions, and one transaction can have many logs. They were selected to provide the reality with the best possible description without redundancy. Global schema provides us with an unbroken and normalised foundation which allows efficient storage, querying, and potential future serialization to JSON to return value from API.


**Scrum board link:**

https://github.com/users/k-bridget/projects/2 



## JSON Data Modeling
Our relational tables were serialized into JSON for API responses.  

### SQL → JSON Mapping
- **Users** → JSON `Users` array  
- **Transaction_Categories** - JSON `Transaction_Categories` array  
- **Transactions** - JSON `Transactions` array (with sender_id, receiver_id, category_id)  
- **System_Logs** - JSON `System_Logs` array  
- **Complex_Transaction_Object** - Nested JSON object showing one transaction with related user info, category, and logs.   