from flask import Flask, render_template, send_file
from io import BytesIO
from graph import graph1, graph2, graph3
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "C:\\Users\\KOSMO\\AppData\\Local\\Microsoft\\Windows\\Fonts\\강원교육모두 Bold.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

app = Flask(__name__, template_folder='templates') #templates 생략가능

@app.route('/')
def index():
    return render_template('index.html', title="데이터시각화", pageName="home.html")

@app.route('/page1')
def page1():
    df = graph1()
    return df.to_html(classes='table', table_id='tbl1')

@app.route('/page2')
def page2():
    df = graph2()
    return df.to_html(classes='table', table_id='tbl2')

@app.route('/page3')
def page3():
    df = graph3()
    return df.to_html(classes='table', table_id='tbl3')

@app.route('/image1')
def image1():
    df = graph1()
    plt.bar(df['영화'], df['평점'])
    plt.title('국내 관객수 Top8 영화 평점 정보')
    plt.xlabel('영화제목')
    plt.xticks(rotation=45)
    plt.ylabel('평점')

    img = BytesIO()
    plt.savefig(img, format='png', dpi=300)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')
    

@app.route('/image2')
def image2():
    df = graph2()
    df_group = df.groupby('개봉 연도')[['관객 수','평점']].mean()
    plt.plot(df_group.index, df_group['평점'], marker='o', color = '#454')
    plt.xticks([2006, 2012, 2013, 2014, 2015, 2017, 2019])
    plt.ylim(7, 10)

    img = BytesIO()
    plt.savefig(img, format='png', dpi=300)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

@app.route('/image3')
def image3():
    df = graph3()
    fig, ax1 = plt.subplots(figsize=(13, 5))
    fig.suptitle('출생아 수 및 합계출산율')
    ax1.bar(df.index, df['출생아 수'], color='#a1b1c1')
    ax1.set_ylabel('출생아 수 (천 명)')
    ax1.set_ylim(250, 550)
    ax1.set_yticks([300, 400, 500])
    for idx, val in enumerate(df['출생아 수']): ax1.text(idx, val+5, val, ha='center')
    ax2 = ax1.twinx()
    ax2.plot(df.index, df['합계 출산율'], color='#f1a1b1', marker='o', ms=15, lw=2, mec='w', mew=1)
    ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
    ax2.set_ylim(0, 1.5)
    ax2.set_yticks([0, 1])
    for idx, val in enumerate(df['합계 출산율']): ax2.text(idx, val+0.05, val, ha='center')

    img = BytesIO()
    plt.savefig(img, format='png', dpi=300)
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5000, debug=True)


