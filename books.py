from fastapi import FastAPI, Body


app = FastAPI()

books = [
    {'title': 'Title One', 'author': 'Author One', 'category' : 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category' : 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category' : 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category' : 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category' : 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category' : 'math'},
]


@app.get("/books")
async def all_books():
    return books


@app.get("/books/{book_title}")
async def read_all_books(book_title : str):
    for book in books:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category : str):
    books_to_return = []
    for book in books:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/by_author/")
async def by_author(author : str):
    books_to_return = []
    for book in books:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_category_by_query(book_author : str, category : str):
    books_to_return = []
    for book in books:
        if book.get("category").casefold() == category.casefold() and book.get("author").casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    books.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        if books[i].get('TiTlE'.casefold()).casefold() == updated_book.get('TiTlE'.casefold()).casefold():
            books[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title : str):
    for i in range(len(books)):
        if books[i].get('title').casefold() == book_title.casefold():
            books.pop(i)
            break


@app.get("/books/by_author/{author}")
async def by_author(author : str):
    books_to_return = []
    for book in books:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
