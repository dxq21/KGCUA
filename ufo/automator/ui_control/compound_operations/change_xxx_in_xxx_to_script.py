from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time

from ufo.utils import print_with_color

configs = Config.get_instance().config_data


class ChangeXXXinXXXtoScript:
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor
        self.all_script_changed = False

    def change_xxx_in_xxx_to_subscript(self):
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

        while not self.all_script_changed:
            param = {'function': 'keyboard_input', 'args': {"keys": "{VK_CONTROL}f"}}
            self.one_step_action(param)
            time.sleep(1)

            param = {"control_text": "Search document", 'function': 'set_edit_text',
                     'args': {"text": self.app_agent_processor._args['string to select']}}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'click_input', 'args': {"button": "left", "double": False},
                     'control_text': 'Next Result'}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'click_input', 'args': {"button": "left", "double": False},
                     'control_text': 'Close pane'}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'keyboard_input', 'args': {"keys": "{LEFT}"}}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'keyboard_input', 'args': {"keys": "{VK_CONTROL}f"}}
            self.one_step_action(param)
            time.sleep(1)

            param = {"control_text": "Search document", 'function': 'set_edit_text',
                     'args': {"text": self.app_agent_processor._args['substring to subscript']}}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'click_input', 'args': {"button": "left", "double": False},
                     'control_text': 'Next Result'}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'click_input', 'args': {"button": "left", "double": False},
                     'control_text': 'Close pane'}
            self.one_step_action(param)
            time.sleep(1)

            param = {'function': 'keyboard_input', 'args': {"keys": "{VK_CONTROL}{VK_SHIFT}-"}}
            self.one_step_action(param)
            time.sleep(1)


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
        if ui_control_list[5].element_info.name[7:ui_control_list[5].element_info.name.find('o')-1] == ui_control_list[5].element_info.name[ui_control_list[5].element_info.name.find('o')+3:]:
            self.all_script_changed = True
        if 'control_text' in param:
            param['control_label'] = ''
            for i in range(len(ui_control_list)):
                if ui_control_list[i].element_info.name == param['control_text']:
                    param['control_label'] = str(i + 1)
                    break
            else:
                print_with_color("Control Text not Found in List", "red")
        elif "#th UI after control text ##" in param:
            for i in range(len(ui_control_list)):
                if ui_control_list[i].element_info.name == param['control text ##']:
                    param['control_label'] = str(i + 1  + int(param['#th UI after control text ##']))
                    param['control_text'] = annotation_dict[param['control_label']].element_info.name
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
