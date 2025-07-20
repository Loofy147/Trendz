# Deployment Strategy

This document outlines the deployment strategy for the Algerian Sales Agent.

## Cloud Provider

The application will be deployed to **Heroku**. Heroku is a platform as a service (PaaS) that is easy to use and has a free tier that is suitable for small projects.

## Deployment Steps

1.  **Create a Heroku account:** Create a free account on the Heroku website.
2.  **Install the Heroku CLI:** Install the Heroku command-line interface (CLI) on your local machine.
3.  **Create a new Heroku app:** Use the Heroku CLI to create a new app.
4.  **Add a PostgreSQL database:** Add a PostgreSQL database to the Heroku app.
5.  **Set environment variables:** Set the necessary environment variables, such as the database URL and the secret key.
6.  **Create a `Procfile`:** Create a `Procfile` in the root of the project to tell Heroku how to run the application.
7.  **Create a `requirements.txt` file:** Create a `requirements.txt` file to list the Python dependencies.
8.  **Deploy the application:** Use Git to push the application to Heroku.
9.  **Run database migrations:** Use the Heroku CLI to run the database migrations.
10. **Scale the application:** Use the Heroku CLI to scale the application to the desired number of dynos.
