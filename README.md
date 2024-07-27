# DripMall Online Shop

DripMall is a modern E-commerec platform built with Django. It provides a user-friendly interface for browsing products, managing shopping carts,processing orders and  direct conversations with sellers.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

DrippMall is a platform where users can:
- Browse products from different range of categories
- Sign-up and log in*
- Add products to the cart.
- Have conversation with the suppilier*
- Process orders 

## Features

- User Authentication (Sign Up, Login, Logout)
- User friendly interface
- Different range of products
- Suppliers for different categories
- Communcate with suppliers
- Process payments 
- Product recommendations
- Notifications for new products*

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/dackMatta/e-commerce.git
    cd e-commerce
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

1. **Browse products**: Browse through products displayed on the landing page.
2. **Add items to the cart**: Add products to your cart.
3. **Update your cart**: Either remove or increase products quantity.
4. **Sign-up or Log-in**: To process your orders sign by either creating an account or log-in.
5. **Process orders and coupons**: Process your orders by  applying coupons.
6. **Select supplier and fill in your location detail**: Select your supplier and fill in your location details.
7. **Message your supplier**: Directly message your supplier allowing room for burgaining and delvery.
8. **Process payments and coupons**: Process your payments with coupons discounts applied.
9. **Process order id**: Receive your order id.
6. **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

Please ensure your code follows our coding standards and includes relevant tests.
Front-end developers help build a user friendly interface

## License

Working on it!.
