from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time

from ufo.utils import print_with_color

configs = Config.get_instance().config_data


class DeleteDuplicates:
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor

    def delete_duplicates(self):
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
        for i in range(len(self.app_agent_processor._args['choosing_texts_list'])):
            param = {'function': 'set_edit_text', 'args': {"text": self.app_agent_processor._args['choosing_texts_list'][i]}, 'control_text': 'Find what:'}
            self.one_step_action(param)
            time.sleep(1)
            param = {'function': 'click_input', 'args': {"button": "left", "double": True}, 'control_text': 'Find Next'}
            self.one_step_action(param)
            time.sleep(1)

            all_duplicates_deleted = False
            while not all_duplicates_deleted:
                param = {'function': 'click_input', 'args': {"button": "left", "double": False},
                         '#th UI after control text ##': '-1', 'control text ##': 'Replace All'}
                self.one_step_action(param)
                ui_control_list = (
                    self.app_agent_processor.control_inspector.find_control_elements_in_descendants(
                        self.app_agent_processor.application_window,
                        control_type_list=configs.get("CONTROL_LIST", []),
                        class_name_list=configs.get("CONTROL_LIST", []),
                    )
                )
                for i in range(len(ui_control_list)):
                    if ui_control_list[i].element_info.name == 'No' or ui_control_list[i].element_info.name == 'OK':
                        if ui_control_list[i].element_info.name == 'No':
                            param = {'function': 'click_input', 'args': {"button": "left", "double": True},
                                     'control_text': 'No'}
                        else:
                            param = {'function': 'click_input', 'args': {"button": "left", "double": True},
                                     'control_text': 'OK'}
                        self.one_step_action(param)
                        all_duplicates_deleted = True
                        break

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
