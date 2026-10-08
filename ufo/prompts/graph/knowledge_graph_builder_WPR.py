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

        with open('读取项目.txt', 'r', encoding='utf-8') as file:
            lines = [line.rstrip('\n') for line in file]
        # 定义节点
        node0 = "begin"
        # node1 = '{"Reference_task": "用explorer打开xxx文件夹, 双击播放xxx，", "Corresponding_application_contain": "文件资源管理器", "Bash": "start explorer \'D:\QD\pycharmproject\issue debug\'", "Status": "ASSIGN"}'
        # node1 = '{"Reference_task": "用explorer打开xxx文件夹, 双击播放xxx，"}'
        # 用explorer打开D:\QD\pycharmproject\issue debug文件夹，播放DMAD.mp4.
        # node1 = '{"Reference_task": "111113242353534，", "Corresponding_application_contain": "文件资源管理器"}'
        node1 = '{"Reference_task": "播放测试视频，用Bash打开WPRUI然后点击Start录制20秒trace,保存后点击OK。", "Corresponding_application_contain": "Windows Performance Recorder"}'
        node2 = '{"Reference_task": "关闭视频。", "Corresponding_application_contain_list": ["播放器","player","Player","movie","Movie"]}'
        # node3 = '{"Reference_task": "在WPA中右键点击屏幕上Series下方Process上方List里audiodg.exe所在位置并选择disable all but selection,观察右侧波形是否具有周期性。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'
        node3 = '{"Reference_task": "在WPA中将CPU Usage加入到Analysis View里，然后打开filter。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'

        # node4 = '{"Reference_task": "打开Edit Filter。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'
        node4 = '{"NodeIndex": "node4", "Reference_task": "在打开的Advanced Settings窗口中, 隐藏Process Name not equal to xxx的trace。", "Corresponding_application": "Advanced Settings"}'
        # node5 = '{"Reference_task": "右键点击保留的trace，然后enable selection,观察截屏上部的波形里的波峰是否稀疏。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'
        node5 = '{"NodeIndex": "node5", "Reference_task": "记录xxx的CPU Usage占比，然后打开filter。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'
        # node55 = '{"NodeIndex": "node5_5", "Reference_task": "把答案键入到结果记录.txt里。", "Corresponding_application_contain": "结果记录"}'
        # node6 = '{"Reference_task": "在打开的Advanced Settings窗口中, 隐藏Process Name not equal to System的trace。", "Corresponding_application": "Advanced Settings"}'
        # node7 = '{"Reference_task": "记录System的CPU Usage占比。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'
        node8 = '{"NodeIndex": "node8", "Reference_task": "把答案键入到结果记录CPU.txt里并保存。", "Corresponding_application_contain": "结果记录CPU"}'
        node9 = '{"NodeIndex": "node9","Reference_task": "关闭filter,关闭Analysis窗口。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'

        # 在SAMSUNG属性里查看驱动程序关键字的值，记下值V下方窗口里的数据。把值V下方窗口里的数据键入到结果记录.txt里。
        # D:\QD\pycharmproject\issue debug
        # node1_1 = '{"ControlText": "地址栏", "Function": "set_edit_text", "Args":{"text": "xxx"}}'
        # node1_1 = '{"Function": "click_input", "Args": {"button": "left", "double": True}}'
        # node1_2 = '{"ControlText": "打开方式", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node1_3 = '{"ControlText": "媒体播放器", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        #
        # node1_2 = '{"#th UI after control text ##": 1, "control text ##": "磁盘驱动器", "Function": "click_input", "Args": {"button": "left", "double": True}}'
        # node18 = '{"Reference_task": "在涂鸦中点击在/离家布防。", "Corresponding_application_contain": "涂鸦"}'
        # node18_1 = '{"ControlText": "在/离家布防", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node1_1 = '{"ControlText": "Start", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node1_2 = '{"NodeIndex": "node1_2", "Function": "wait", "Args": {"time": 20}}'
        node1_3 = '{"NodeIndex": "node1_3", "ControlText": "Save", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "This action will save the recorded trace."}'
        node1_4 = '{"NodeIndex": "node1_4", "ControlText": "Save", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node1_5 = '{"Function": "check_available", "Args": {"control_text": "Open in WPA", "timeout": 60, "retry_interval": 5}}'
        node1_6 = '{"ControlText": "Open in WPA", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node1_7 = '{"NodeIndex": "node1_7", "Function": "wait", "Args": {"time": 20}}'
        node1_8 = '{"NodeIndex": "node1_8", "ControlText_contain_list": ["Close","关闭"], "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        node2_1 = '{"ControlText_contain_list": ["Close","关闭"], "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        node3_0_1 = '{"ControlText": "Window Position Menu", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node3_0_2 = '{"ControlText": None, "ControlLabel": None, "Function": "keypress", "Args": {"keys": "d"}}'
        node3_0_2 = '{"ControlText": "Dock", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node3_1 = '{"ControlText": "Computation - CPU Usage (Sampled) - Utilization by Process, Stack", "Function": "click_input", "Args": {"button": "right", "double": False}}'
        node3_2 = '{"ControlText": None, "ControlLabel": None, "Function": "keypress", "Args": {"keys": "a"}}'
        node3_3 = '{"NodeIndex": "node3_3", "ControlText": "Edit Filter", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        node4_1 = '{"ControlText": "Edit Filter", "Function": "set_WPA_trace_filter", "Args":{"trace_name_not_equal_to": "' + lines[0] + '", "press_down_times": 5}, "Action Introduction": "This action will filter out all traces but Idle.", "Status": "FINISH"}'

        node5_1 = '{"NodeIndex": "node5_1", "#th UI after control text contain ##": 2, "control text contain ##": "% Weight, ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node5_2 = '{"NodeIndex": "node5_2", "#th UI after control text contain ##": 2, "control text contain ##": "% Weight, ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node5_3 = '{"NodeIndex": "node5_3", "Function": "paste_whole_column_to_txt","Args": {"keys": "{VK_CONTROL}c"}}'
        node5_4 = '{"ControlText": "Edit Filter", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        # node55_1 = '{"NodeIndex": "node55_1", "Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}v"}, "Status": "FINISH"}'

        if len(lines) >= 2:
            dynamic_vars = {}
            for t in range(len(lines)-1):
                i = t + 1
                dynamic_vars['node_edit_filter' + lines[
                    i]] = '{"Reference_task": "在打开的Advanced Settings窗口中, 隐藏Process Name not equal to ' + lines[
                    i] + '的trace。", "Corresponding_application": "Advanced Settings"}'
                dynamic_vars['node_edit_filter_1' + lines[
                    i]] = '{"ControlText": "Edit Filter", "Function": "set_WPA_trace_filter", "Args":{"trace_name_not_equal_to": "' + \
                          lines[
                              i] + '", "press_down_times": 0}, "Action Introduction": "This action will filter out all traces but Idle.", "Status": "FINISH"}'

                dynamic_vars['node_read_CPU_usage' + lines[i]] = '{"Reference_task": "记录' + lines[
                    i] + '的CPU Usage占比，然后打开filter。", "Corresponding_application_contain": "Windows® Performance Analyzer"}'
                dynamic_vars['node_read_CPU_usage_1' + lines[i]] = '{"NodeIndex": "node_read_CPU_usage_1' + lines[
                    i] + '", "#th UI after control text contain ##": 2, "control text contain ##": "% Weight, ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
                dynamic_vars['node_read_CPU_usage_2' + lines[i]] = '{"NodeIndex": "node_read_CPU_usage_2' + lines[
                    i] + '", "#th UI after control text contain ##": 2, "control text contain ##": "% Weight, ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
                dynamic_vars['node_read_CPU_usage_3' + lines[i]] = '{"NodeIndex": "node_read_CPU_usage_3' + lines[
                    i] + '", "Function": "paste_whole_column_to_txt"}'
                dynamic_vars['node_read_CPU_usage_4' + lines[i]] = '{"NodeIndex": "node_read_CPU_usage_4' + lines[
                    i] + '", "ControlText": "Edit Filter", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

                # dynamic_vars['node_write_in_txt' + lines[i]] = '{"NodeIndex": "node_write_in_txt' + lines[
                #     i] + '", "Reference_task": "把答案键入到结果记录.txt里。", "Corresponding_application_contain": "结果记录"}'
                # dynamic_vars['node_write_in_txt_1' + lines[i]] = '{"NodeIndex": "node_write_in_txt_1' + lines[
                #     i] + '", "Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}v"}, "Status": "FINISH"}'

        # node6_1 = '{"ControlText": "Edit Filter", "Function": "set_WPA_trace_filter", "Args":{"trace_name_not_equal_to": "System", "press_down_times": 0}, "Action Introduction": "This action will filter out all traces but System.", "Status": "FINISH"}'
        #
        # node7_1 = '{"NodeIndex": "node7_1", "#th UI after control text contain ##": 2, "control text contain ##": "% Weight, ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node7_2 = '{"NodeIndex": "node7_2", "#th UI after control text contain ##": 2, "control text contain ##": "% Weight, ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node7_3 = '{"NodeIndex": "node7_3", "Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}c"}, "Status": "FINISH"}'


        # node8_1 = '{"ControlText_contain_list": ["文本编辑器","Text Editor"], "Function": "keyboard_input", "Args": {"keys": self.agent.blackboard.trajectories.content[4].Action[0]["Results"]["return_value"][0], "control_focus": True}}'
        # node8_2 = '{"ControlText_contain_list": ["文本编辑器","Text Editor"], "Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": True}}'

        # node8_1 = '{"NodeIndex": "node8_1", "Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}v"}}'
        node8_2 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}s"}}'
        node8_3 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}w"}, "Status": "FINISH"}'

        node9_1 = '{"NodeIndex": "node9_1", "ControlText_contain_list": ["Close","关闭"], "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node9_2 = '{"NodeIndex": "node10_1", "#th UI after control text ##": 3, "control text ##": "Analysis", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        # node6_1 = '{"ControlText": "文本编辑器", "Function": "keyboard_input", "Args": {"keys": "xx", "control_focus": True, "transform_tag": "large_bracket"}}'

        # 创建有向图
        G = nx.DiGraph()

        # 添加节点
        G.add_node(node0)
        # G.add_node(node1)
        G.add_node(node2)
        G.add_node(node3)
        # G.add_node(node4)
        # G.add_node(node5)

        # G.add_node(node1_1)

        G.add_node(node2_1)

        G.add_node(node3_1)
        # G.add_node(node3_2)
        # G.add_node(node3_3)

        # G.add_node(node4_1)

        # G.add_node(node5_1)
        # G.add_node(node5_2)
        # G.add_node(node5_3)
        # G.add_node(node5_4)

        # G.add_node(node6_1)

        # 添加边
        G.add_edge(node0, node1)
        G.add_edge(node0, node2)
        G.add_edge(node0, node3)
        G.add_edge(node0, node4)
        G.add_edge(node0, node5)
        # G.add_edge(node0, node6)
        # G.add_edge(node0, node7)
        G.add_edge(node0, node8)
        # G.add_edge(node0, node18)

        G.add_edge(node1, node1_1)
        G.add_edge(node1_1, node1_2)
        G.add_edge(node1_2, node1_3)
        G.add_edge(node1_3, node1_4)
        G.add_edge(node1_4, node1_5)
        G.add_edge(node1_5, node1_6)
        G.add_edge(node1_6, node1_7)
        G.add_edge(node1_7, node1_8)
        G.add_edge(node1_8, node2)

        G.add_edge(node2, node2_1)
        G.add_edge(node2_1, node3)

        G.add_edge(node3, node3_0_1)
        G.add_edge(node3_0_1, node3_0_2)
        G.add_edge(node3_0_2, node3_1)
        G.add_edge(node3_1, node3_2)
        G.add_edge(node3_2, node3_3)
        G.add_edge(node3_3, node4)

        G.add_edge(node4, node4_1)
        G.add_edge(node4_1, node5)

        G.add_edge(node5, node5_1)
        G.add_edge(node5_1, node5_2)
        G.add_edge(node5_2, node5_3)
        G.add_edge(node5_3, node5_4)
        # G.add_edge(node5_4, node55)

        # G.add_edge(node55, node55_1)

        if len(lines) >= 2:
            G.add_edge(node5_4, dynamic_vars['node_edit_filter' + lines[1]])

            for t in range(len(lines) - 1):
                i = t + 1
                G.add_edge(dynamic_vars['node_edit_filter' + lines[i]], dynamic_vars['node_edit_filter_1' + lines[i]])
                G.add_edge(dynamic_vars['node_edit_filter_1' + lines[i]], dynamic_vars['node_read_CPU_usage' + lines[i]])
                G.add_edge(dynamic_vars['node_read_CPU_usage' + lines[i]], dynamic_vars['node_read_CPU_usage_1' + lines[i]])
                G.add_edge(dynamic_vars['node_read_CPU_usage_1' + lines[i]], dynamic_vars['node_read_CPU_usage_2' + lines[i]])
                G.add_edge(dynamic_vars['node_read_CPU_usage_2' + lines[i]], dynamic_vars['node_read_CPU_usage_3' + lines[i]])
                G.add_edge(dynamic_vars['node_read_CPU_usage_3' + lines[i]], dynamic_vars['node_read_CPU_usage_4' + lines[i]])
                # G.add_edge(dynamic_vars['node_read_CPU_usage_4' + lines[i]],dynamic_vars['node_write_in_txt' + lines[i]])
                # G.add_edge(dynamic_vars['node_write_in_txt' + lines[i]], dynamic_vars['node_write_in_txt_1' + lines[i]])
                if i+1 == len(lines):
                    G.add_edge(dynamic_vars['node_read_CPU_usage_4' + lines[i]], node8)
                else:
                    G.add_edge(dynamic_vars['node_read_CPU_usage_4' + lines[i]], dynamic_vars['node_edit_filter' + lines[i+1]])
        else:
            G.add_edge(node5_4, node8)

        G.add_edge(node8, node8_2)
        G.add_edge(node8_2, node8_3)
        G.add_edge(node8_3, node9)

        G.add_edge(node9, node9_1)
        G.add_edge(node9_1, node9_2)

        # G.add_edge(node18, node18_1)

        self.graph = G

        return