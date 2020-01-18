                                                  Electronic Vendor Database

Overview

The application is an electronics vendor that operates both a website and a chain of many physical stores. Examples include Best Buy and Circuit City. To think out more about this application, think about any experiences you may have had making purchases both online and in store, and browse their websites.
In our hypothetical company, we have designed a major part of the database that underlies company operations. Here are a few points we have considered:
•	There are many different products, grouped into a variety of (possibly overlapping) categories. Groups are formed by type of product (cameras, phones, etc.), by manufacturer (Sony, Apple, etc.), or by other means (for example, a Gateway PC might be packaged with a Sony monitor and an HP printer and marketed as a package).
•	Some customers have a contract with the company and can bill their purchases to an account number. They are billed monthly. Other customers are infrequent customers and pay with a credit or debit card. Card information are stored for online customers, but not for in-store customers.
•	Online sales are sent to a shipper. The company stores the tracking number for the shipping company so it can respond to customer inquiries.
•	Inventory are accurate both in stores and in warehouses which is used to replenish stores and to ship to online customers. When inventory is low, a reorder is sent to the manufacturer listed in the database. When goods arrive, inventory is updated, and reorders marked as having been filled.


Application

The application is developed for only one electronic vendor (e.g., Best Buy). It should support the following actions:
•	Every customer can register an account with an email and will be assigned an ID (as a frequent customer). If one customer purchases multiple products from the website and physical stores, the same ID is used. Note that frequent customers can also purchase as infrequent customers.
•	A frequent customer holding an account can register/modify/delete the information for their account.
•	A frequent customer can complete his/her transaction online (including shipping) and check his/her purchase history from both website and the physical stores, as well as the stock information of different products available for purchase (both online and physical stores).
•	Infrequent customers can complete their online transactions using their credit cards. Before each purchase, the system checks that if the customer has enough available credit for the purchase (assuming that the available credit is also maintained by the electronic vendor).


