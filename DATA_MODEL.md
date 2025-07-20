# Data Model

This document outlines the data model for the Algerian Sales Agent.

## Tables

### Products

This table stores information about the products that are being tracked.

| Column      | Type        | Description                                  |
|-------------|-------------|----------------------------------------------|
| `id`        | `INTEGER`   | The unique identifier for the product.       |
| `name`      | `TEXT`      | The name of the product.                     |
| `description`| `TEXT`     | A description of the product.                |
| `url`       | `TEXT`      | The URL of the product on the original website.|
| `image_url` | `TEXT`      | The URL of the product image.                |
| `created_at`| `TIMESTAMP` | The timestamp when the product was created.  |
| `updated_at`| `TIMESTAMP` | The timestamp when the product was last updated.|

### Sales

This table stores information about the sales of the products.

| Column      | Type        | Description                                  |
|-------------|-------------|----------------------------------------------|
| `id`        | `INTEGER`   | The unique identifier for the sale.          |
| `product_id`| `INTEGER`   | A foreign key to the `products` table.       |
| `price`     | `DECIMAL`   | The price of the product at the time of the sale.|
| `sale_price`| `DECIMAL`   | The sale price of the product.               |
| `start_date`| `TIMESTAMP` | The start date of the sale.                  |
| `end_date`  | `TIMESTAMP` | The end date of the sale.                    |
| `created_at`| `TIMESTAMP` | The timestamp when the sale was created.     |

### Users

This table stores information about the users of the application.

| Column      | Type        | Description                                  |
|-------------|-------------|----------------------------------------------|
| `id`        | `INTEGER`   | The unique identifier for the user.          |
| `username`  | `TEXT`      | The username of the user.                    |
| `password`  | `TEXT`      | The hashed password of the user.             |
| `email`     | `TEXT`      | The email address of the user.               |
| `created_at`| `TIMESTAMP` | The timestamp when the user was created.     |

### Transactions

This table stores information about the transactions that are made on the platform.

| Column      | Type        | Description                                  |
|-------------|-------------|----------------------------------------------|
| `id`        | `INTEGER`   | The unique identifier for the transaction.   |
| `user_id`   | `INTEGER`   | A foreign key to the `users` table.          |
| `product_id`| `INTEGER`   | A foreign key to the `products` table.       |
| `amount`    | `DECIMAL`   | The amount of the transaction.               |
| `status`    | `TEXT`      | The status of the transaction (e.g., pending, completed, failed).|
| `created_at`| `TIMESTAMP` | The timestamp when the transaction was created.|
