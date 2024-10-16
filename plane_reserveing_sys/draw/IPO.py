from graphviz import Digraph

# 创建一个有向图
ipo_dot = Digraph(comment='IPO图')
ipo_dot.attr('node', fontname='SimSun')  # 设置节点字体
ipo_dot.attr('edge', fontname='SimSun')  # 设置边字体

# 添加处理节点
ipo_dot.node('Process', '处理过程')

# 添加输入节点
ipo_dot.node('PassengerInfo', '旅客信息')
ipo_dot.node('FlightInfo', '航班信息')

# 添加输出节点
ipo_dot.node('Ticket', '机票')
ipo_dot.node('Itinerary', '行程单')

# 添加边
# 输入到处理
ipo_dot.edge('PassengerInfo', 'Process', label='旅客信息')
ipo_dot.edge('FlightInfo', 'Process', label='航班信息')

# 处理到输出
ipo_dot.edge('Process', 'Ticket', label='生成机票')
ipo_dot.edge('Process', 'Itinerary', label='生成行程单')

# 绘制IPO图
ipo_dot.render('ipo_diagram.gv', view=True)