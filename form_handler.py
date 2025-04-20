from flask import Flask, request, render_template

app = Flask(__name__)  # Define Flask app FIRST

@app.route('/')
def form():
    return render_template('CompletionForm.html')  

@app.route('/page/<page_name>')
def render_page(page_name):
    
   return render_template(f'{page_name}.html')
    

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    return f"Form received! Hello, {username} {password}!"


@app.route('/user/<username>/<middle>', methods= ['GET'])
def getUserDetails( middle, username):
    return(f"Great work {username} your middle name is {middle}")

if __name__ == '__main__':
    app.run(debug=True)
