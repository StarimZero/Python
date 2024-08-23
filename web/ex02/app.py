from flask import Flask
from routes import bbs

app = Flask(__name__, template_folder='templates') #templates 생략가능
app.register_blueprint(bbs.bp)

@app.route('/')
def home():
    return "하잉"

if __name__ == '__main__':
    app.run(port=5000, debug=True)