from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time
import warnings
from ufo.utils import print_with_color

configs = Config.get_instance().config_data

class SetWPATraceFilter:
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor

    def set_WPA_trace_filter(self):
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

        # param = {'function': 'click_input', 'args': {"button": "left", "double": False}, 'control_label': '4'}
        # self.one_step_action(param)
        # time.sleep(1)
        # param = {'function': 'keyboard_input', 'args': {"keys": "{UP}"}}
        # self.one_step_action(param)
        # time.sleep(1)
        # param = {'function': 'keyboard_input', 'args': {"keys": "{ENTER}"}}
        # self.one_step_action(param)
        # time.sleep(1)
        # param = {'function': 'click_input', 'args': {"button": "left", "double": False}, 'control_text': "Group 0 and selector"}
        # self.one_step_action(param)
        # time.sleep(1)
        param = {'function': 'set_edit_text', 'args': {"text": "Process Name"},'control_text': 'Condition 0 column name'}
        self.one_step_action(param)
        time.sleep(1)
        param = {'function': 'click_input', 'args': {"button": "left", "double": False},'control_text': 'Condition 0 operation'}
        self.one_step_action(param)
        time.sleep(1)
        for i in range (self.app_agent_processor._args['press_down_times']):
            param = {'function': 'keyboard_input', 'args': {"keys": "{DOWN}"}}
            self.one_step_action(param)
            time.sleep(1)
        # param = {'function': 'keyboard_input', 'args': {"keys": "{UP}"}}
        # self.one_step_action(param)
        # time.sleep(1)
        # param = {'function': 'keyboard_input', 'args': {"keys": "{UP}"}}
        # self.one_step_action(param)
        # time.sleep(1)
        param = {'function': 'keyboard_input', 'args': {"keys": "{ENTER}"}}
        self.one_step_action(param)
        time.sleep(1)
        param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['trace_name_not_equal_to']},
                 'control_text': 'Condition 0 value'}
        self.one_step_action(param)
        time.sleep(1)
        param = {'function': 'click_input', 'args': {"button": "left", "double": False},'control_text': 'OK'}
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