# Algerian Sales Agent

A full‑stack application that constantly gathers trending products and sales data from popular Algerian e‑commerce sites, automates purchasing of trending items, and resells them on a dedicated platform. This project encompasses web scraping, a RESTful API, and a user‑friendly frontend.

---

## Table of Contents

1. [Features](#features)
2. [High‑Level Design](#high‑level-design)
3. [Getting Started](#getting-started)
4. [Architecture Overview](#architecture-overview)
5. [Data Model](#data-model)
6. [Technology Stack](#technology-stack)
7. [UI/UX](#uiux)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

* **Web Scraping:** Periodically crawls and parses product listings and sales metrics from leading Algerian e‑commerce platforms (e.g., Jumia, Ouedkniss).
* **Trending Products Detection:** Analyzes scraped data to surface trending items based on metrics like price fluctuation, sales volume, and user engagement.
* **Automated Reselling:** Automatically purchases high‑potential products and posts them for sale on our platform with dynamic pricing.
* **RESTful API:** Exposes endpoints for product listings, price histories, purchase orders, and user management.
* **Frontend Dashboard:** React‑based interface for users to browse trending products, view analytics, and place orders.

---

## Getting Started

### Prerequisites

* Python 3.10+
* Node.js 18+
* PostgreSQL 14+
* Redis 6+ (for caching and queuing)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/algerian-sales-agent.git
   cd algerian-sales-agent
   ```

2. **Backend setup:**

   Create a `.env` file in the `backend` directory. This file will hold your local environment variables. Add the following variables to the file:

   ```
   SECRET_KEY='a-secure-secret-key-for-development'
   DATABASE_URL='sqlite:///db.sqlite3'
   ```

   Now, you can set up the backend:

   ```bash
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend setup:**

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Worker & Scheduler:**

   ```bash
   # In a separate shell
   cd backend
   celery -A project.celery_app worker --loglevel=info
   celery -A project.celery_app beat --loglevel=info
   ```

Your application will now be accessible at `http://localhost:3000` (frontend) and `http://localhost:8000/api/` (backend).

---

## Architecture Overview

See [ARCHITECTURE.md](ARCHITECTURE.md) for a detailed system diagram and component interactions. This document covers:

* Modular microservices for scraping, analytics, and order processing
* Message broker (Celery + Redis) for asynchronous tasks
* API gateway and load balancing strategies

---

## Data Model

For entity definitions and relationships, refer to [DATA\_MODEL.md](DATA_MODEL.md), which describes:

* Product, Sale, Trend, User, and Order schemas
* ER diagrams and indexing strategies

---

## Technology Stack

Refer to [TECHNOLOGY\_STACK.md](TECHNOLOGY_STACK.md) for rationale on selected technologies:

* **Backend:** Django REST Framework, Celery, Redis
* **Frontend:** React, Next.js, Tailwind CSS
* **Database:** PostgreSQL
* **Infrastructure:** Docker, Kubernetes, AWS ECS

---

## UI/UX

The user experience flow and wireframes are documented in [UI\_UX.md](UI_UX.md). Highlights include:

* Intuitive dashboard for monitoring trends
* Real‑time charting of sales data
* Simple checkout and order management

---

## Deployment

Deployment guidelines and CI/CD setup are in [DEPLOYMENT.md](DEPLOYMENT.md):

* Dockerized services with version pinning
* Kubernetes manifests for staging and production
* GitHub Actions workflows for build, test, and deploy

---

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/...`)
3. Commit your changes (`git commit -m "Add ..."`)
4. Push to the branch (`git push origin feature/...`)
5. Open a pull request

Please ensure all new code includes tests and adheres to the existing linting rules.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Happy reselling!*
