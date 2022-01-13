from dataclasses import dataclass
import operator


@dataclass(frozen=True, order=True)
class Book:
    title: str
    author: str


books = [
    Book(title="1984", author="George Orwell"),
    Book(title="The Martian Chronicles", author="Ray Bradbury"),
    Book(title="The Hobbit", author="J.R.R. Tolkien"),
    Book(title="Animal Farm", author="George Orwell"),
    Book(title="Fahrenheit 451", author="Ray Bradbury"),
    Book(title="The Lord of the Rings (1-3)", author="J.R.R. Tolkien"),
    Book(title="Harry Potter and the Sorcerer’s Stone", author="J.K. Rowling"),
    Book(title="To Kill a Mockingbird", author="Harper Lee"),
]
