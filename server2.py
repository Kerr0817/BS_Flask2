from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar
from random import randrange
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType


app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS, width="1080px", height="700px"))
        .add_xaxis(["一室", "二室", "三室", "四室", "五室", "六室", "七室", "八室", "十室", "十一室", "十三室", "十五室"])
        .add_yaxis("人数", [randrange(0, 100) for _ in range(12)])
        .add_yaxis("评分", [randrange(0, 100) for _ in range(12)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-我喔藕我我我我", subtitle="副标题"))
    )
    return c


@app.route("/")
def index():
    c = bar_base()
    print('woooooo就i偶偶')
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
