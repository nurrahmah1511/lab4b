import json

# Open the JSON file
with open('books.json') as file:
    data = json.load(file)

# Access the information of the first book
book = data['books'][0]
title = book['title']
author = book['author']
publication_year = book['publicationYear']
genres = book['genres']

# Print the information for the first book
print("Title:", title)
print("Author:", author)
print("Publication Year:", publication_year)
print("Genres:", ", ".join(genres))

# Optionally, print information for all books
print("\nAll Books Information:")
for index, book in enumerate(data['books'], start=1):
    print(f"Book {index}:")
    print("Title:", book['title'])
    print("Author:", book['author'])
    print("Publication Year:", book['publicationYear'])
    print("Genres:", ", ".join(book['genres']))
    print("---------------------------")
