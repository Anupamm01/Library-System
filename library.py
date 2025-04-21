class Library:

    __book_list = []

    @classmethod
    def entry_book(cls,book):
        cls.__book_list.append(book)

    @classmethod
    def view_all_books(cls):
        if cls.__book_list:    
            for book in cls.__book_list:
                print(book.view_book_info())
        else:
            print('No Books are available in the book list')

    @classmethod
    def find_book_by_id(cls,id):
        for book in cls.__book_list:
            if book._book_id == id:
                return book
        return None


class Book(Library):

    def __init__(self,book_id,title,author,availability):
        self._book_id = book_id
        self._book_title = title
        self._book_author = author
        self._book_availability = availability

        Library.entry_book(self)

    def borrow_book(self):
        if self._book_availability == True:
            self._book_availability = False
            print(f'You have successfully borrowed \'{self._book_title}\' book')
        else:
            raise Exception (f'Sorry, {self._book_title} is already borrowed')

    def return_book(self):
        if not self._book_availability:
            self._book_availability = True
            print(f'{self._book_title} has been returned and is now available')
        else:
            raise Exception(f'{self._book_title} was not borrowed')


    
    def view_book_info(self):
        print(f'Book_id: {self._book_id}')
        print(f'Title: {self._book_title}')
        print(f'Author: {self._book_author}')
        if self._book_availability:
            print(f'Status: Available')
        else:
            print(f'Status: Not Available')
        

myBook = Book(101,'Deep Work', 'Cal Newport', True)
myBook2 = Book(102,'Atomic Habits', 'James Clear', True)


while True:

    print('-----Library Menu-----')
    print('1. View All Books')
    print('2. Borrow Book')
    print('3. Return Book')
    print('4. Exit')

    choice = int(input('Enter your choice (1-4): '))

    if choice == 1:
        Library.view_all_books()

    elif choice == 2:
        book_id = int(input('Enter Book ID borrow '))
        book = Library.find_book_by_id(book_id)

        if book:
            book.borrow_book()
        else:
            raise ValueError(f'Book ID {book_id} not found!')
        
    elif choice == 3:
        book_id = int(input('Enter Book ID return '))
        book = Library.find_book_by_id(book_id)

        if book:
            book.return_book()
        else:
            raise ValueError(f'Book ID {book_id} not found!')
        
    elif choice == 4:
        print('Exiting from the library system. Goodbye!')
        break
    
    else:
        print('Invalid choice!, please select from 1 to 4')


