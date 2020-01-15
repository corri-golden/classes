from book import Book
from library import Library


book_one = Book("J.K Rowling", "Harry Potter and the Sorcerer's Stone")  #creates an instance of book class. A type of book.  A type is like an object. 
print(book_one.title, book_one.author)

book_two = Book("J.K Rowling", "Harry Potter and the Chamber of Secress")  #creates an instance of book class. A type of book.  A type is like an object. 
book_one.current_page = 197
print(book_two.title, book_two.author)

nss_library = Library("THE NSS LIBRARY")
print(nss_library.name)

nss_library.add_book(book_one)
nss_library.add_book(book_two)
nss_library.list_books()

book_one.title = "NEW TITLE"
nss_library.list_books()
nss_library.set_address("301 Plus Park Blvd")
print(nss_library.address)

 
# print(f'I am reading {book_one.title} by {book_one.author}')

# book_one.start_reading()

# book_two = Book()  #creates an instance of book class. A type of book.  A type is like an object. 
# book_two.title = "Harry Potter and the Chamber of Secrets"
# book_two.author = "J.K Rowling"
# book_two.current_page = 197
# book_two.start_reading()