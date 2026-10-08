from ufo.agents.processors.actions import ActionSequence, BaseControlLog, OneStepAction
from ufo.config.config import Config
import time
import warnings
from ufo.utils import print_with_color

configs = Config.get_instance().config_data

class CheckAvailable:
    def __init__(self, app_agent_processor, **kwargs):
        self.app_agent_processor = app_agent_processor

    def check_available(self):
        """
        目标UI检测是否存在
        :params: 字典类型，包含'timeout'（检测时间）和'interval'（检测间隔）
        """
        timeout = self.app_agent_processor._args['timeout']
        retry_interval = self.app_agent_processor._args['retry_interval']
        control_is_available = False
        while not control_is_available:
            ui_control_list = (
                self.app_agent_processor.control_inspector.find_control_elements_in_descendants(
                    self.app_agent_processor.application_window,
                    control_type_list=configs.get("CONTROL_LIST", []),
                    class_name_list=configs.get("CONTROL_LIST", []),
                )
            )
            for i in range(len(ui_control_list)):
                if ui_control_list[i].element_info.name == self.app_agent_processor._args['control_text']:
                    control_is_available = True
                    break
            time.sleep(retry_interval)
            timeout -= retry_interval
            if timeout <= 0:
                warnings.warn(f"Timeout: {self.app_agent_processor._args['control_text']} is not available.")
                break