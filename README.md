# SQL Server to PostgreSQL ETL

A lightweight and modular ETL (Extract, Transform, Load) pipeline built with Python. This script extracts data from a Microsoft SQL Server database and loads it into a PostgreSQL database using `pandas` and `SQLAlchemy`.

---

## 🚀 Features

- Extracts data from SQL Server using ODBC
- Loads data into PostgreSQL with auto table creation
- Uses environment variables for secure credentials
- Modular `extract()` and `load()` functions
- Minimal dependencies and easy to extend

---

## 📦 Technologies Used

- Python 3.8+
- Pandas
- SQLAlchemy
- pyodbc
- PostgreSQL
- python-dotenv

---

## 🧪 Prerequisites

- Local or network-accessible SQL Server instance with the `AdventureWorksDW2019` database
- PostgreSQL server with an `AdventureWorks` database
- ODBC Driver 17 for SQL Server installed
- Python environment (recommend using virtualenv)

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```dotenv
PGUID=your_postgres_username
PGPASS=your_postgres_password
