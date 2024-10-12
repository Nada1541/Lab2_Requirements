from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        print(f'Name: {name}, Email: {email}')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
