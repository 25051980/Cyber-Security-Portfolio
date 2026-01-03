# Online Bookstore Flask Application

## 📚 Academic Project - Software Testing Learning

**⚠️ ACADEMIC USE ONLY - FOR EDUCATIONAL PURPOSES**

## 🛍️ Application Overview

The Online Bookstore is a simple e-commerce web application built with Flask that demonstrates common software patterns and potential testing scenarios.

### Features Implemented

#### 📖 Book Catalog (FR-001)
- Display featured books with details (title, category, price, cover image)
- Browse available inventory
- View book information

#### 🛒 Shopping Cart Functionality (FR-002)
- **Add to Cart**: Add books with specified quantities
- **View Cart**: Display cart contents with quantities and totals
- **Update Cart**: Modify item quantities
- **Remove Items**: Delete items from cart
- **Clear Cart**: Remove all items
- **Dynamic Pricing**: Real-time total calculations

#### 💳 Checkout Process (FR-003)
- Order summary display
- Cart validation (prevent empty cart checkout)
- Total price calculation

## 🏗️ Technical Architecture

### Backend
- **Framework**: Flask (Python web framework)
- **Language**: Python 3.11+
- **Session Management**: Flask sessions for cart persistence
- **Template Engine**: Jinja2 for dynamic HTML rendering

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom styling with responsive design
- **JavaScript**: Form interactions (client-side)

### Project Structure
```
online-bookstore-flask/
│
├── app.py                 # Main Flask application
├── models.py             # Data models (Book, Cart, CartItem)
├── requirements.txt      # Python dependencies
├── README.md            # This documentation
│
├── static/
│   ├── styles.css       # Application styling
│   ├── logo.png         # Store logo
│   └── images/
│       └── books/       # Book cover images
│
└── templates/
    ├── index.html       # Home page template
    ├── cart.html        # Shopping cart page
    └── checkout.html    # Checkout page template
```

## ⚖️ Academic Integrity

This project is provided for educational purposes only. Students should:
- Use this code for learning testing concepts
- Create original test cases and documentation
- Properly cite any external testing frameworks or tools used
- Follow academic honesty policies


**Remember**: The goal is learning! Focus on understanding testing principles and creating thorough, well-documented test cases. Good luck with your software testing journey! 🎓
