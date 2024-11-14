const fs = require('fs');

// Read the JSON file
fs.readFile('books.json', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the JSON data
  const bookData = JSON.parse(data);

  // Access and print the information of all books
  bookData.books.forEach((book, index) => {
    console.log(`Book ${index + 1}:`);
    console.log("Title:", book.title);
    console.log("Author:", book.author);
    console.log("Publication Year:", book.publicationYear);
    console.log("Genres:", book.genres.join(", "));
    console.log("---------------------------");
  });
});
