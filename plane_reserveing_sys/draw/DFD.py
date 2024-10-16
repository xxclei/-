from graphviz import Digraph

def draw_dfd():
    dot = Digraph(comment='机票预订系统数据流图', format='png')

    # 设置字体
    dot.attr('node', fontname='SimSun')
    dot.attr('edge', fontname='SimSun')

    # 定义外部实体（正方形）
    dot.node('A', '旅客', shape='square', style='filled', fillcolor='lightgrey')
    dot.node('B', '旅行社', shape='square', style='filled', fillcolor='lightgrey')
    dot.node('C', '航空公司', shape='square', style='filled', fillcolor='lightgrey')

    # 定义数据存储（两条平行线）
    dot.node('DS1', '旅客信息库', shape='cds', style='filled', fillcolor='lightgrey')
    dot.node('DS2', '航班信息库', shape='cds', style='filled', fillcolor='lightgrey')
    dot.node('DS3', '财务记录库', shape='cds', style='filled', fillcolor='lightgrey')

    # 定义加工过程（圆角矩形）
    dot.node('P1', '预定处理', shape='rect', style='filled,rounded', fillcolor='lightblue')
    dot.node('P2', '机票发放', shape='rect', style='filled,rounded', fillcolor='lightblue')
    dot.node('P3', '延误处理', shape='rect', style='filled,rounded', fillcolor='lightblue')
    dot.node('P4', '班机取消处理', shape='rect', style='filled,rounded', fillcolor='lightblue')
    dot.node('P5', '更改班次处理', shape='rect', style='filled,rounded', fillcolor='lightblue')
    dot.node('P6', '查询统计', shape='rect', style='filled,rounded', fillcolor='lightblue')

    # 定义数据流
    dot.edge('B', 'P1', label='旅客信息')
    dot.edge('P1', 'DS1', label='更新信息')
    dot.edge('DS1', 'P1', label='查询信息')
    dot.edge('P1', 'DS2', label='查询航班')
    dot.edge('DS2', 'P1', label='航班详情')
    dot.edge('P1', 'P2', label='发放机票')
    dot.edge('P2', 'DS3', label='收款记录')
    dot.edge('DS3', 'P2', label='支付验证')
    dot.edge('A', 'P3', label='延误通知')
    dot.edge('P3', 'DS1', label='更新状态')
    dot.edge('A', 'P4', label='取消')
    dot.edge('P4', 'DS1', label='取消请求')
    dot.edge('A', 'P5', label='更改请求')
    dot.edge('P5', 'DS1', label='更改确认')
    dot.edge('C', 'P6', label='请求统计')
    dot.edge('P6', 'DS2', label='航班载客情况')
    dot.edge('P6', 'C', label='统计报告')

    # 渲染图形
    dot.render('机票预订系统DFD', view=True)

draw_dfd()