from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Nael Stephanson", 500)
    paper_novel = PrintBook("The Cacher in the Rye", "J.D. Salinger", 234)
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)
    my_library.list_books()
if __name__ == "__main__":
    main()    