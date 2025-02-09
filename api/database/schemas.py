def individual_serial(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "authors": book["authors"],
        "isbn": book["isbn"],
        "sessions": book["sessions"]
    }

def list_serial(books) -> list:
    return[individual_serial(book) for book in books]