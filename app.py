from flask import Flask
from flask import jsonify, make_response
from flask import request

app = Flask("the-box-library")

books =[
{
   'name' : 'Across the bridge',
   'author' : 'JK vim',
   'category' : 'comics',
   'id' : "ac657"
}
]

@app.route('/api/category/books', methods=['GET', 'POST'])
def book_api():
    if request.method == 'GET':
        return jsonify(books)
        resp = jsonify(books)
    else
       name = request.values.get('name', None)
       author = request.values.get('author', None)
       category = request.values.get('category', None)
       id = request.values.get('id', None)

       new_book = {
          'name' : name,
          'author' : author,
          'category' : category,
          'id' : id
       }
       books.append(new_book)
      resp = jsonify({'OK' : 'Book Added'})

     return resp

if __name__ == '__main__':
    app.run()
