from flask import Flask, render_template
from routes import LinearRegression

app = Flask(__name__, template_folder='templates') #templates 생략가능

app.register_blueprint(LinearRegression.bp)


@app.route('/')
def index():
    return render_template('index.html', title="홈페이지", pageName="home.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)