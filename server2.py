from flask import Flask, render_template
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
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="1024px", height="640px"))
        .add_xaxis(["一室", "二室", "三室", "四室", "五室", "六室", "七室", "八室", "十室", "十一室", "十三室", "十五室"])
        .add_yaxis("人数", [randrange(0, 100) for _ in range(12)])
        .add_yaxis("评分", [randrange(0, 100) for _ in range(12)])
        .add_yaxis("月评分",[randrange(0, 100) for _ in range(12)])
        .add_yaxis("年评分", [randrange(0, 100) for _ in range(12)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar图", subtitle="研究室月度评分"))
    )
    return c


@app.route("/")
def index():
    c = bar_base()
    print('IGUO server is connecting')
#    return Markup(c.render_embed()) 跑templates里的html
#    return c.dump_options_with_quotes()  # 返回json字符
    c.render("templates/my.html")  # 生成html在tempaltes里
    return render_template("my.html")  # 驱动templates里的html


if __name__ == "__main__":
    app.run()
