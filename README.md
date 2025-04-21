📚 Library Management System (Python CLI)
This is a menu-driven Python application that simulates a simple Library Management System using the principles of Object-Oriented Programming (OOP) such as:

Class & Instance Attributes

Encapsulation (using protected/private members)

Class Methods

Exception Handling

🚀 Features
View all available books in the library

Borrow a book by its ID (if available)

Return a borrowed book

Handles errors such as:

Invalid book ID

Borrowing an already borrowed book

Returning a book that hasn't been borrowed

🧱 Class Structure
Library Class
Class Attribute: __book_list (Private list of all book objects)

entry_book(book): Adds a new book to the list

view_all_books(): Displays all books

find_book_by_id(book_id): Returns a book object by ID

Book Class (Inherits from Library)
Attributes:

_book_id (int)

_book_title (str)

_book_author (str)

_book_availability (bool)

Methods:

borrow_book(): Sets availability to False

return_book(): Sets availability to True

view_book_info(): Prints book details
