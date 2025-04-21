# 📚 Library Management System (Python CLI)

A simple, menu-driven **command-line application** in Python that demonstrates **Object-Oriented Programming (OOP)** concepts like encapsulation, inheritance, class methods, and error handling.

---

## 🚀 Features

- ✅ View all available books in the library  
- 📥 Borrow a book (if available)  
- 📤 Return a borrowed book  
- ⚠️ Handles errors like:
  - Invalid Book ID
  - Borrowing already borrowed books
  - Returning a book that hasn't been borrowed  

---

## 🧱 Class Structure

### 🏛️ `Library` Class
- **Class Attributes:**
  - `__book_list` – A private list storing all book objects
- **Class Methods:**
  - `entry_book(book)` – Adds a book to the list
  - `view_all_books()` – Displays all available books
  - `find_book_by_id(id)` – Finds a book by its ID



---
