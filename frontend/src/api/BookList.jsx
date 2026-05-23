import React  from "react";
import { useState, useEffect } from "react";
import  axios  from 'axios';

function Books() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/api")
            .then(response => setBooks(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Book List </h1>
            <ul>
                {books.map(book => (
                    <li key={book.id}>
                        {book.book_title}: {book.author}
                    </li>
                ))}
            </ul>
        </div>
    );
}
export default Books;



