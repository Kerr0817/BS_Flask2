from random import randrange
from flask import Flask, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["一室", "二室", "三室", "四室", "五室", "六室", "七室", "八室", "十室", "十一室", "十三室", "十五室"])
        .add_yaxis("人数", [randrange(0, 100) for _ in range(12)])
        .add_yaxis("评分", [randrange(0, 100) for _ in range(12)])
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    )
    return c

@app.route("/")
def index():
    print('进来了没？？？？')
    return render_template("index.html")

'''
@app.route("/")
def get_bar_chart():
    c = bar_base()
    print('哎。。。。。。。。。。')
    return c.dump_options_with_quotes()
'''

if __name__ == "__main__":
    app.run()
