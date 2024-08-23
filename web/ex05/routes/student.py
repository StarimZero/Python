from io import BytesIO
from flask import Blueprint, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_path = "C:\\Users\\KOSMO\\AppData\\Local\\Microsoft\\Windows\\Fonts\\강원교육모두 Bold.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)


bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/search')
def search():
    return render_template(
        'index.html', title='범죄검색', pageName='student/search.html'
    )


def read_data():
    df = pd.read_csv('data/경찰청_범죄 발생 지역별 통계_20221231.csv', encoding='euc-kr')
    return df

@bp.route('/search/data')
def search_data():
    df = read_data()
    args = request.args
    key = args['key']
    word = args['word']
    if word:
        filt = df[key].str.contains(word, na=False)
        df1 = df[filt]
    else:
        df1 = df
    #table = df.to_html(classes='table', table_id='tbl1')
    json = df1.to_json(orient='records')
    return json


def read_student():
    df = pd.read_csv('data/score.csv', index_col='지원번호')
    df['학년'] = [3, 3, 3, 1, 1, 3, 2, 2]
    return df

@bp.route('/info')
def info():
    df = read_student()
    df1 = df.loc[:, ['학교', '이름', '국어', '영어', '수학' ]]
    df1['평균'] = ((df['국어'] + df['영어'] + df['수학'])/3).round(2)
    df2 = df.loc[:, ['학교', '이름', '키', 'SW특기']]
    df3 = df.groupby(['학교', '학년'])[['국어', '영어', '수학']].mean().round(2)
    table1 = df1.to_html(classes='table', table_id='tbl1')
    table2 = df2.to_html(classes='table', table_id='tbl2')
    table3 = df3.to_html(classes='table', table_id='tbl3')
    
    
    return render_template(
        'index.html', title="학생정보", pageName='student/info.html', table1=table1, table2=table2, table3=table3
    )


@bp.route('/graph')
def graph():
        return render_template(
        'index.html', title="학생성적그래프", pageName='student/graph.html'
    )

@bp.route('/graph/image')
def graph_image():
    import numpy as np
    df = read_student()
    index = np.arange(df.shape[0])
    w = 0.25
    plt.figure(figsize=(10, 5))
    plt.title('학생별성적')
    plt.bar(index-w, df['국어'], width=w, label='국어점수')
    plt.bar(index, df['영어'], width=w, label='영어')
    plt.bar(index+w, df['수학'], width=w, label='수학')
    plt.xticks(index, df['이름'], rotation=105)
    plt.legend(ncol=1)
    
    img = BytesIO()
    plt.savefig(img, format='png', dpi=300)
    img.seek(0)
    return send_file(img, mimetype='image/png')
