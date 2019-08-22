from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__, static_folder="templates")


def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["一室", "二室", "三室", "四室", "五室", "六室", "七室", "八室", "十室", "十一室", "十三室", "十五室"])
        .add_yaxis("人数", [5, 20, 36, 10, 75, 90, 5, 20, 36, 10, 75, 90])
        .add_yaxis("评分", [15, 25, 16, 55, 48, 8, 5, 20, 36, 10, 75, 90])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c


@app.route("/")
def index():
    c = bar_base()
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run()
