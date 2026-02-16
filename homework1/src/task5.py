'''
Arguments: none
Splices a list of books and authors to print specific values
Return: none (print statement)
'''
def Favorite_Books():
    arr = ["The Glass Castle", "Jeannette Walls", "The Kite Runner", "Khaled Hoseinni", "Book 3", "Author 3"]
    fav_books = arr[::2]      # Splices list to only books
    
    # Prints books in list
    counter = 0
    for i in fav_books:
        if(counter < 2):
            print(i + ", ", end="")     # Ensures new line is not included in print with end=""
        else:
            print(i, end="")            # Ensures new line is not included in print with end=""
        counter += 1

'''
Arguments: none
Splices a list of books and authors to print specific values
Return: Dictoinary object
'''
def Student_Database():
    student_database = {"Alice" : 0, "Ben" : 1, "Cameron" : 2}       # Initializes a dictionary {key (string) : value (int)}
    return student_database
