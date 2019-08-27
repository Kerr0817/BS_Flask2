# coding=gb2312
import pandas as pd

# 读取数据源文件，将其读入内存转换成pandas的dataframe数据表结构
# usecols 的意思是只用后面列表中存在的数据。这里只用日期，热点话题，性别，省份..
Data = pd.read_csv('WeiboSubproject/data.csv', usecols=['date', 'topic', 'gender', 'location', 'repostsnum'])


def time_paser(kw):
    '''
        时间变化趋势图
        对数据表进行筛选 返回讨论人数随时间变化的坐标点（x,y）
        格式为 x=[4/7,4/8,4/9/4/10...]  y=[1000,2000,1000,3000,3000,...]
    '''
    myData = Data[(Data['topic'] == kw)]
    myData['date'] = pd.to_datetime(myData['date']).dt.normalize()
    pf = myData.groupby('date').size()
    pf = pf['2014/4/27':'2014/5/16']
    x = [str(i)[:10] for i in pf.index]
    y = [int(j) for j in pf.values]
    # print(x)
    # print(y)
    return x, y


def gender_paser(kw):
    '''
        用户性别分布图
        对数据表进行筛选 返回参与指定单一话题的性别分布。
        格式为[{'name':'m','value':8000},{'name':'f','value':9000}]
        m指的是男性，f指的是女性。
    '''
    myData = Data[(Data['topic'] == kw)]
    pf = myData.groupby('gender').size()
    res = []
    for k, v in dict(zip([str(i) for i in pf.index], [int(j) for j in pf.values])).items():
        res.append({'name': k, 'value': v})
    return res


def topic_paser(kw):
    '''
        单个话题在总话题中的占比
        对数据表进行筛选 返回单一指定话题在总话题中的占比
        格式为[{'name':'热点话题1','value':8000},{'name':'其他全部话题','value':80000}]
        转换的数值，由前端echarts绘图的时候会自动转化成百分比形式。
    '''
    data = Data.groupby('topic').size()
    myData = Data[(Data['topic'] == kw)]
    pf = myData.groupby('topic').size()
    res = [
        {"value": int(pf.values), "name": kw},
        {"value": int(data.sum()) - int(pf.values), "name": '其他'},
    ]

    return res


def remove_whitespace(x):
    """
    Helper function to remove any blank space from a string
    x: a string
    """
    try:
        # Remove spaces inside of the string
        x = "".join(x.split(' '))

    except:
        pass
    return x


def city_paser(kw):
    '''
        单个话题讨论人数的地区分布图
        对数据表进行筛选 返回单一指定话题中讨论人群的地区分布。
        格式为[{'name':'北京','value':600},{'name':'南京','value':300}.。。。]
        在前端echarts绘图时，不同大小的value在地图上的颜色深浅不同，
        通过颜色变化可以直观发现，参与讨论话题的人群地理位置分布。
    '''
    myData = Data[(Data['topic'] == kw)]
    myData['location'] = myData['location'].astype(str)
    myData['location'] = myData['location'].apply(lambda x: str(x)[:3])
    myData['location'] = myData['location'].apply(lambda x: remove_whitespace(x))
    myData = myData[(myData['location'] != '其他') & (myData['location'] != '海外')]
    pf = myData.groupby('location').size()
    res = []
    for k, v in dict(zip([str(i) for i in pf.index], [int(j) for j in pf.values])).items():
        res.append({'name': k, 'value': v})
    # print(res)
    return res
