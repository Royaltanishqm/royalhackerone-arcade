<div align="center">

# 🕹️ HackerOne Arcade

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*A modular CLI arcade engine backed by relational MySQL authentication.*

</div>

A Python terminal-based arcade game system featuring persistent user authentication backed by MySQL / XAMPP.

---

## 🚀 Features

- **Authentication System:** User Registration and Login integrated with MySQL.
- **Mini-Games Included:**
  - 🪙 **Head / Tail:** Classic coin flip guess.
  - 🎯 **Number Guessing:** Pick a random integer from 1 to 5.
  - 🎰 **Roll Game:** 3-slot fruit reel spinner.

---

## 🛠️ Prerequisites

1. **Python 3.8+** installed on your system.
2. **XAMPP** (or a local MySQL service running on port 3306).

---

## ⚙️ Installation & Setup

### 1. Configure the Database
1. Launch **XAMPP** and start the **MySQL** module.
2. Open [phpMyAdmin](http://localhost/phpmyadmin).
3. Create a new database named:
   ```sql
   royalhackerone