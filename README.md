# 🍽️ VENKY'S Restaurant - Django Project

Welcome to **VENKY'S Restaurant**, a responsive and visually appealing restaurant website built using Django and Tailwind CSS. This project showcases a modern food ordering homepage with dynamic components and static files.

---

## 🚀 Features

- 🏠 **Home Page with Hero Banner**
- 📷 **High-Quality Dish Images**
- 🧑‍🍳 **Chef's Note Section**
- 🧾 **Popular Dishes Section**
- 📱 **Fully Responsive UI (Mobile + Desktop)**
- 🔍 **Search Bar + Profile + Cart Icons**
- 📂 Modular structure using Django Templates and Static Files

---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.3
- **Frontend**: Tailwind CSS
- **Language**: Python 3.12.7
- **Templating**: Django Template Language (DTL)
- **Version Control**: Git + GitHub

---

## 📁 Project Structure

```bash
.
├── core/
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── components/
│   │           ├── navbar.html
│   │           └── footer.html
│   ├── static/
│   │   └── core/
│   │       ├── images/
│   │       │   ├── paneer.png
│   │       │   ├── dish1.png
│   │       │   ├── dish2.png
│   │       │   ├── dish3.png
│   │       │   └── about.png
│   │       └── css/
│   │           └── tailwind_output.css
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
└── README.md
