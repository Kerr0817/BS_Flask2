from pyecharts.charts import Bar
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_Page():
    bar = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    )
    # print(bar.render_embed())
    # print(bar.dump_options())
    return render_template("pyecharts.html", bar_data=bar.dump_options())


if __name__ == '__main__':
    app.run()
