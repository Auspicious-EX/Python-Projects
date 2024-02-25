import tkinter as tk

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def display_books(self):
        if self.no_of_books == 0:
            return "No books available in the library."
        else:
            return "Books available in the library:\n" + "\n".join(self.books)
 
    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
        return f"Book '{book}' added successfully."

    def get_no_of_books(self):
        return self.no_of_books

def add_book_to_library():
    book_name = book_entry.get()
    if book_name:
        result.set(library.add_book(book_name))
        no_of_books.set(library.get_no_of_books())
        books_display.set(library.display_books())
    else:
        result.set("Please enter a valid book name.")

# Create main window
root = tk.Tk()
root.title("Library Management System")

# Create labels and entry fields
book_label = tk.Label(root, text="Enter the name of the book:")
book_label.grid(row=0, column=0, padx=10, pady=10)

book_entry = tk.Entry(root, width=30)
book_entry.grid(row=0, column=1, padx=10, pady=10)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 12))
result_label.grid(row=1, columnspan=2, padx=10, pady=5)

no_of_books = tk.IntVar()
no_of_books_label = tk.Label(root, textvariable=no_of_books, font=("Helvetica", 12))
no_of_books_label.grid(row=2, columnspan=2, padx=10, pady=5)

books_display = tk.StringVar()
books_display_label = tk.Label(root, textvariable=books_display, font=("Helvetica", 12))
books_display_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Create add book button
add_button = tk.Button(root, text="Add Book", command=add_book_to_library)
add_button.grid(row=0, column=2, padx=10, pady=10)

# Creating a library
library = Library()

# Initial display of the number of books
no_of_books.set(library.get_no_of_books())
books_display.set(library.display_books())

root.mainloop()
