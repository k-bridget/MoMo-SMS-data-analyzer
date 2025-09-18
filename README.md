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

The ERD shows these core entities, attributes, and relationships:
1. Users- User records(sender/receiver)
2. Transactions- transaction records.
3. Transaction_categories -Transaction types.
4. System_logs - for tracking data processing.

** Relationships**
1. A user can have many Transactions(one to many).
2. One transaction_category can appear on many transactions(one to many).
3. One transaction can have many system_logs(one to many).
4. Transactions table(Junction table) shows the relation between users and transaction_categories through the junction table(transactions) (M:N).



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
