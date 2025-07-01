from data import books as data


def register_book(title: str, author: str) -> bool:
    if not title or not title.strip():
        return False
    if not author or not author.strip():
        return False

    return data.register_book(title.strip(), author.strip())


def get_available_books():
    return data.get_available_books()


def delete_book_if_available(book_id: int) -> bool:
    return data.delete_book_if_available(book_id)