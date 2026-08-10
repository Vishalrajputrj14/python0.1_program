'''
Write a Library class with no_of_books and books as two instance variables. Write a program to create a libary from this Library 
class and show how you can print all books add a book and get the numbar of books using different methods. show that your program doesnt persist the books after the program 
is stopped.

'''
class Library:
    def __init__(self):
        # instance variables
        self.books = []
        self.no_of_books = 0

    def display_books(self):
        """Display all books in the library"""
        if self.no_of_books == 0:
            print("No books available in the library.")
        else:
            print("Books in Library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

    def add_book(self, book_name):
        """Add a new book to the library"""
        self.books.append(book_name)
        self.no_of_books = len(self.books)
        print(f"Book '{book_name}' added successfully!")

    def get_no_of_books(self):
        """Return the number of books"""
        return self.no_of_books


# ------- Main Program -------
if __name__ == "__main__":
    my_library = Library()

    # Add some books
    my_library.add_book("Python Programming")
    my_library.add_book("Data Structures and Algorithms")
    my_library.add_book("Computer Networks")

    # Display all books
    my_library.display_books()

    # Show total number of books
    print("\nTotal number of books:", my_library.get_no_of_books())

    # Program ends here
    print("\nNow close and rerun the program...")
    print("You will notice that the library list is empty again — data isn't saved permanently.")
