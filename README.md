# 💳 ConsoleBank — Terminal-Based Python Banking System

**ConsoleBank** is a modular, menu-driven Python banking app built purely with core Python—designed to help beginners understand backend logic like registration, login, balance tracking, deposits/withdrawals, and transaction history.

---

## 🧩 Project Structure

```bash
ConsoleBank/
├── main.py # Main menu loop and user interaction
├── bank.py # Registration, login, balance check, transactions
├── account.py # Account management (deposit, withdraw, auth)
├── models.py # User model (username, name, balance, etc.)
├── utils.py # Helper functions for validation
├── README.md # Project documentation (this file)
```

---

## 🚀 Features

- 🔐 **User Registration & Login**
  - Unique usernames
  - Password rules (uppercase, lowercase, digit, special character)

- 💰 **Deposits & Withdrawals**
  - Input validation with retry logic
  - Transaction tracking with timestamps

- 📊 **Transaction History**
  - Stores user-wise transactions (runtime only)

- 📞 **Contact & Address Input**
  - Validates 11-digit contact number
  - Ensures address is not empty

---

## 📜 Password Rules

- Length: 8 to 12 characters  
- Must contain:
  - At least 1 uppercase letter  
  - At least 1 lowercase letter  
  - At least 1 digit  
  - At least 1 special character (e.g., `@`, `#`, `!`, etc.)

---

## 🧠 Technologies Used

| Library    | Purpose                           |
|------------|------------------------------------|
| `re`       | Regex validation for password      |
| `datetime` | Timestamping transaction history   |
| Python 3.x | Entire logic implemented in Python |

---

## ▶️ How to Run

# Step 1: Navigate to project directory

```bash
cd ConsoleBank
```

# Step 2: Run the app

```bash
python main.py
```

> 💡 All data is stored in runtime only. Closing the app clears everything.

---

#### 🔧 Fututre Additions
Add JSON or SQLite for data persistence
Add password hashing with hashlib
Convert CLI to Flask app
Export transaction history to CSV

---

### 👩‍💻 Author
Laiba Muzammal
Backend Developer | Python & Flask Enthusiast

---

### 📝 License
MIT License — Free to learn, modify, and share.
