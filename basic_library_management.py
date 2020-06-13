class Library:
    def __init__(self, book_list, lib_name):
        self.book_list = book_list
        self.lib_name = lib_name
        self.lend_record = {}

    def display_books(self):
        print(f'Welcome to {self.lib_name} Library!!!!')
        for book in self.book_list:
            print(book)

    def lend_book(self):

        book_name = input("Enter the book: ")
        if book_name in self.book_list:
            if book_name not in self.lend_record:
                print("You Can Have the book")
                cust_name = input("Enter Name: ")
                self.lend_record[book_name] = cust_name
            else:
                print(f'The is already taken by {self.lend_record[book_name]}')
        else:
            print("SORRY!!!!...Book is not Available")

    def donate_book(self):
        give_book = input("Enter the book u want to donate: ")
        self.book_list.append(give_book)
        print("Thank You For Your Kind Gesture!!!")

    def return_book(self):
        book = input("Enter the book You want to Return: ")
        self.lend_record.pop(book)
        print("Book has been returned Successfully")

# move this code in main block to manually enter the books


'''books_list = []
for book in range(3):
    add_book = input("Enter: ")
    books_list.append(add_book)
name = input("Enter Name: ")'''
if __name__ == '__main__':

    bk_list = ['Jungle Book', 'Harry Potter', 'Jumanji']

    my_lib = Library(bk_list, 'Rohit')
    while True:
        print("""
Press 1 to Display all the Available Books
Press 2 to lend a Book
Press 3 to Donate a Book
Press 4 to Return a Book
""")
        choice = int(input("Enter Your choice: "))
        if choice == 1:
            my_lib.display_books()
        elif choice == 2:
            my_lib.lend_book()
        elif choice == 3:
            my_lib.donate_book()
        elif choice == 4:
            my_lib.return_book()
        else:
            print("Wrong Input")
        more = input("Press 'Y' to Continue ").lower()
        if more == 'y':
            continue
        else:
            print("Thank You for using our service...Come Again..")
            exit()
