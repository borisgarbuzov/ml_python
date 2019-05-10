from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dir1')
def index():
    return render_template('first_app.html')
	
if __name__ == '__main__':
    app.run(debug=True)