from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType
# 随机数生成
from random import randrange
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
# from snapshot_selenium import snapshot # 没网，没下载下来

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
    .add_xaxis(["一室", "二室", "三室", "四室", "五室", "六室", "七室", "八室", "十室", "十一室", "十三室", "十五室"])
    .add_yaxis("人数", [randrange(0, 100) for _ in range(12)])
    .add_yaxis("评分", [randrange(0, 100) for _ in range(12)])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
# bar.render()

bar.render_notebook()
# Note: 在使用 Pandas&Numpy 时，请确保将数值类型转换为 python 原生的 int/float。比如整数类型请确保为 int，而不是 numpy.int32