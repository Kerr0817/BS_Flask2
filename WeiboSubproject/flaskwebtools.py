# coding=gb2312
import pandas as pd

# ��ȡ����Դ�ļ�����������ڴ�ת����pandas��dataframe���ݱ�ṹ
# usecols ����˼��ֻ�ú����б��д��ڵ����ݡ�����ֻ�����ڣ��ȵ㻰�⣬�Ա�ʡ��..
Data = pd.read_csv('WeiboSubproject/data.csv', usecols=['date', 'topic', 'gender', 'location', 'repostsnum'])


def time_paser(kw):
    '''
        ʱ��仯����ͼ
        �����ݱ����ɸѡ ��������������ʱ��仯������㣨x,y��
        ��ʽΪ x=[4/7,4/8,4/9/4/10...]  y=[1000,2000,1000,3000,3000,...]
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
        �û��Ա�ֲ�ͼ
        �����ݱ����ɸѡ ���ز���ָ����һ������Ա�ֲ���
        ��ʽΪ[{'name':'m','value':8000},{'name':'f','value':9000}]
        mָ�������ԣ�fָ����Ů�ԡ�
    '''
    myData = Data[(Data['topic'] == kw)]
    pf = myData.groupby('gender').size()
    res = []
    for k, v in dict(zip([str(i) for i in pf.index], [int(j) for j in pf.values])).items():
        res.append({'name': k, 'value': v})
    return res


def topic_paser(kw):
    '''
        �����������ܻ����е�ռ��
        �����ݱ����ɸѡ ���ص�һָ���������ܻ����е�ռ��
        ��ʽΪ[{'name':'�ȵ㻰��1','value':8000},{'name':'����ȫ������','value':80000}]
        ת������ֵ����ǰ��echarts��ͼ��ʱ����Զ�ת���ɰٷֱ���ʽ��
    '''
    data = Data.groupby('topic').size()
    myData = Data[(Data['topic'] == kw)]
    pf = myData.groupby('topic').size()
    res = [
        {"value": int(pf.values), "name": kw},
        {"value": int(data.sum()) - int(pf.values), "name": '����'},
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
        �����������������ĵ����ֲ�ͼ
        �����ݱ����ɸѡ ���ص�һָ��������������Ⱥ�ĵ����ֲ���
        ��ʽΪ[{'name':'����','value':600},{'name':'�Ͼ�','value':300}.������]
        ��ǰ��echarts��ͼʱ����ͬ��С��value�ڵ�ͼ�ϵ���ɫ��ǳ��ͬ��
        ͨ����ɫ�仯����ֱ�۷��֣��������ۻ������Ⱥ����λ�÷ֲ���
    '''
    myData = Data[(Data['topic'] == kw)]
    myData['location'] = myData['location'].astype(str)
    myData['location'] = myData['location'].apply(lambda x: str(x)[:3])
    myData['location'] = myData['location'].apply(lambda x: remove_whitespace(x))
    myData = myData[(myData['location'] != '����') & (myData['location'] != '����')]
    pf = myData.groupby('location').size()
    res = []
    for k, v in dict(zip([str(i) for i in pf.index], [int(j) for j in pf.values])).items():
        res.append({'name': k, 'value': v})
    # print(res)
    return res
