from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time
import warnings
from ufo.utils import print_with_color
from pywinauto import Application, findwindows
import pyperclip

configs = Config.get_instance().config_data

class PasteWholeColumnToTxt(object):
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor

    def has_char_after_first_crlf(self, s):
        """
        检测字符串中第一个'\r\n'后面是否还有字符
        :param s: 输入字符串
        :return: 如果第一个'\r\n'后存在任何字符则返回True，否则返回False
        """
        index = s.find('\r\n')
        if index == -1:
            return False  # 没有找到\r\n
        # 检查\r\n后的位置是否在字符串长度范围内
        return index + 2 < len(s)

    def paste_whole_column_to_txt(self):
        """
        设置要查找的内容及它的格式
        :param params: 字典类型，包含'what'（需要查找的内容）和'format'（格式信息）
        """

        # windows_dict = self.app_agent_processor.control_inspector.get_desktop_app_dict(remove_empty=True)
        # # windows_info = self.app_agent_processor.control_inspector.get_desktop_app_info(windows_dict)
        # for i in range(len(windows_dict)):
        #     if windows_dict[str(i + 1)].element_info.name == '查找和替换':
        #         break
        # self.app_agent_processor.application_window = windows_dict[str(i + 1)]
        previous_copied_content = None

        hwnd = findwindows.find_window(title_re=".*结果记录.txt.*")
        app = Application(backend="uia").connect(handle=hwnd)
        target_window = app.window(handle=hwnd)

        param = {'function': 'keyboard_input', 'args': {"keys": "{VK_CONTROL}c"}}
        self.one_step_action(param)
        time.sleep(1)

        copied_content = pyperclip.paste()
        while previous_copied_content != copied_content and self.has_char_after_first_crlf(copied_content):
            previous_copied_content = copied_content
            target_window.set_focus()
            target_window.type_keys("^v")

            param = {'function': 'keyboard_input', 'args': {"keys": "{DOWN}"}}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'keyboard_input', 'args': {"keys": "{VK_CONTROL}c"}}
            self.one_step_action(param)
            time.sleep(1)

            copied_content = pyperclip.paste()

    def one_step_action(self, param):
        ui_control_list = (
            self.app_agent_processor.control_inspector.find_control_elements_in_descendants(
                self.app_agent_processor.application_window,
                control_type_list=configs.get("CONTROL_LIST", []),
                class_name_list=configs.get("CONTROL_LIST", []),
            )
        )
        annotation_dict = self.app_agent_processor.photographer.get_annotation_dict(
            self.app_agent_processor.application_window, ui_control_list, annotation_type="number"
        )

        if 'control_text' in param:
            param['control_label'] = ''
            for i in range(len(ui_control_list)):
                if ui_control_list[i].element_info.name == param['control_text']:
                    param['control_label'] = str(i + 1)
                    break
            else:
                print_with_color("Control Text not Found in List", "red")
        else:
            param['control_text'] = ''

        if 'control_label' not in param:
            param['control_label'] = ''
        act = OneStepAction(
            function=param['function'],
            args=param['args'],
            control_label=param['control_label'],
            control_text=param['control_text'],
        )
        act_sequence = ActionSequence([act])
        act_sequence.execute_all(
            puppeteer=self.app_agent_processor.app_agent.Puppeteer,
            control_dict=annotation_dict,
            application_window=self.app_agent_processor.application_window,
        )