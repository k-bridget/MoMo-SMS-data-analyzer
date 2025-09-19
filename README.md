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

The MoMo SMS Data Processing System Entity Relationship Diagram (ERD) was created to fulfill business and technical requirements and be extendable, maintainable, and efficient in processing mobile money data. The four major entities and the general themes for designing are Users, Transactions, Transaction_Categories, and System_Logs. They are essential attributes of a mobile money scenario and are still receptive to further enhancements.
Both senders and recipients are also stored in the Users table along with the user type (customer, merchant, or agent), phone number, and name. It is stored separately from it to maintain it in a highly normalized form, prevent redundancy, and make customer segmentation for reporting purposes, as well as service customization, more straightforward.


The Transactions table is the main table in the database that records the primary attributes like amount, currency, date, and transaction status. Foreign key references of receiver, sender, and category are also stored in the table for money flow tracking and transaction history.
The additional Transaction_Categories table was used to type transactions such as payments, transfers, and airtime purchases. Abstraction here supports ad hoc querying through patterns and trends by transaction type.


Transparency and accountability are achieved by the System_Logs table through the maintenance of system activity and errors encountered with respect to particular transactions. Troubleshooting and auditing are facilitated by the design with accountability for data processing.


All the relationships were correctly created: a user may have multiple transactions, a category may be related to several transactions, and a transaction may have several logs. The design provides for a possible future many-to-many relationship resolution through a junction. The ERD is a generally normalized and stable database schema that can deal with quick processing, business intelligence needs, secure storage, and reasonable analysis of MoMo SMS data.


...








**Scrum board link:**

https://alustudent-team-dcq685fi.atlassian.net/jira/software/projects/T1/boards/34


## JSON Data Modeling
Our relational tables were serialized into JSON for API responses.  

### SQL → JSON Mapping
- **Users** → JSON `Users` array  
- **Transaction_Categories** - JSON `Transaction_Categories` array  
- **Transactions** - JSON `Transactions` array (with sender_id, receiver_id, category_id)  
- **System_Logs** - JSON `System_Logs` array  
- **Complex_Transaction_Object** - Nested JSON object showing one transaction with related user info, category, and logs.   
