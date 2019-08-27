# coding=gb2312
from flask import Flask, render_template, request
from flask import jsonify

# 从falsktools脚本里面导入相应的处理方法，flasktools.py项目文件中。
from WeiboSubproject.flaskwebtools import time_paser, gender_paser, city_paser, topic_paser

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdad"


@app.route('/')
def index():
    '''
        根目录，访问的主页。一个搜索框，
        可以在里面输入一些指定的话题，来转换到指定数据分析路由。
    '''
    return render_template('index.html')


@app.route('/zl', methods=['GET', 'POST'])
def zl():
    '''
        数据总览页面，大体的介绍下数据分布，数据的一些属性。
        起到一个说明书的作用，建立与浏览页面者的信任。
    '''
    if request.method == 'POST':
        return
    else:
        return '<h1>只接受post请求！</h1>'


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/gwy', methods=['GET', 'POST'])
def gwy():
    '''
       路由/gwy 对应的请求为公务员。下面的类推，/tzdn对应同桌的你...
    '''
    a, b = time_paser('公务员')
    c = gender_paser('公务员')
    d = topic_paser('公务员')
    e = city_paser('公务员')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/tzdn', methods=['GET', 'POST'])
def tzdn():
    a, b = time_paser('同桌的你')
    c = gender_paser('同桌的你')
    d = topic_paser('同桌的你')
    e = city_paser('同桌的你')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/xm', methods=['GET', 'POST'])
def xm():
    a, b = time_paser('小米')
    c = gender_paser('小米')
    d = topic_paser('小米')
    e = city_paser('小米')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/hd', methods=['GET', 'POST'])
def hd():
    a, b = time_paser('恒大')
    c = gender_paser('恒大')
    d = topic_paser('恒大')
    e = city_paser('恒大')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/fj', methods=['GET', 'POST'])
def fj():
    a, b = time_paser('房价')
    c = gender_paser('房价')
    d = topic_paser('房价')
    e = city_paser('房价')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/hj', methods=['GET', 'POST'])
def hj():
    a, b = time_paser('韩剧')
    c = gender_paser('韩剧')
    d = topic_paser('韩剧')
    e = city_paser('韩剧')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/lsh', methods=['GET', 'POST'])
def lsh():
    a, b = time_paser('林书豪')
    c = gender_paser('林书豪')
    d = topic_paser('林书豪')
    e = city_paser('林书豪')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/hj1', methods=['GET', 'POST'])
def hj1():
    a, b = time_paser('火箭')
    c = gender_paser('火箭')
    d = topic_paser('火箭')
    e = city_paser('火箭')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/tg', methods=['GET', 'POST'])
def tg():
    a, b = time_paser('贪官')
    c = gender_paser('贪官')
    d = topic_paser('贪官')
    e = city_paser('贪官')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/zjy', methods=['GET', 'POST'])
def zjy():
    a, b = time_paser('转基因')
    c = gender_paser('转基因')
    d = topic_paser('转基因')
    e = city_paser('转基因')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/wm', methods=['GET', 'POST'])
def wm():
    a, b = time_paser('雾霾')
    c = gender_paser('雾霾')
    d = topic_paser('雾霾')
    e = city_paser('雾霾')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


# 接收前端web页面的点击请求，如果是下面路由，返回以下内容
@app.route('/mz', methods=['GET', 'POST'])
def mz():
    a, b = time_paser('魅族')
    c = gender_paser('魅族')
    d = topic_paser('魅族')
    e = city_paser('魅族')
    datas = {

        "data1": {
            "x": a,
            "y": b
        },
        "data2": c,
        "data3": d,
        "data5": e

    }
    return jsonify(datas)


if __name__ == '__main__':
    app.run()
