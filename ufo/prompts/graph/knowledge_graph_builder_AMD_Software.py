import networkx as nx

class KnowledgeGraph:

    def __init__(self):
        # 初始化一个有向图
        self.graph = None
        self.build_graph()

        # 当前所处的节点
        # self.current_node = 'begin'

    # def get_successors(self):
    #     """返回当前节点所有的后继节点"""
    #     if self.current_node is None:
    #         raise ValueError("当前节点未设置。请先使用 set_current_node 设置当前节点。")
    #
    #     return list(self.graph.successors(self.current_node))

    def build_graph(self):
        # 定义节点
        node0 = "begin"
        node1 = '{"Reference_task": "在AMD Settings里查看Vari-Bright level然后关闭AMD Settings。", "Corresponding_application": "AMD Software: Adrenalin Edition"}'
        # node1 = '{"Reference_task": "在AMD Settings里设置Vari-Bright level为2然后关闭AMD Settings。", "Corresponding_application": "AMD Software: Adrenalin Edition"}'
        node2 = '{"Reference_task": "在AMD Settings里查看AMD FreeSync是否支持且启用。", "Corresponding_application": "AMD Software: Adrenalin Edition"}'
        # node2 = '{"Reference_task": "在AMD Settings里启用AMD FreeSync。", "Corresponding_application": "AMD Software: Adrenalin Edition"}'
        node3 = '{"Reference_task": "把该数据键入到结果记录.txt保存并关闭。", "Corresponding_application": "结果记录.txt - Notepad"}'
        # node4 = '{"Reference_task": "在任务管理器里点击启动tab查看上次BIOS所用时间是多少。", "Corresponding_application": "任务管理器"}'
        # node5 = '{"Reference_task": "在任务管理器里点击启动选择xxx并禁用。", "Corresponding_application": "任务管理器"}'
        # node6 = '{"Reference_task": "在任务管理器里点击详细信息右键选择xxx并创建转储文件。", "Corresponding_application": "任务管理器"}'

        #在任务管理器里点击性能tab查看CPU的利用率和速度是多少。把该数据键入到结果记录.txt里。

        node1_1 = '{"ControlText": "Virtual Super Resolution", "Function": "wheel_mouse_input", "Args": {"wheel_dist": -30}, "Action Introduction": "This action will scroll down to show the Vari-Bright Level."}'
        node1_2 = '{"ControlText": "Vari-Bright滑块文本输入", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "CONTINUE"}'
        # node1_2 = '{"ControlText": "Vari-Bright滑块文本输入", "Function": "set_edit_text", "Args": {"text": "2"}, "Status": "CONTINUE"}'
        # node1_3 = '{"ControlText": "Vari-Bright滑块文本输入", "Function": "keyboard_input", "Args": {"keys": "{ENTER}"}, "Status": "CONTINUE"}'
        # node1_4 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node1_3 = '{"Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}a"}, "Status": "CONTINUE", "Action Introduction": "This action will select the Vari-Bright Level value."}'
        node1_4 = '{"Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}c"}, "Action Introduction": "This action will copy the Vari-Bright Level value."}'
        node1_5 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        # node2_1 = '{"ControlText": "最大化", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node2_1 = '{"ControlText": "设置", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node2_2 = '{"ControlText": "显示器", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node2_3 = '{"#th UI after control text ##": 2, "control text ##": "AMD FreeSync Premium", "Function": "texts", "Action Introduction": "This action will return the AMD FreeSync enable state."}'
        # node2_3 = '{"#th UI after control text ##": 1, "control text ##": "AMD FreeSync Premium", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node3_1 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": self.agent.blackboard.trajectories.content[4].Action[0]["Results"]["return_value"][0], "control_focus": True}}'
        node3_2 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": True}}'
        node3_3 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}v"}, "Action Introduction": "This action will paste the Vari-Bright Level value in the notepad."}'
        node3_4 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}s"}, "Action Introduction": "This action will save the notepad."}'
        node3_5 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}w"}, "Action Introduction": "This action will close the notepad."}'

        # 创建有向图
        G = nx.DiGraph()

        # 添加节点
        G.add_node(node0)
        G.add_node(node1)
        G.add_node(node2)
        G.add_node(node3)

        G.add_node(node1_1)
        G.add_node(node1_2)
        G.add_node(node1_3)
        G.add_node(node1_4)
        G.add_node(node1_5)

        G.add_node(node2_1)
        G.add_node(node2_2)
        G.add_node(node2_3)
        # G.add_node(node2_4)


        G.add_node(node3_1)
        G.add_node(node3_2)
        G.add_node(node3_3)
        G.add_node(node3_4)
        G.add_node(node3_5)

        # 添加边
        G.add_edge(node0, node1)
        G.add_edge(node0, node2)
        G.add_edge(node0, node3)
        # G.add_edge(node0, node4)
        # G.add_edge(node0, node5)
        # G.add_edge(node0, node6)

        G.add_edge(node1, node1_1)
        G.add_edge(node1_1, node1_2)
        G.add_edge(node1_2, node1_3)
        G.add_edge(node1_3, node1_4)
        G.add_edge(node1_4, node1_5)

        G.add_edge(node2, node2_1)
        G.add_edge(node2_1, node2_2)
        G.add_edge(node2_2, node2_3)
        # G.add_edge(node2_3, node2_4)

        G.add_edge(node3, node3_1)
        G.add_edge(node3_1, node3_2)
        G.add_edge(node3_2, node3_3)
        G.add_edge(node3_3, node3_4)
        G.add_edge(node3_4, node3_5)

        self.graph = G

        return