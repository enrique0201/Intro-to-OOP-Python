class Student:
    def __init__ (self, name, age, grade, height):
            self.name = name
            self.age = age
            self.grade = grade
            self.height = height
    
    def __str__ (self):
          return f'Student: {self.name}'
    

new_student = Student('Calum', 20, 'A',165)
old_student = Student('Dan', 18, 'A', 164)

print(new_student)


class Book:
      def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

      def __str__(self):
        return f'{self.title}by{self.author}'

class Member:
      def __init__(self, name,member_id):
        self.name = name
        self.memeber_id = member_id
        self.borrowed_books = []
     
      def __str__(self):
        return f'Member;{self.name}(ID:{self.member_id})'

class Library:
      def __init__(self):
        self.books=[]
        self.members=[]

      def add_book(self,book):
        self.books.append(book)

      def register_member(self,member):
        self.members.append(member)

      def lend_book(self,book,member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f'{book.title} has been lent to {member.name}')
        else:
            print(f'Sorry,{book.title} is not available for lending')                        

      def return_book(self,book,member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f'{book.title} has been returned by {member.name}')
        else:
            print(f'{member.name}did not borrow {book.title}')  
            
             
book1 = Book('Kiss of the Spider Woman', 'My Brilliant Friend')
book2 = Book('Nosferatu','Labyrinths')

member1 = Member('Enrique',101)
member2 = Member('Sean',102)

library = Library()

library.add_book (book1)
library.add_book(book2)

library.register_member(member1)
library.register_member(member2)

library.lend_book(book1, member1)

library.lend_book(book2, member2)

library.return_book(book1, member1)

library.return_book(book1, member2)












