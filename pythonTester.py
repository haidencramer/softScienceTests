import unittest
from mutant29 import Library, Calculator

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Initialize a library instance for all tests
        self.library = Library()

    def test_add_and_display_books(self):
        # Test adding and displaying books
        self.library.add_book("MrBook", "booksey", 3)
        self.library.add_book("1999", "geoff da lord", 2)

        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0].title, "MrBook")
        self.assertEqual(self.library.books[1].copies, 2)

    def test_add_and_display_members(self):
        # Test adding and displaying members
        self.library.add_member("Tpain")
        self.library.add_member("brudda")

        self.assertEqual(len(self.library.members), 2)
        self.assertEqual(self.library.members[0].name, "Tpain")
        self.assertEqual(self.library.members[1].name, "brudda")

    def test_borrow_book_success(self):
        # Test borrowing a book successfully
        self.library.add_book("MrBook", "booksey", 1)
        self.library.add_member("Tpain")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id

        self.library.borrow_book(member_id, book_id)
        self.assertEqual(self.library.books[0].copies, 0)
        self.assertEqual(len(self.library.members[0].borrowed_books), 1)

    def test_borrow_book_no_copies(self):
        # Test borrowing when no copies are available
        self.library.add_book("MrBook", "booksey", 0)
        self.library.add_member("Tpain")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)

        self.assertEqual(len(self.library.members[0].borrowed_books), 0)

    def test_borrow_book_limit_reached(self):
        # Test borrowing limit
        self.library.add_book("Maze Walker", "John Cena", 1)
        self.library.add_book("Oceans 15", "Mike Vick", 1)
        self.library.add_book("Alice in Nightmare Land", "Harry Mike", 1)
        self.library.add_book("Booby Traps 101", "Clay Jones", 1)
        self.library.add_member("Tpain")
        
        member_id = self.library.members[0].member_id
        for i in range(3):
            book_id = self.library.books[i].book_id
            self.library.borrow_book(member_id, book_id)
        # Try borrowing a fourth book
        self.library.borrow_book(member_id, self.library.books[3].book_id)

        self.assertEqual(len(self.library.members[0].borrowed_books), 3)

    def test_return_book_success(self):
        # Test returning a borrowed book successfully
        self.library.add_book("MrBook", "booksey", 1)
        self.library.add_member("Tpain")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)
        self.library.return_book(member_id, book_id)

        self.assertEqual(self.library.books[0].copies, 1)
        self.assertEqual(len(self.library.members[0].borrowed_books), 0)

    def test_return_book_not_borrowed(self):
        # Test returning a book that wasn't borrowed
        self.library.add_book("MrBook", "booksey", 1)
        self.library.add_member("Tpain")
        member_id = self.library.members[0].member_id
        self.library.return_book(member_id, "InvalidBookID")

        self.assertEqual(self.library.books[0].copies, 1)

    def test_find_book(self):
        # Test finding a book
        self.library.add_book("MrBook", "booksey", 1)
        book_id = self.library.books[0].book_id
        book = self.library.find_book(book_id)

        self.assertIsNotNone(book)
        self.assertEqual(book.title, "MrBook")

    def test_find_member(self):
        # Test finding a member
        self.library.add_member("Tpain")
        member_id = self.library.members[0].member_id
        member = self.library.find_member(member_id)

        self.assertIsNotNone(member)
        self.assertEqual(member.name, "Tpain")

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Initialize a Calculator instance for all tests
        self.calc = Calculator()

    def test_operators(self):
        self.calc.add(10, 15)
        self.calc.subtract(15, 10)
        self.calc.multiply(2, 3)
        self.calc.divide(6, 3)
        self.calc.power(2, 3)
        self.calc.show_history()

        # Add Tests
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertNotEqual(self.calc.add(10, 15), 18)

        self.assertTrue(self.calc.add(10, 15), 25)


        # Subtract Tests
        self.assertEqual(self.calc.subtract(15, 10), 5)
        self.assertNotEqual(self.calc.subtract(10, 15), 18)
        self.assertTrue(self.calc.subtract(15, 10), 5)


        # Multipy Tests
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertNotEqual(self.calc.multiply(2, 3), 28)
        self.assertTrue(self.calc.multiply(2, 3), 6)
   

        # Divide Tests
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertNotEqual(self.calc.divide(6, 3), 5)

        self.assertTrue(self.calc.divide(6, 3), 2)

        # Power Tests
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertNotEqual(self.calc.power(2, 3), 4)

        self.assertTrue(self.calc.power(2, 3), 8)

# def main():
#     file_path = '\Users\benne\Documents\GitHub\softScienceTests\pythonTestor.py'
# with open(file_path, 'r') as file:
#     file_content = file.read()

# print(file_content)

if __name__ == '__main__':
    unittest.main()


