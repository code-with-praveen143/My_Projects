from flask import Flask, jsonify, request
import os

app = Flask(__name__)

port = int(os.environ.get("PORT",3000))
books = [
    {'id': 1, 'title': 'Romeo Juliet', 'author': 'Praveen'},
    {'id': 2, 'title': 'Dark Rider', 'author': 'Raghu'},
]
@app.route('/')
def home():
    return "<h1>Welcome to REST API Course Using FLASK"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': request.json['id'],
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message': 'Book deleted'})
    return jsonify({'error': 'Book not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
