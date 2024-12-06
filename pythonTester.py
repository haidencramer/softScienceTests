import unittest
from classCode import Library, Calculator

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Initialize a library instance for all tests
        self.library = Library()

    def test_add_and_display_books(self):
        # Test adding and displaying books
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 3)
        self.library.add_book("1984", "George Orwell", 2)
        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0].title, "The Great Gatsby")
        self.assertEqual(self.library.books[1].copies, 2)

    def test_add_and_display_members(self):
        # Test adding and displaying members
        self.library.add_member("Alice")
        self.library.add_member("Bob")
        self.assertEqual(len(self.library.members), 2)
        self.assertEqual(self.library.members[0].name, "Alice")
        self.assertEqual(self.library.members[1].name, "Bob")

    def test_borrow_book_success(self):
        # Test borrowing a book successfully
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1)
        self.library.add_member("Alice")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)
        self.assertEqual(self.library.books[0].copies, 0)
        self.assertEqual(len(self.library.members[0].borrowed_books), 1)

    def test_borrow_book_no_copies(self):
        # Test borrowing when no copies are available
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 0)
        self.library.add_member("Alice")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)
        self.assertEqual(len(self.library.members[0].borrowed_books), 0)

    def test_borrow_book_limit_reached(self):
        # Test borrowing limit
        self.library.add_book("Book1", "Author1", 1)
        self.library.add_book("Book2", "Author2", 1)
        self.library.add_book("Book3", "Author3", 1)
        self.library.add_book("Book4", "Author4", 1)
        self.library.add_member("Alice")
        member_id = self.library.members[0].member_id
        for i in range(3):
            book_id = self.library.books[i].book_id
            self.library.borrow_book(member_id, book_id)
        # Try borrowing a fourth book
        self.library.borrow_book(member_id, self.library.books[3].book_id)
        self.assertEqual(len(self.library.members[0].borrowed_books), 3)

    def test_return_book_success(self):
        # Test returning a borrowed book successfully
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1)
        self.library.add_member("Alice")
        book_id = self.library.books[0].book_id
        member_id = self.library.members[0].member_id
        self.library.borrow_book(member_id, book_id)
        self.library.return_book(member_id, book_id)
        self.assertEqual(self.library.books[0].copies, 1)
        self.assertEqual(len(self.library.members[0].borrowed_books), 0)

    def test_return_book_not_borrowed(self):
        # Test returning a book that wasn't borrowed
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1)
        self.library.add_member("Alice")
        member_id = self.library.members[0].member_id
        self.library.return_book(member_id, "InvalidBookID")
        self.assertEqual(self.library.books[0].copies, 1)

    def test_find_book(self):
        # Test finding a book
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1)
        book_id = self.library.books[0].book_id
        book = self.library.find_book(book_id)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "The Great Gatsby")

    def test_find_member(self):
        # Test finding a member
        self.library.add_member("Alice")
        member_id = self.library.members[0].member_id
        member = self.library.find_member(member_id)
        self.assertIsNotNone(member)
        self.assertEqual(member.name, "Alice")

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Initialize a Calculator instance for all tests
        self.library = Calculator()



    
if __name__ == '__main__':
    unittest.main()
