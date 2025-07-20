# System Architecture

This document outlines the high-level system architecture for the Algerian Sales Agent.

## Components

The system is composed of the following main components:

*   **Scraper:** This component is responsible for gathering product information and sales data from various e-commerce websites in Algeria. It will be designed to be extensible, so that new websites can be added easily.
*   **Database:** This component stores the scraped data, including product information, prices, and sales history. It will also store user data and transaction information.
*   **API Server:** This component provides a RESTful API for interacting with the database. It will be used by the frontend to display product information and by the backend to manage the reselling process.
*   **Frontend:** This component is the user interface of the application. It will be a web application that allows users to browse products, view sales, and make purchases.
*   **Payment Gateway:** This component handles the payment processing for the application. It will be integrated with a popular payment gateway in Algeria.
*   **Reselling Engine:** This component is the core of the application. It will be responsible for identifying trending products, managing the reselling process, and automating the purchase and relisting of products.

## Interactions

The components interact with each other in the following way:

1.  The **Scraper** gathers data from e-commerce websites and stores it in the **Database**.
2.  The **API Server** retrieves data from the **Database** and exposes it to the **Frontend**.
3.  The **Frontend** displays the data to the user and allows them to make purchases.
4.  When a user makes a purchase, the **Frontend** sends a request to the **API Server**.
5.  The **API Server** processes the request and interacts with the **Payment Gateway** to handle the payment.
6.  The **Reselling Engine** continuously monitors the data in the **Database** to identify trending products.
7.  When a trending product is identified, the **Reselling Engine** automatically purchases the product and relists it on the platform.

## Diagram

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Scraper     +----->+    Database    <----->+   API Server   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
                                                       ^
                                                       |
                                                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Reselling     +----->+ Payment Gateway<----- +    Frontend    |
|    Engine      |      |                |      |                |
+----------------+      +----------------+      +----------------+
```
