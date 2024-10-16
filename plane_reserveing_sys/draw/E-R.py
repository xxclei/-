from graphviz import Digraph

# 创建一个有向图
dot = Digraph(comment='E-R Diagram')
dot.attr('node', fontname='SimSun')
dot.attr('edge', fontname='SimSun')
# 添加实体节点
entities = [
    '旅客', '旅行社', '航空公司', '预定系统', '航班安排',
    '财务系统', '机票打印', '取票通知和账单', '旅客信息',
    '支付系统', '延误处理', '班机取消处理', '更改班次处理'
]
for entity in entities:
    dot.node(entity, shape='entity')

# 添加关系边
relationships = [
    ('旅客', '预定系统', '进行预定'),
    ('旅行社', '预定系统', '发起预定'),
    ('航空公司', '预定系统', '接收预定'),
    ('预定系统', '航班安排', '安排航班'),
    ('航班安排', '财务系统', '处理付款'),
    ('财务系统', '机票打印', '打印机票'),
    ('预定系统', '取票通知和账单', '生成通知'),
    ('旅客', '旅客信息', '提供信息'),
    ('旅客信息', '支付系统', '进行支付'),
    ('旅客', '延误处理', '报告延误'),
    ('旅客', '班机取消处理', '取消航班'),
    ('旅客', '更改班次处理', '更改班次')
]
for start, end, label in relationships:
    dot.edge(start, end, label=label)

# 绘制E-R图
dot.render('er_diagram.gv', view=True)

