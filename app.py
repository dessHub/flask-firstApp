from flask import Flask

app = Flask("the-box-library")

@app.route('/api/category/books', methods=['GET', 'POST'])
def book_api():
    return 'some resource'

if __name__ == '__main__':
    app.run()
