# coding=gb2312
from flask import Flask, render_template, request
from flask import jsonify

# ��falsktools�ű����浼����Ӧ�Ĵ�������flasktools.py��Ŀ�ļ��С�
from WeiboSubproject.flaskwebtools import time_paser, gender_paser, city_paser, topic_paser

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdad"


@app.route('/')
def index():
    '''
        ��Ŀ¼�����ʵ���ҳ��һ��������
        ��������������һЩָ���Ļ��⣬��ת����ָ�����ݷ���·�ɡ�
    '''
    return render_template('index.html')


@app.route('/zl', methods=['GET', 'POST'])
def zl():
    '''
        ��������ҳ�棬����Ľ��������ݷֲ������ݵ�һЩ���ԡ�
        ��һ��˵��������ã����������ҳ���ߵ����Ρ�
    '''
    if request.method == 'POST':
        return
    else:
        return '<h1>ֻ����post����</h1>'


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/gwy', methods=['GET', 'POST'])
def gwy():
    '''
       ·��/gwy ��Ӧ������Ϊ����Ա����������ƣ�/tzdn��Ӧͬ������...
    '''
    a, b = time_paser('����Ա')
    c = gender_paser('����Ա')
    d = topic_paser('����Ա')
    e = city_paser('����Ա')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/tzdn', methods=['GET', 'POST'])
def tzdn():
    a, b = time_paser('ͬ������')
    c = gender_paser('ͬ������')
    d = topic_paser('ͬ������')
    e = city_paser('ͬ������')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/xm', methods=['GET', 'POST'])
def xm():
    a, b = time_paser('С��')
    c = gender_paser('С��')
    d = topic_paser('С��')
    e = city_paser('С��')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/hd', methods=['GET', 'POST'])
def hd():
    a, b = time_paser('���')
    c = gender_paser('���')
    d = topic_paser('���')
    e = city_paser('���')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/fj', methods=['GET', 'POST'])
def fj():
    a, b = time_paser('����')
    c = gender_paser('����')
    d = topic_paser('����')
    e = city_paser('����')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/hj', methods=['GET', 'POST'])
def hj():
    a, b = time_paser('����')
    c = gender_paser('����')
    d = topic_paser('����')
    e = city_paser('����')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/lsh', methods=['GET', 'POST'])
def lsh():
    a, b = time_paser('�����')
    c = gender_paser('�����')
    d = topic_paser('�����')
    e = city_paser('�����')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/hj1', methods=['GET', 'POST'])
def hj1():
    a, b = time_paser('���')
    c = gender_paser('���')
    d = topic_paser('���')
    e = city_paser('���')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/tg', methods=['GET', 'POST'])
def tg():
    a, b = time_paser('̰��')
    c = gender_paser('̰��')
    d = topic_paser('̰��')
    e = city_paser('̰��')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/zjy', methods=['GET', 'POST'])
def zjy():
    a, b = time_paser('ת����')
    c = gender_paser('ת����')
    d = topic_paser('ת����')
    e = city_paser('ת����')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/wm', methods=['GET', 'POST'])
def wm():
    a, b = time_paser('����')
    c = gender_paser('����')
    d = topic_paser('����')
    e = city_paser('����')
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


# ����ǰ��webҳ��ĵ���������������·�ɣ�������������
@app.route('/mz', methods=['GET', 'POST'])
def mz():
    a, b = time_paser('����')
    c = gender_paser('����')
    d = topic_paser('����')
    e = city_paser('����')
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
