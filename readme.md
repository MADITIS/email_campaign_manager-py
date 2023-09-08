# Email Campaign Manager API Documentation

Welcome to the Email Campaign Manager API documentation. This API allows you to manage subscribers, campaigns, and send daily email campaigns efficiently.

## Table of Contents
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [.env Configuration](#env-configuration)
- [API Routes](#api-routes)
  - [Subscribe to a Campaign](#subscribe-to-a-campaign)
  - [Unsubscribe from a Campaign](#unsubscribe-from-a-campaign)
- [Cron Job](#cron-job)
- [Multithreading](#multithreading)

## Technology Stack

This project is powered by the following technologies:

- ![Django](https://img.shields.io/badge/Django-green)
- ![django-crontab](https://img.shields.io/badge/django--crontab-blue)
- ![python-dotenv](https://img.shields.io/badge/python--dotenv-yellow)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-optional-blue)

## Installation

To set up and use this API, follow these steps:

1. Clone the project repository:

   ```shell
   git clone https://github.com/MADITIS/email_campaign_manager-py.git

   cd email_campaign_manager-py
   ```

```shell
   pip install -r requirements.txt

   python manage.py migrate

   python manage.py createsuperuser


```

## .env Configuration

Set up your environment variables in a `.env` file to configure database credentials and Gmail user password for sending emails. Using PostgreSQL for the database is optional.

### Example .env file:

```env
EMAIL_PASSWORD=your_email_password
EMAIL=your_email@example.com
POSTGRES_PASSWORD=your_postgres_password  # Optional
POSTGRES_USER=your_postgres_user  # Optional
POSTGRES_DB=your_postgres_db  # Optional
POSTGRES_HOST=your_postgres_host  # Optional
POSTGRES_PORT=your_postgres_port  # Optional
```

## API Routes

### Subscribe to a Campaign

- **Endpoint**: `subscribe/<int:campaign_id>/`
- **HTTP Method**: POST
- **Parameters**:
  - `campaign_id` (integer, required): The ID of the campaign to subscribe to.
  - `email` (string, required): The email address of the subscriber.
  - `first_name` (string, required): The first name of the subscriber.

#### Usage

To subscribe to a campaign, make a POST request to the `/api/subscribe/<int:campaign_id>/` endpoint with the required parameters.

Example Request:
```http
POST subscribe/123/
Content-Type: application/json

{
  "email": "john@example.com",
  "first_name": "John"
}


### Unsubscribe from a Campaign

- **Endpoint**: `unsubscribe/<int:campaign_id>/`
- **HTTP Method**: POST
- **Parameters**:
  - `campaign_id` (integer, required): The ID of the campaign to unsubscribe from.
  - `email` (string, required): The email address of the subscriber to unsubscribe.

#### Usage

To unsubscribe from a campaign, make a POST request to the `/api/unsubscribe/<int:campaign_id>/` endpoint with the required parameters.

Example Request:
```http
POST unsubscribe/123/
Content-Type: application/json

{
  "email": "john@example.com"
}

## Cron Job with django-crontab

### Starting the Cron Job

To schedule and start the cron job for sending daily email campaigns, use the following command:

```bash
python manage.py crontab add
python manage.py crontab show
python manage.py runserver

```

## Multithreading

Using Multithreading to send the emails Asynchronously