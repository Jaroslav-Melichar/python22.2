from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        with open('results/all.txt', 'a') as f:
            f.write(f'User data: {user_data}\n')
    return render_template('add_user.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_data = request.form.to_dict()
        with open('results/all.txt', 'a') as f:
            f.write(f'Book data: {book_data}\n')
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)