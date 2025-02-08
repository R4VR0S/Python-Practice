def main():
    books = []
    bname = ""
    bauthor = ""
    byear = 0

    while True:
        try:
            print ("\nWelcome to Rav's Library! Please choose a number.\n"
                "(1) Add a new book\n"
                "(2) List all books\n" 
                "(3) Search for a book title\n" 
                "(4) Remove a book by title\n" 
                "(5) Exit")
            
            choice = int(input("Enter number: \n"))

            if choice == 1:
                books.append(badd(bname, bauthor, byear))
                print(books)

            elif choice == 2:
                blist(books)

            elif choice == 3:
                bsrch(books)
                
            elif choice == 4:
                brem(books)

            elif choice == 5:
                exit()

            else:
                print("\nPlease enter correct number.")

        except NameError:
            print("\nBook not found!")
        except ValueError:
             print("\nEnter a valid choice!")
            
def badd(name, author, year):
       name = input("Name of book: ").strip().lower()
       author = input("Name of author: ").strip()

       while True:
              try:
                     year = input("Year of book: ").strip()
                     if len(year) == 4:
                            if int(year) <= 2025:
                                   
                                   print ("\nSuccessfully added book!")
                                   return ({"name": name, "author": author, "year":int(year)})
                            elif int(year) > 2025:
                                   raise(ValueError)
                     elif int(year) == 1:
                            return
                     else:
                          raise(ValueError)
              except ValueError:
                     print("\nPlease enter correct value for year.\n"
                            "(Enter 1 to go back)\n")
    
def blist(shelf):
     print("Books in the shelf: \n")
     for bs in shelf:
       print (f"1. {bs["name"].title()} by {bs["author"].title()} ({bs["year"]})")

def bsrch(shelf):
     search = input("\nSearch for book: ").strip().lower()
     any = False
     for bs in shelf:
       if bs["name"] == search:
              print ("\nResult found!\n"
              f"\nBook: {bs["name"].title()}\n"
              f"Author: {bs["author"]}\n"
              f"Year: {bs["year"]}")
              any = True
       elif any == False:
              raise(NameError)

def brem(shelf):
     while True:
        try:
            rem = input("\nRemoving a book...\n(Enter '1' to go back)\nEnter book name: ").strip().lower()
            any = False
            for bs in shelf:
                if bs["name"] == rem:
                        any = True
                        while True:
                            try:
                                choice = input("Are you sure you want to remove this book?\nYes or No: ").lower()
                                if choice in ("yes", "y"):
                                        shelf.remove (bs)
                                        print("\nSuccessfully removed book!")
                                        return
                                elif choice in ("no", "n"):
                                        break
                            except(NameError,ValueError):
                                    print("Please enter correct choice")
                elif rem == "1":
                        return
                elif any == False:
                        raise (NameError)
        except NameError:
             print ("Book not found!")
             
             

main()