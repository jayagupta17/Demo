books = {}
members = {}
flag = 1
while(flag):
    print("1. Book catalog management")
    print("2. Members management")
    print("3. Exit")
    choice = int(input())
    match choice:
        case 1:
            print("1. View catalog")
            print("2. Add book")
            print("3. Update book")
            print("4. Delete book")
            print("5. Search for a book")
            choice1 = int(input())
            match choice1:
                case 1:
                    if(len(books)==0):
                        print("Nothing in the catalog")
                    else:
                        print(books)
                case 2:
                    print("Enter the title of book")
                    name = input()
                    print("Enter the author of book")
                    author = input()
                    print("Enter the genre of book")
                    genre = input()
                    print("Enter the price of book")
                    price = input()
                    books[name] = {"Title": name, "Author": author, "Genre": genre, "Price": price}
                    print("Book added")
                case 3:
                    print("Enter the title of book")
                    name = input()
                    if(name not in books):
                        print("Book not found")
                    else:
                        print("Enter the author of book")
                        author = input()
                        print("Enter the genre of book")
                        genre = input()
                        print("Enter the price of book")
                        price = input()
                        books[name] = {"Title": name, "Author": author, "Genre": genre, "Price": price}
                        print("Book updated")
                case 4:
                    print("Enter the title of book")
                    name = input()
                    if(name not in books):
                        print("Book not found")
                    else:
                        del books[name]
                        print("Book deleted")
                case 5:
                    if(len(books)==0):
                        print("No books in the catalog")
                    else:
                        print("1. Search by title")
                        print("2. Search by author")
                        print("3. Search by genre")
                        choice2 = int(input())
                        match choice2:
                            case 1:
                                print("Enter the title to search")
                                title = input()
                                if(title in books):
                                    print(books[title])
                                else:
                                    print("Book not found")
                            case 2:
                                print("Enter the author to search")
                                author = input()
                                c=0
                                for i in books:
                                    if(books[i]["Author"]==author):
                                        print(books[i])
                                        c+=1
                                if(c==0):
                                    print("No books found by the given author")
                            case 3:
                                print("Enter the genre to search")
                                genre = input()
                                c=0
                                for i in books:
                                    if(books[i]["Genre"]==genre):
                                        print(books[i])
                                        c+=1
                                if(c==0):
                                    print("No books found in given genre")                  
        case 2:
            print("1. Member registration")
            print("2. Update details")
            print("3. View members")
            print("4. Delete member")
            choice1 = int(input())
            match choice1:
                case 1:
                    print("Enter the name")
                    name = input()
                    members[name] = {"Book issued": None, "Fine": 0}
                    print("Member added")
                case 2:
                    print("Enter the name")
                    name = input()
                    if(name not in members):
                        print("Member not found")
                    else:   
                        print("Enter the book issued")
                        book = input()
                        print("Enter the fine amount")
                        fine = int(input())
                    members[name] = {"Book issued": book, "Fine": fine}   
                    print("Details updated")
                case 3:
                    if(len(members)==0):
                        print("Nothing in the catalog")
                    else:
                        print(members)
                case 4:
                    print("Enter the name of member")
                    name = input()
                    if(name not in members):
                        print("Member not found")
                    else:
                        del members[name]
                        print("Member deleted")
        case 3:
            flag = 0
