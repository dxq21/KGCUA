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
        node1 = '{"Reference_task": "在DSAT里点击FreeSync查看FreeSync是否support。", "Corresponding_application_contain": "DSAT"}'
        # node1 = '{"Reference_task": "在DSAT里点击FreeSync选择Aoto Sweep然后开始扫描。"}'
        # node2 = '{"Reference_task": "在任务管理器里点击性能tab查看xxx的xxx是多少。", "Corresponding_application": "任务管理器"}'
        node2 = '{"Reference_task": "把该数据键入到结果记录.txt里。", "Corresponding_application": "结果记录.txt - Notepad"}'
        node3 = '{"Reference_task": "在DSAT里点击DMCU选择LEN设置AutoRefresh并打开Log Window。", "Corresponding_application_contain": "DSAT"}'
        node4 = '{"Reference_task": "记录PSR status log。", "Corresponding_application": "PSR Status Log"}'
        # node5 = '{"Reference_task": "在任务管理器里点击启动选择xxx并禁用。", "Corresponding_application": "任务管理器"}'
        # node6 = '{"Reference_task": "在任务管理器里点击详细信息右键选择xxx并创建转储文件。", "Corresponding_application": "任务管理器"}'

        #在任务管理器里点击性能tab查看CPU的利用率和速度是多少。把该数据键入到结果记录.txt里。

        node1_1 = '{"ControlText": "FreeSync", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node1_2 = '{"#th UI after control text ##": 2, "control text ##": "local system", "Function": "click_input", "Args": {"button": "left", "double": False}, "node_index": 1}'
        # node1_2 = '{"ControlText": "Virtual Super Resolution", "Function": "wheel_mouse_input", "Args": {"wheel_dist": -30}, "Action Introduction": "This action will scroll down to show the Vari-Bright Level."}'
        node1_3 = '{"ControlText_Contain": "FreeSync is", "Function": "texts"}'
        node1_4 = '{"ControlText_contain_list": ["Close","关闭"], "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node1_4 = '{"ControlLabel": "37", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node1_5 = '{"ControlLabel": "27", "Function": "texts"}'
        # node1_6 = '{"ControlLabel": "27", "Function": "texts"}'
        # node1_7 = '{"ControlLabel": "27", "Function": "texts"}'
        # node1_5 = '{"Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}c"}, "Action Introduction": "This action will copy the Vari-Bright Level value."}'

        # node2_1 = '{"ControlText": "性能", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # # node2_2 = '{"ControlText_Contain": "CPU", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node2_2_1 = '{"#th UI after control text ##": 2, "control text ##": "服务", "Function": "texts", "Action Introduction": "This action will return the CPU utilization and record it in blackboard."}'
        # node2_2_2 = '{"#th UI after control text ##": 3, "control text ##": "服务", "Function": "texts", "Action Introduction": "This action will return the CPU speed and record it in blackboard."}'
        # # node2_3 = '{"ControlText": "GPU 1", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node2_3_1 = '{"#th UI after control text ##": 2, "control text ##": "GPU 1", "Function": "texts",  "Action Introduction": "This action will return the GPU utilization and record it in blackboard."}'
        # # node2_4 = '{"ControlLabel": "3", "Function": "no_action"}'
        # # node2_5 = '{"ControlLabel": "3", "Function": "texts"}'
        # # node2_5 = '{"ControlLabel": "3", "Function": "no_action"}'

        # node2_1 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}v"}, "Action Introduction": "This action will paste the Vari-Bright Level value in the notepad."}'
        node2_1 = '{"ControlText_contain_list": ["Text Editor","文本编辑器"], "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}v"}}'
        # node2_2 = '{"ControlText": "Text Editor", "Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": True}}'
        node2_2 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": self.agent.blackboard.trajectories.content[3].Action[0]["Results"]["return_value"][0], "control_focus": True}}'
        node2_3 = '{"ControlText": "Text Editor", "Function": "keyboard_input", "Args": {"keys": self.agent.blackboard.trajectories.content[3].Action[0]["Results"]["return_value"][0], "control_focus": True}}'
        # self.agent.blackboard.trajectories.content[3].Action[0]['Results']['return_value'][0]
        node2_4 = '{"ControlText": "Text Editor", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}s"}, "Action Introduction": "This action will save the notepad."}'
        node2_5 = '{"ControlText": "Text Editor", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}w"}, "Action Introduction": "This action will close the notepad."}'
        # node2_2 = '{"ControlText": "Text Editor", "Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": True}}'
        # node2_3 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": self.agent.blackboard.trajectories.content[6].Action[0]["Results"]["return_value"][0], "control_focus": True}}'
        # node2_4 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": True}}'
        # node2_5 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": self.agent.blackboard.trajectories.content[7].Action[0]["Results"]["return_value"][0], "control_focus": True}}'

        node3_1 = '{"ControlText": "DMCU", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node3_2 = '{"#th UI after control text ##": 2, "control text ##": "local system", "Function": "click_input", "Args": {"button": "left", "double": False}, "node_index": 3}'
        node3_3 = '{"#th UI after control text ##": 2, "control text ##": "PSR Escape Status", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node3_4 = '{"#th UI after control text ##": 3, "control text ##": "PSR Escape Status", "Function": "set_edit_text", "Args":{"text": "444"}}'
        node3_5 = '{"ControlText": "Show Log Window", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        'PSR Escape Status'

        node4_1 = '{"ControlLabel": "2", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node4_2 = '{"ControlLabel": "2", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}a"}}'
        node4_3 = '{"ControlLabel": "2", "Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}c"}}'
        node4_4 = '{"ControlText_contain_list": ["Close","关闭"], "Function": "click_input", "Args": {"button": "left", "double": False}}'
        #
        # node5_1 = '{"ControlText": "启动", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node5_2 = '{"Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node5_3 = '{"ControlText": "禁用(A)", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        #
        # node6_1 = '{"ControlText": "详细信息", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node6_2 = '{"Function": "click_input", "Args": {"button": "right", "double": False}}'
        # node6_3 = '{"ControlText": "创建转储文件(C)", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        # node1_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}f"}}'
        # node1_2 = '{"ControlText": "搜索文档", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node1_3 = '{"ControlText": "下一个结果", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node1_4 = '{"ControlText": "关闭窗格", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node1_5 = '{"Function": "keyboard_input", "Args": {"keys": "{RIGHT}", "control_focus": "False"}}'
        # node1_6 = '{"Function": "keyboard_input", "Args": {"keys": "xx", "control_focus": "False"}}'

        # node2_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}h"}}'
        # node2_2 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}a"}}'

        # node3_1 = '{"ControlText": "查找内容(N):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node3_2 = '{"ControlText": "替换为(I):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node3_3 = '{"ControlText": "查找下一处(F)", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node3_4 = '{"ControlText": "替换(R)", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node3_5 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        #
        # node4_1 = '{"ControlText": "“文件”选项卡", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node4_2 = '{"ControlText": "新建", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node4_3 = '{"ControlText": "空白文档", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        #
        # node5_1 = '{"ControlText": "开始", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node5_2 = '{"ControlText": "字体", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node5_3 = '{"Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": "False"}}'

        # # node6_1 = '{"ControlText": "查找内容(N):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # # node6_2 = '{"ControlText": "替换为(I):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node6_1 = '{"ControlText": "查找内容(N):", "Function": "set_find_what_and_its_format", "Args":{"查找内容": "xx", "中文字体": "xx"}}'
        # node6_2 = '{"ControlText": "替换为(I):", "Function": "set_replace_with_and_its_format", "Args":{"替换为": "xx", "中文字体": "xx"}}'
        # # node6_3 = '{"ControlText": "更多(M) >>", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # # node6_4 = '{"ControlText": "格式", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # # node6_5 = '{"Function": "keyboard_input", "Args": {"keys": "f"}}'
        # # node6_6 = '{"ControlText": "中文字体(T):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # # node6_7 = '{"ControlText": "西文字体(F):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # # node6_8 = '{"ControlText": "字形(Y):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # # node6_9 = '{"ControlText": "字号(S):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # # node6_10 = '{"ControlText": "确定", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node6_11 = '{"ControlText": "替换(R)", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node6_12 = '{"ControlText": "全部替换(A)", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node6_13 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'
        # node6_14 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": "false"}}'

        # 创建有向图
        G = nx.DiGraph()

        # 添加节点
        G.add_node(node0)
        G.add_node(node1)

        G.add_node(node2)
        G.add_node(node3)
        G.add_node(node4)

        G.add_node(node1_1)
        G.add_node(node1_2)
        G.add_node(node1_3)
        G.add_node(node1_4)
        # G.add_node(node1_5)
        # G.add_node(node1_6)

        G.add_node(node2_1)
        G.add_node(node2_2)
        G.add_node(node2_3)
        G.add_node(node2_4)
        G.add_node(node2_5)

        G.add_node(node3_1)
        G.add_node(node3_2)
        G.add_node(node3_3)
        G.add_node(node3_4)
        G.add_node(node3_5)

        G.add_node(node4_1)
        G.add_node(node4_2)
        G.add_node(node4_3)
        G.add_node(node4_4)

        # 添加边
        G.add_edge(node0, node1)
        G.add_edge(node0, node2)
        G.add_edge(node0, node3)
        G.add_edge(node0, node4)

        G.add_edge(node1, node1_1)
        G.add_edge(node1_1, node1_2)
        G.add_edge(node1_2, node1_3)
        G.add_edge(node1_3, node1_4)
        # G.add_edge(node1_4, node1_5)
        # G.add_edge(node1_5, node1_6)

        G.add_edge(node2, node2_1)
        # G.add_edge(node2_1, node2_2)
        # G.add_edge(node2_2, node2_3)
        G.add_edge(node2_1, node2_4)
        G.add_edge(node2_4, node2_5)

        G.add_edge(node3, node3_1)
        G.add_edge(node3_1, node3_2)
        G.add_edge(node3_2, node3_3)
        G.add_edge(node3_3, node3_4)
        G.add_edge(node3_4, node3_5)

        G.add_edge(node4, node4_1)
        G.add_edge(node4_1, node4_2)
        G.add_edge(node4_2, node4_3)
        G.add_edge(node4_3, node4_4)

        self.graph = G

        return