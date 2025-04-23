# 🛒 Amazon Clone - Django E-commerce Project

A Django-based Amazon-style e-commerce platform with essential features like user registration, product management, image uploads, and more. Designed for learning full-stack development using Django.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Issues](https://img.shields.io/github/issues/yourusername/amazon-clone-django)
![Stars](https://img.shields.io/github/stars/yourusername/amazon-clone-django)

---

## 📸 Demo


![image](https://github.com/user-attachments/assets/6009850c-4411-4ef7-9a97-dca05129be4d)

![image](https://github.com/user-attachments/assets/86ae70ac-37a1-4638-9ba2-9e1236e5a7b1)


---

## ✅ Features

- 🔐 **User Registration & Login** — Secure authentication using Django's built-in system.
- 📤 **Product Image Upload** — Upload and display images for each product.
- 🛠️ **CRUD Functionality** — Admin can create, update, and delete product listings.
- 🎨 **Responsive UI** — Clean, Bootstrap-styled frontend with easy navigation.

---

## 🛠️ Tech Stack

- Backend: **Python, Django**
- Frontend: **HTML, CSS, Bootstrap**
- Database: **SQLite3** (for development)
- Media Handling: **Django Media Files**
- Authentication: **Django Auth System**

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/amazon-clone-django.git
cd amazon-clone-django

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
