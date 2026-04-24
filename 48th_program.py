import os

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.loadBooks()

    # 📂 Load books from file
    def loadBooks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.books = [line.strip() for line in f.readlines()]

    # 💾 Save books to file
    def saveBooks(self):
        with open(self.filename, "w") as f:
            for book in self.books:
                f.write(book + "\n")

    # ➕ Add Book
    def addBook(self, book):
        self.books.append(book)
        self.saveBooks()
        print("✅ Book added successfully")

    # ❌ Delete Book
    def deleteBook(self, book):
        if book in self.books:
            self.books.remove(book)
            self.saveBooks()
            print("❌ Book deleted")
        else:
            print("⚠️ Book not found")

    # 🔍 Search Book
    def searchBook(self, book):
        if book in self.books:
            print("🔍 Book found")
        else:
            print("❌ Book not found")

    # 📖 Show Books
    def showBooks(self):
        if len(self.books) == 0:
            print("📂 Library is empty")
        else:
            print(f"\n📚 Total Books: {len(self.books)}")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


# 🔥 Menu System (User Interaction)
def main():
    lib = Library()

    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Show Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book = input("Enter book name: ")
            lib.addBook(book)

        elif choice == "2":
            book = input("Enter book name to delete: ")
            lib.deleteBook(book)

        elif choice == "3":
            book = input("Enter book name to search: ")
            lib.searchBook(book)

        elif choice == "4":
            lib.showBooks()

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("⚠️ Invalid choice, try again")


if __name__ == "__main__":
    main()a