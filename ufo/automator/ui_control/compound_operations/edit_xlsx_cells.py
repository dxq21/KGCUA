from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time
import warnings
from ufo.utils import print_with_color
from pywinauto import Application, findwindows
import pyperclip

configs = Config.get_instance().config_data

class EditXlsxCells(object):
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor

    def edit_xlsx_cells(self):

        target_cells = self.app_agent_processor._args['target_cells']
        target_cells_values = self.app_agent_processor._args['target_cells_values']

        for i in range(len(target_cells)):

            param = {"#th UI after control text ##": -1, "control text ##": "Function Wizard", 'function': 'set_edit_text', 'args': {"text": target_cells[i]}}
            self.one_step_action(param)
            time.sleep(1)

            param = {"#th UI after control text ##": 10, "control text ##": "Function Wizard",
                     'function': 'set_edit_text', 'args': {"text": target_cells_values[i]}}
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