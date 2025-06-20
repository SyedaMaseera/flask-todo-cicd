from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todos.append(task)
        return redirect(url_for('home'))
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
