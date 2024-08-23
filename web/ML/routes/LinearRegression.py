from io import BytesIO
from flask import Blueprint, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = "C:\\Users\\KOSMO\\AppData\\Local\\Microsoft\\Windows\\Fonts\\강원교육모두 Bold.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)



bp = Blueprint('linear', __name__, url_prefix='/linear')

@bp.route('/page1')
def page1():
    return render_template(
        'index.html', title='선형회귀(Linear Regression)', pageName='linear/page1.html'
    )

@bp.route('/result1')
def result1():
    hours = float(request.args['hours'])
    dataset = pd.read_csv('data/LinearRegressionData.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:,-1].values
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(X, y)
    result = reg.predict([[hours]])
    return str(round(result[0], 2))

@bp.route('/page3')
def page3():
    return render_template(
        'index.html', title='다중선형회귀(Multiple Linear Regression)', pageName='linear/page3.html'
    )



