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

        node1 = '{"Reference_task": "Open Find and Replace"}'
        node1_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}h"}, "Action Introduction": "This action will open the Find and Replace window."}'

        node2 = '{"Reference_task": "Change the xxx in xxx to a subscript/superscript"}'
        node2_1 = '{"Function": "change_xxx_in_xxx_to_subscript", "Args":{"string to select": "xx", "substring to subscript": "xx"}, "Action Introduction": "This action will change the substring xxx in string xxx to subscript."}'

        node3 = '{"Reference_task": "Select all."}'
        node3_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}a"}}'

        node4 = '{"Reference_task": "Change the selected text font to xx."}'
        node4_1 = '{"ControlText": "Home", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node4_2 = '{"ControlText": "Font", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        node4_3 = '{"Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": False}}'

        node5 = '{"Reference_task": "Select text xx and align the selected text to the xxx."}'
        node5_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}f"}}'
        node5_2 = '{"ControlText": "Search document", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        node5_3 = '{"ControlText": "Next Result", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node5_4 = '{"ControlText": "Close pane", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node5_5 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node6 = '{"Reference_task": "Export the current document into PDF with name xxx."}'
        node6_1 = '{"NodeIndex": "node6_1", "ControlText": "File Tab", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node6_2 = '{"NodeIndex": "node6_2", "ControlText": "Export", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node6_3 = '{"ControlText": "Create PDF/XPS", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node6_4 = '{"ControlText": "File name:", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        node6_5 = '{"ControlText": "Publish", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node7 = '{"Reference_task": "Delete duplicate texts in list xxx after Find and Replace function is opened.", "Corresponding_application": "Find and Replace"}'
        node7_1 = '{"Function": "delete_duplicates", "Args": {"choosing_texts_list": "xx"}, "Action Introduction": "This action will delete duplicates of all texts in the list."}'
        node7_2 = '{"ControlText": "Close", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "This action indicates all duplicated occurrence of the selected texts in the list has been removed."}'

        node8 = '{"Reference_task": "Select text xx and change the line space to xxx."}'
        node8_1 = '{"Function": "select_text","Args": {"text": "xx"}}'
        node8_2 = '{"Function": "select_paragraph","Args": {"start_index": "xx", "end_index": "xx", "non_empty": True}}'
        node8_3 = '{"ControlText": "Line and Paragraph Spacing", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node8_4 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        node9 = '{"Reference_task": "Insert a blank page after page xx."}'
        node9_1 = '{"Function": "move_cursor_to_beginning_of_page_xx","Args": {"target_page_number": "xx"}, "Action Introduction": "This action will move cursor to the beginning of page xx, then we can insert blank page before page xx."}'
        node9_2 = '{"ControlText": "Insert", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node9_3 = '{"ControlText": "Blank Page", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node91 = '{"Reference_task": "Change case of selected texts."}'
        node91_11 = '{"Function": "select_text","Args": {"text": "xx"}}'
        node91_12 = '{"Function": "select_paragraph","Args": {"start_index": "xx", "end_index": "xx", "non_empty": True}}'
        node91_13 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}a"}}'
        node91_2 = '{"ControlText": "Change Case", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node91_3 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        node10 = '{"Reference_task": "Save the Excel sheet as xxx."}'
        node10_1 = '{"Function": "save_as", "Args": {"file_dir": "xx", "file_name": "xx", "file_ext": "xx"}}'

        node11 = '{"Reference_task": "Reorder the columns to xxx."}'
        node11_1 = '{"Function": "reorder_columns", "Args": {"sheet_name": "xx", "desired_order": "xx"}}'

        node12 = '{"Reference_task": "Fill xxx as xxx in the xxx column."}'
        node12_1 = '{"Function": "insert_excel_table", "Args": {"table": "xx", "sheet_name": "xx", "start_row": "xx", "start_col": "xx"}, "Action Introduction": "This action will insert a table to target position based on requirement."}'
        # node12_1 = '{"ControlText": "xxx", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        node12_2 = '{"ControlText": "Line down", "Function": "click_input", "Args": {"button": "left", "double": True}}'

        node13 = '{"Reference_task": "Select cell and setting its background as xxx."}'
        # node13_1 = '{"Function": "select_table_range", "Args": {"sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx", "end_row": "xxx", "end_col": "xxx"}, "Action Introduction": "Choose this action to select target cells which their background will be changed in the next action."}'
        node13_1 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose this action to click on target cell."}'
        node13_2 = '{"#th UI after control text ##": 2, "control text ##": "Fill Color", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the dropdown list to select more background color."}'
        node13_3 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose background color from the dropdown list."}'
        node13_4 = '{"ControlText": "Line down", "Function": "click_input", "Args": {"button": "left", "double": True}, "Action Introduction": "Choose this action to scroll down a little bit when the target cell not shown in the screen."}'

        node14 = '{"Reference_task": "Select table and open the sort window."}'
        node14_1 = '{"Function": "select_table_range", "Args": {"sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx", "end_row": "xxx", "end_col": "xxx"}}'
        node14_2 = '{"ControlText": "Data", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node14_3 = '{"ControlText": "Sort...", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH", "Action Introduction": "This action will open the Sort window, switch to Sort window in the next step."}'

        node15 = '{"Reference_task": "Set the Sort window and confirm.", "Corresponding_application": "Sort", "Status": "ASSIGN", "Action Introduction": "This action will focus on the Sort window, set the Sort window in the following steps."}'
        node15_1 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}}'


        # node15_1 = '{"#th UI after control text ##": 2, "control text ##": "Sort by", "Function": "set_edit_text", "Args":{"text": "xx"}, "Action Introduction": "Set the sort by to required value."}'
        # # node15_1 = '{"#th UI after control text ##": 2, "control text ##": "Sort by", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the Sort by dropdown list in the Sort dialog box."}'
        # # node15_1 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the Sort by dropdown list in the Sort dialog box."}'
        # node15_2 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose the column to be referenced for sorting from the dropdown list."}'
        # node15_3 = '{"#th UI after control text ##": 1, "control text ##": "Sort On", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the Sort on dropdown list in the Sort dialog box."}'
        # node15_4 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose the property to be referenced for sorting from the dropdown list."}'
        # node15_5 = '{"#th UI after control text ##": 1, "control text ##": "Order", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the Order dropdown list in the Sort dialog box."}'
        # node15_6 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose the order for sorting from the dropdown list."}'
        # node15_7 = '{"ControlText": "OK", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node16 = '{"Reference_task": "Select NA cells and hide them."}'
        # node16_1 = '{"Function": "select_table_range", "Args": {"sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx", "end_row": "xxx", "end_col": "xxx"}, "Action Introduction": "Select cells that contain NA and cells that related to these cells."}'
        node16_1 = '{"ControlText": "Home", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Go to Home tab then click Find & Select."}'
        node16_2 = '{"ControlText": "Find & Select", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_3 = '{"ControlText": "Go To Special...", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_4 = '{"ControlText": "Formulas", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_5 = '{"ControlText": "Numbers", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_6 = '{"ControlText": "Text", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_7 = '{"ControlText": "Logicals", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_8 = '{"ControlText": "OK", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node16_9 = '{"#th UI after control text ##": 2, "control text ##": "Font Color", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the font color dropdown list."}'
        node16_10 = '{"ControlText_Contain": "Background 1", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose the white color to hide the selected cells."}'

        node17 = '{"Reference_task": "Remove the adundant whitespaces and canonicalized letter cases by inserting table content into target position based on other cells value."}'
        node17_1 = '{"Function": "insert_excel_table", "Args": {"table": "xxx", "sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx"}, "Action Introduction": "Insert canonicalized table content, make sure new content satisfy the user requirement."}'

        node18 = '{"Reference_task": "Remove duplicated items in Excel and input unique ones in target position."}'
        node18_1 = '{"Function": "insert_excel_table", "Args": {"table": "xxx", "sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx"}, "Action Introduction": "Insert table content of unique ones, make sure new content satisfy the user requirement."}'

        node19 = '{"Reference_task": "Transpose table in Excel and paste it in the target position."}'
        node19_1 = '{"Function": "select_table_range", "Args": {"sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx", "end_row": "xxx", "end_col": "xxx"}, "Tips": "start_col, start_row, end_col and end_row should only depend on the first and last cell provided in the File Content, not the screenshot. For example, if the first cell in provided File Content is A1, the start_col and start_row should be 1 and 1. If the last cell is G6, the end_col and end_row should be 7 and 6."}'
        node19_2 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}c"}}'
        node19_3 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "right", "double": False}, "Action Introduction": "Right click the target cell before using paste special to paste the transposed table."}'
        node19_4 = '{"ControlText": "Transpose", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node20 = '{"Reference_task": "Make following cells dropdown list."}'
        node20_1 = '{"Function": "select_table_range", "Args": {"sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx", "end_row": "xxx", "end_col": "xxx"}, "Tips": "Select target table range based on user requirement."}'
        node20_2 = '{"ControlText": "Data", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Switch to Data tab before Data Validation."}'
        node20_3 = '{"#th UI after control text ##": 1, "control text ##": "Data Validation...", "Function": "click_input", "Args": {"button": "left", "double": False}, "Status": "FINISH"}'

        node21 = '{"Reference_task": "Set the dropdown list allowed content.", "Corresponding_application": "Data Validation"}'
        node21_1 = '{"#th UI after control text ##": 1, "control text ##": "Allow:", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Open the Allow dropdown list."}'
        node21_2 = '{"ControlText": "List", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node21_3 = '{"#th UI after control text ##": 1, "control text ##": "Source:", "Function": "set_edit_text", "Args":{"text": "xx"}, "Action Introduction": "Set the dropdown list allowed content, seperated by comma, e.g. A,B,C."}'

        node22 = '{"Reference_task": "Set background color in PowerPoint as xxx.", "Corresponding_application_contain": "PowerPoint"}'
        node22_1 = '{"ControlText": "Design", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node22_2 = '{"ControlText": "Format Background", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node22_3 = '{"ControlText": "Fill Color RGB(255, 255, 255)", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node22_4 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose the proper color for the background based on user requirement."}'
        node22_5 = '{"ControlText": "Apply to All", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node23 = '{"Reference_task": "Create cover page using target image in PPT.", "Corresponding_application_contain": "PowerPoint"}'
        # node23_1 = '{"ControlText": "Insert", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node23_1 = '{"Function": "click_on_coordinates", "Args": {"x": "xxx", "y": "xxx", "button": "left", "double": False}, "Action Introduction": "click to choose the target image in slide"}'
        node23_2 = '{"Function": "drag_on_coordinates", "Args": {"start_x": "xxx", "start_y": "xxx", "end_x": "xxx", "end_y": "xxx","button": "left"}, "Action Introduction": "drag to stretch the target image in slide"}'

        node24 = '{"Reference_task": "Make duplicates of target slides.", "Corresponding_application_contain": "PowerPoint", "Tips": "Do not set the target slides so early, wait until app agent get the detailed file content."}'
        # node24_1 = '{"Function": "keyboard_input", "Args": {"keys": "{END}", "control_focus": False}}'
        node24_1 = '{"ControlText": "工作区", "Function": "wheel_mouse_input", "Args": {"wheel_dist": "xxx"}, "Action Introduction": "Scroll down until target slides show up.", "Tips": "Given the file content, reconsider the choice of target slides."}'
        node24_2 = '{"Function": "click_on_coordinates", "Args": {"x": "xxx", "y": "xxx", "button": "left", "double": False}, "Action Introduction": "click to choose the first target slide on the left side"}'
        node24_3 = '{"Function": "click_on_coordinates", "Args": {"x": "xxx", "y": "xxx", "button": "left", "double": False, "pressed": "CONTROL"}, "Action Introduction": "press control and click to choose the rest target slide on the left side"}'
        node24_4 = '{"Function": "keyboard_input", "Args": {"keys": "{VK_CONTROL}d", "control_focus": False}, "Action Introduction": "Make a duplicate of the target slides."}'

        node25 = '{"Reference_task": "Save slides as xxx at xxx.", "Corresponding_application_contain": "PowerPoint"}'
        node25_1 = '{"Function": "save_as", "Args": {"file_dir": "xxx", "file_name": "xxx", "file_ext": "xxx", "current_slide_only": "xxx"}}'
        node25_2 = '{"Function": "save_as", "Args": {"file_dir": os.path.join(os.environ["USERPROFILE"], "Desktop"), "file_name": "xxx", "file_ext": "xxx", "current_slide_only": "xxx"}, "Action Introduction": "Choose this action to save file to the desktop."}'
        # # node13_1 = '{"Function": "select_table_range", "Args": {"sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx", "end_row": "xxx", "end_col": "xxx"}, "Action Introduction": "Choose this action to select target cells."}'
        # node13_1 = '{"ControlText": "xxx", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose this action to select target cells."}'

        node26 = '{"Reference_task": "Select target texts and set its format.", "Corresponding_application_contain": "PowerPoint"}'
        node26_1 = '{"ControlText": "工作区", "Function": "wheel_mouse_input", "Args": {"wheel_dist": "xxx"}, "Action Introduction": "Scroll down until target slide shows up.", "Tips": "Given the file content, reconsider the choice of target slide."}'
        node26_2 = '{"Function": "click_on_coordinates", "Args": {"x": "xxx", "y": "xxx", "button": "left", "double": False}, "Action Introduction": "click to choose the target slide on the left side"}'
        node26_3 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}f"}, "Action Introduction": "Open the Find and Replace window.", "Tips": "Target texts are hard to select by mouse click, using search function to choose them instead"}'
        node26_4 = '{"#th UI after control text ##": -1, "control text ##": "Match case", "Function": "set_edit_text", "Args":{"text": "xx"}, "Action Introduction": "Choose the target text by searching.", "Tips": "Target texts are hard to select by mouse click, using search function to choose them instead"}'
        node26_5 = '{"ControlText": "Close pane", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Close the Find and Replace window."}'
        node26_6 = '{"ControlText": "Strikethrough", "Function": "click_input", "Args": {"button": "left", "double": False}, "Action Introduction": "Choose the proper format for the selected text based on user requirement."}'

        node27 = '{"Reference_task": "Insert certain texts in docx based on provided files."}'
        node27_1 = '{"Function": "select_text","Args": {"text": "xx"}, "Action Introduction": "Use this action then press right to move cursor to the right of selected text."}'
        node27_2 = '{"Function": "keyboard_input", "Args": {"keys": "{RIGHT}", "control_focus": False}, "Action Introduction": "Use this action after select target text to move cursor to the right of selected text."}'
        node27_3 = '{"Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": False}, "Action Introduction": "Use this action to start a new line after current cursor position."}'
        node27_4 = '{"Function": "keyboard_input", "Args": {"keys": "xxx", "control_focus": False}}'

        node28 = '{"Reference_task": "Edit certain texts in docx."}'
        node28_1 = '{"Function": "move_cursor_to_beginning_of_page_xx","Args": {"target_page_number": "xx"}, "Action Introduction": "Move cursor to the target page."}'
        node28_2 = '{"Function": "select_paragraph","Args": {"start_index": "xx", "end_index": "xx", "non_empty": True}, "Action Introduction": "Use this action to select target text for editing."}'
        node28_1 = '{"Function": "select_text","Args": {"text": "xx"}, "Action Introduction": "Use this action to select target text for editing."}'
        node28_3 = '{"Function": "keyboard_input", "Args": {"keys": "xxx", "control_focus": False}, "Action Introduction": "Use this action to input text to replace target text."}'

        node29 = '{"Reference_task": "Edit certain cell in Excel."}'
        node29_1 = '{"ControlText": "xx", "Function": "set_edit_text", "Args":{"text": "xx"}}'

        node30 = '{"Reference_task": "Export PPT as video."}'
        node30_1 = '{"ControlText": "File Tab", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node30_2 = '{"NodeIndex": "node30_2", "ControlText": "Export", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node30_3 = '{"ControlText": "Create a Video", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node30_4 = '{"ControlText": "Create Video", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node30_5 = '{"ControlText": "Export", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node31 = '{"Reference_task": "Insert table in Excel."}'
        node31_1 = '{"Function": "insert_excel_table", "Args": {"table": "xxx", "sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx"}}'

        node32 = '{"Reference_task": "Click Quick Start in chrome webpage"}'
        node32_1 =  '{"ControlText": "My Drive", "Function": "click_input", "Args": {"button": "right", "double": False}}'


        node33 = '{"Reference_task": "Open PDF file", "Corresponding_application_contain": "文件资源管理器"}'
        node33_1 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": True}, "Status": "FINISH"}'

        node34 = '{"Reference_task": "Check PDF file", "Corresponding_application_contain": "pdf"}'
        node34_1 = '{"Function": "no_action", "Corresponding_application_contain": "pdf", "Action Introduction": "Use this action to go through the paper first page and extract author information.", "Status": "FINISH"}'

        node35 = '{"Reference_task": "Fill excel table based on extracted information", "Corresponding_application_contain": "Excel"}'
        node35_1 = '{"Function": "insert_excel_table", "Args": {"table": "xxx", "sheet_name": "xxx", "start_row": "xxx", "start_col": "xxx"}, "Action Introduction": "Insert table based on extracted information."}'

        node36 = '{"Reference_task": "Export address book from Thunderbird", "Corresponding_application_contain": "Thunderbird"}'
        node36_1 = '{"ControlText_Contain": "Address Book", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node36_2 = '{"ControlText_Contain": "Personal Address Book", "Function": "click_input", "Args": {"button": "right", "double": False}}'
        node36_3 = '{"ControlText_Contain": "Export", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node36_4 = '{"ControlText_Contain": "保存(S)", "Function": "click_input", "Args": {"button": "left", "double": False}}'

        node37 = '{"Reference_task": "Edit notes in PowerPoint based on docx file", "Corresponding_application_contain": "PowerPoint"}'
        node37_1 = '{"ControlText": "Status Bar", "Function": "set_edit_text", "Args":{"text": "xx", "coords":[500, -20]}, "Action Introduction": "Add notes based on information from docx file to current slide."}'
        node37_1_1 = '{"ControlText": "Notes ", "Function": "click_input", "Args": {"button": "left", "double": True}}'
        node37_2 = '{"Function": "keyboard_input", "Args": {"keys": "{PGDN}", "control_focus": False}, "Action Introduction": "Check control text (View Indicator Slide xx of xx) for the current slide, press PAGE DOWN to go to next slide."}'

        node38 = '{"Reference_task": "Draw in paint.", "Corresponding_application_contain": "画图"}'
        node38_1 = '{"ControlText": "xx", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        node38_2 = '{"Function": "drag_on_coordinates", "Args": {"start_x": "xxx", "start_y": "xxx", "end_x": "xxx", "end_y": "xxx","button": "left", "key_hold": "xxx"}, "Action Introduction": "drag to stretch the target image in slide"}'


        # node2 = '{"Reference_task": "在word里打开查找和替换"}'
        # node3 = '{"Reference_task": "将光标后的xx个xx替换为xx"}'
        # node4 = '{"Reference_task": "新建文档"}'
        # node5 = '{"Reference_task": "将选中文字字体修改为xx"}'
        # node6 = '{"Reference_task": "查找所有xx格式的“xx”将其全部替换为xx格式的xx。", "Corresponding_application": "查找和替换"}'
        #
        # node7 = '{"Reference_task": "将选中文字字号修改为xx"}'
        # node8 = '{"Reference_task": "将选中文字颜色修改为xx"}'
        #
        # node1_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}f"}}'
        # node1_2 = '{"ControlText": "搜索文档", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node1_3 = '{"ControlText": "下一个结果", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node1_4 = '{"ControlText": "关闭窗格", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node1_5 = '{"Function": "keyboard_input", "Args": {"keys": "{RIGHT}", "control_focus": False}}'
        # node1_6 = '{"Function": "keyboard_input", "Args": {"keys": "xx", "control_focus": False}}'
        #
        # node2_1 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}h"}}'
        # node2_2 = '{"Function": "keyboard_input","Args": {"keys": "{VK_CONTROL}a"}}'
        #
        # node3_1 = '{"ControlText": "查找内容(N):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node3_2 = '{"ControlText": "替换为(I):", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node3_3 = '{"ControlText": "查找下一处(F)", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node3_4 = '{"ControlText": "替换(R)", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node3_5 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        #
        # node4_1 = '{"ControlText": "“文件”选项卡", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node4_2 = '{"ControlText": "新建", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node4_3 = '{"ControlText": "空白文档", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        #
        # node5_1 = '{"ControlText": "开始", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node5_2 = '{"ControlText": "字体", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node5_3 = '{"Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": False}}'
        #
        #
        # node6_1 = '{"ControlText": "查找内容(N):", "Function": "set_find_what_and_its_format", "Args":{"查找内容": "xx", "中文字体": "xx"}}'
        # node6_2 = '{"ControlText": "替换为(I):", "Function": "set_replace_with_and_its_format", "Args":{"替换为": "xx", "中文字体": "xx"}}'
        #
        # node6_11 = '{"ControlText": "替换(R)", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node6_12 = '{"ControlText": "全部替换(A)", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node6_13 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node6_14 = '{"ControlText": "关闭", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        #
        # node7_2 = '{"ControlText": "字号", "Function": "set_edit_text", "Args":{"text": "xx"}}'
        # node7_3 = '{"Function": "keyboard_input", "Args": {"keys": "{ENTER}", "control_focus": False}}'
        #
        # node8_2 = '{"Previous_ControlText_Contain": "字体颜色 ", "Function": "click_input", "Args": {"button": "left", "double": False}}'
        # node8_3 = '{"Function": "click_input", "Args": {"button": "left", "double": False}}'

        # 创建有向图
        G = nx.DiGraph()

        # 添加节点
        G.add_node(node0)

        G.add_node(node1)
        G.add_node(node1_1)

        G.add_node(node2)
        G.add_node(node2_1)
        # G.add_node(node2_2)
        # G.add_node(node2_3)

        G.add_node(node3)
        G.add_node(node3_1)

        G.add_node(node4)
        G.add_node(node4_1)
        G.add_node(node4_2)
        G.add_node(node4_3)

        G.add_node(node5)
        G.add_node(node5_1)
        G.add_node(node5_2)
        G.add_node(node5_3)
        G.add_node(node5_4)
        G.add_node(node5_5)

        G.add_node(node6)
        G.add_node(node6_1)
        G.add_node(node6_2)
        G.add_node(node6_3)
        G.add_node(node6_4)
        G.add_node(node6_5)

        G.add_node(node7)
        G.add_node(node7_1)
        G.add_node(node7_2)
        # G.add_node(node7_3)
        # G.add_node(node7_4)

        G.add_node(node8)
        G.add_node(node8_1)
        G.add_node(node8_2)
        G.add_node(node8_3)
        G.add_node(node8_4)

        G.add_node(node9)
        G.add_node(node9_1)
        G.add_node(node9_2)
        G.add_node(node9_3)

        G.add_node(node10)
        G.add_node(node10_1)

        G.add_node(node11)
        G.add_node(node11_1)

        G.add_node(node12)
        G.add_node(node12_1)
        G.add_node(node12_2)

        G.add_node(node13)
        G.add_node(node13_1)
        G.add_node(node13_2)

        G.add_node(node14)
        G.add_node(node14_1)
        G.add_node(node14_2)
        G.add_node(node14_3)

        G.add_node(node15)
        G.add_node(node15_1)
        # G.add_node(node15_2)
        # G.add_node(node15_3)
        # G.add_node(node15_4)
        # G.add_node(node15_5)
        # G.add_node(node15_6)
        # G.add_node(node15_7)


        G.add_node(node16)
        G.add_node(node16_1)
        G.add_node(node16_2)
        G.add_node(node16_3)
        G.add_node(node16_4)
        G.add_node(node16_5)
        G.add_node(node16_6)
        G.add_node(node16_7)
        G.add_node(node16_8)
        G.add_node(node16_9)
        G.add_node(node16_10)

        G.add_node(node17)
        G.add_node(node17_1)

        G.add_node(node18)
        G.add_node(node18_1)

        G.add_node(node19)
        G.add_node(node19_1)
        G.add_node(node19_2)
        G.add_node(node19_3)
        G.add_node(node19_4)

        # 添加边
        # G.add_edge(node0, node1)
        # G.add_edge(node0, node2)
        # # G.add_edge(node0, node3)
        # G.add_edge(node0, node4)
        # G.add_edge(node0, node5)
        # G.add_edge(node0, node6)
        # G.add_edge(node0, node7)
        # G.add_edge(node0, node8)
        # G.add_edge(node0, node9)
        # G.add_edge(node0, node91)
        # G.add_edge(node0, node10)
        # G.add_edge(node0, node11)
        # G.add_edge(node0, node12)
        # G.add_edge(node0, node13)
        # G.add_edge(node0, node14)
        G.add_edge(node0, node15)
        # G.add_edge(node0, node16)
        # G.add_edge(node0, node17)
        # G.add_edge(node0, node18)
        # G.add_edge(node0, node19)
        # G.add_edge(node0, node20)
        # G.add_edge(node0, node22)
        G.add_edge(node0, node23)
        # G.add_edge(node0, node24)
        # G.add_edge(node0, node25)
        # G.add_edge(node0, node26)
        G.add_edge(node0, node27)
        G.add_edge(node0, node28)
        G.add_edge(node0, node29)
        G.add_edge(node0, node30)
        G.add_edge(node0, node31)
        G.add_edge(node0, node32)
        G.add_edge(node0, node33)
        G.add_edge(node0, node36)
        G.add_edge(node0, node37)
        G.add_edge(node0, node38)

        G.add_edge(node1, node1_1)

        G.add_edge(node2, node2_1)
        # G.add_edge(node2_1, node2_2)
        # G.add_edge(node2_2, node2_3)

        G.add_edge(node3, node3_1)

        G.add_edge(node4, node4_1)
        G.add_edge(node4_1, node4_2)
        G.add_edge(node4_2, node4_3)

        G.add_edge(node5, node5_1)
        G.add_edge(node5_1, node5_2)
        G.add_edge(node5_2, node5_3)
        G.add_edge(node5_3, node5_4)
        G.add_edge(node5_4, node5_5)

        G.add_edge(node6, node6_1)
        G.add_edge(node6_1, node6_2)
        G.add_edge(node6_2, node6_3)
        G.add_edge(node6_3, node6_4)
        G.add_edge(node6_3, node6_5)
        G.add_edge(node6_4, node6_5)

        G.add_edge(node7, node7_1)
        G.add_edge(node7_1, node7_2)
        # G.add_edge(node7_2, node7_3)
        # G.add_edge(node7_3, node7_3)
        # G.add_edge(node7_3, node7_4)
        # G.add_edge(node7_4, node7_1)

        # G.add_edge(node8,node8_1)
        G.add_edge(node8,node8_2)
        G.add_edge(node8_1,node8_3)
        G.add_edge(node8_2,node8_3)
        G.add_edge(node8_3, node8_4)
        # G.add_edge(node8_4, node8_1)
        G.add_edge(node8_4, node8)

        G.add_edge(node9, node9_1)
        G.add_edge(node9_1, node9_2)
        G.add_edge(node9_2, node9_3)

        G.add_edge(node91, node91_11)
        G.add_edge(node91, node91_12)
        G.add_edge(node91, node91_13)
        G.add_edge(node91_11, node91_2)
        G.add_edge(node91_12, node91_2)
        G.add_edge(node91_13, node91_2)
        G.add_edge(node91_2, node91_3)

        G.add_edge(node10, node10_1)

        G.add_edge(node11, node11_1)

        G.add_edge(node12, node12_1)
        # G.add_edge(node12_1, node12_1)
        G.add_edge(node12_1, node12_2)
        G.add_edge(node12_2, node12_1)

        G.add_edge(node13, node13_1)
        G.add_edge(node13_1, node13_2)
        G.add_edge(node13_2, node13_3)
        G.add_edge(node13_3, node13_1)
        G.add_edge(node13_3, node13_4)
        G.add_edge(node13_4, node13_1)

        G.add_edge(node14, node14_1)
        G.add_edge(node14_1, node14_2)
        G.add_edge(node14_2, node14_3)
        G.add_edge(node14_3, node15)

        G.add_edge(node15, node15_1)
        G.add_edge(node15_1, node15_1)


        # G.add_edge(node15_1, node15_7)

        # G.add_edge(node15_2, node15_3)
        # G.add_edge(node15_3, node15_4)
        # G.add_edge(node15_4, node15_5)
        # G.add_edge(node15_5, node15_6)
        # G.add_edge(node15_6, node15_7)
        # G.add_edge(node15_7, node15_8)
        # G.add_edge(node14_10, node14_11)

        G.add_edge(node16, node16_1)
        G.add_edge(node16_1, node16_2)
        G.add_edge(node16_2, node16_3)
        G.add_edge(node16_3, node16_4)
        G.add_edge(node16_4, node16_5)
        G.add_edge(node16_5, node16_6)
        G.add_edge(node16_6, node16_7)
        G.add_edge(node16_7, node16_8)
        G.add_edge(node16_8, node16_9)
        G.add_edge(node16_9, node16_10)

        G.add_edge(node17, node17_1)

        G.add_edge(node18, node18_1)

        G.add_edge(node19, node19_1)
        G.add_edge(node19_1, node19_2)
        G.add_edge(node19_2, node19_3)
        G.add_edge(node19_3, node19_4)

        G.add_edge(node20, node20_1)
        G.add_edge(node20_1, node20_2)
        G.add_edge(node20_2, node20_3)
        G.add_edge(node20_3, node21)

        G.add_edge(node21, node21_1)
        G.add_edge(node21_1, node21_2)
        G.add_edge(node21_2, node21_3)

        G.add_edge(node22, node22_1)
        G.add_edge(node22_1, node22_2)
        G.add_edge(node22_2, node22_3)
        G.add_edge(node22_3, node22_4)
        G.add_edge(node22_4, node22_5)

        G.add_edge(node23, node23_1)
        G.add_edge(node23_1, node23_1)
        G.add_edge(node23_1, node23_2)
        G.add_edge(node23_2, node23_2)

        G.add_edge(node24, node24_1)
        G.add_edge(node24_1, node24_1)
        G.add_edge(node24_1, node24_2)
        G.add_edge(node24_2, node24_3)
        G.add_edge(node24_3, node24_3)
        G.add_edge(node24_3, node24_4)
        G.add_edge(node24_2, node24_4)
        G.add_edge(node24_4, node24_2)

        G.add_edge(node25, node25_1)
        G.add_edge(node25, node25_2)

        G.add_edge(node26, node26_1)
        G.add_edge(node26_1, node26_1)
        G.add_edge(node26_1, node26_2)
        G.add_edge(node26_2, node26_3)
        G.add_edge(node26_3, node26_4)
        G.add_edge(node26_4, node26_5)
        G.add_edge(node26_5, node26_6)
        G.add_edge(node26_6, node26_3)

        G.add_edge(node27, node27_1)
        G.add_edge(node27_1, node27_2)
        G.add_edge(node27_2, node27_3)
        G.add_edge(node27_3, node27_4)
        # G.add_edge(node27_4, node27_4)
        G.add_edge(node27_4, node27_1)

        G.add_edge(node28, node28_1)
        # G.add_edge(node28, node28_2)
        G.add_edge(node28_1, node28_3)
        # G.add_edge(node28_2, node28_3)
        G.add_edge(node28_3, node28_1)
        # G.add_edge(node28_3, node28_2)

        G.add_edge(node29, node29_1)
        G.add_edge(node29_1, node29_1)

        G.add_edge(node30, node30_1)
        G.add_edge(node30_1, node30_2)
        G.add_edge(node30_2, node30_3)
        G.add_edge(node30_3, node30_4)
        G.add_edge(node30_4, node30_5)

        G.add_edge(node31, node31_1)

        G.add_edge(node32, node32_1)

        G.add_edge(node33, node33_1)
        G.add_edge(node33_1, node34)
        G.add_edge(node34, node34_1)
        G.add_edge(node34_1, node33)
        G.add_edge(node34_1, node35)
        G.add_edge(node35, node35_1)
        G.add_edge(node35_1, node35_1)
        G.add_edge(node35_1, node33)

        G.add_edge(node36, node36_1)
        G.add_edge(node36_1, node36_2)
        G.add_edge(node36_2, node36_3)
        G.add_edge(node36_3, node36_4)
        # G.add_edge(node36_4, node36_5)
        # G.add_edge(node36_5, node36_6)

        G.add_edge(node37, node37_1)
        G.add_edge(node37, node37_2)
        G.add_edge(node37_1, node37_1_1)
        G.add_edge(node37_1_1, node37_2)
        G.add_edge(node37_2, node37_2)
        G.add_edge(node37_2, node37_1)

        G.add_edge(node38, node38_1)
        G.add_edge(node38_1, node38_1)
        G.add_edge(node38_1, node38_2)

        self.graph = G

        return