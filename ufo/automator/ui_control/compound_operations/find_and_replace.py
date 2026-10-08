from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time

from ufo.utils import print_with_color

configs = Config.get_instance().config_data


class FindAndReplace:
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor

    def set_find_what_and_its_format(self):
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

        param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['查找内容']}, 'control_text': '查找内容(N):'}
        self.one_step_action(param)
        time.sleep(3)
        param = {'function': 'click_input', 'args': {"button": "left"}, 'control_text': '更多(M) >>'}
        self.one_step_action(param)
        time.sleep(3)
        param = {'function': 'click_input', 'args': {"button": "left"}, 'control_text': '格式'}
        self.one_step_action(param)
        time.sleep(3)
        param = {'function': 'keypress', 'args': {"keys": "f"}}
        self.one_step_action(param)
        time.sleep(3)
        if "中文字体" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['中文字体']}, 'control_text': '中文字体(T):'}
            self.one_step_action(param)
            time.sleep(3)
        if "西文字体" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['西文字体']}, 'control_text': '西文字体(F):'}
            self.one_step_action(param)
        if "字形" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['字形']}, 'control_text': '字形(Y):'}
            self.one_step_action(param)
        if "字号" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['字号']}, 'control_text': '字号(S):'}
            self.one_step_action(param)
        param = {'function': 'click_input', 'args': {"button": "left"}, 'control_text': '确定'}
        self.one_step_action(param)

    def set_replace_with_and_its_format(self):
        """
        设置替换内容及其格式
        :param params: 字典类型，包含'replace'（用于替换的内容）和'format'（格式信息）
        """

        # windows_dict = self.app_agent_processor.control_inspector.get_desktop_app_dict(remove_empty=True)
        # # windows_info = self.app_agent_processor.control_inspector.get_desktop_app_info(windows_dict)
        # for i in range(len(windows_dict)):
        #     if windows_dict[str(i + 1)].element_info.name == '查找和替换':
        #         break
        # self.app_agent_processor.application_window = windows_dict[str(i + 1)]

        param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['替换为']}, 'control_text': '替换为(I):'}
        self.one_step_action(param)
        time.sleep(3)
        param = {'function': 'click_input', 'args': {"button": "left"}, 'control_text': '更多(M) >>'}
        self.one_step_action(param)
        time.sleep(3)
        param = {'function': 'click_input', 'args': {"button": "left"}, 'control_text': '格式'}
        self.one_step_action(param)
        time.sleep(3)
        param = {'function': 'keypress', 'args': {"keys": "f"}}
        self.one_step_action(param)
        time.sleep(3)
        if "中文字体" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['中文字体']}, 'control_text': '中文字体(T):'}
            self.one_step_action(param)
            time.sleep(3)
        if "西文字体" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['西文字体']}, 'control_text': '西文字体(F):'}
            self.one_step_action(param)
        if "字形" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['字形']}, 'control_text': '字形(Y):'}
            self.one_step_action(param)
        if "字号" in self.app_agent_processor._args:
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['字号']}, 'control_text': '字号(S):'}
            self.one_step_action(param)
        param = {'function': 'click_input', 'args': {"button": "left"}, 'control_text': '确定'}
        self.one_step_action(param)

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
