# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.


import json
import time
from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from pywinauto.controls.uiawrapper import UIAWrapper

from ufo import utils
from ufo.agents.processors.actions import (
    ActionExecutionLog,
    ActionSequence,
    BaseControlLog,
    OneStepAction,
)
from ufo.agents.processors.basic import BaseProcessor
from ufo.config.config import Config
from ufo.module.context import Context, ContextNames
from ufo.prompts.graph import knowledge_graph_builder as kgb
import re
import subprocess
import os
import pyautogui

from ufo.utils import print_with_color

configs = Config.get_instance().config_data


if TYPE_CHECKING:
    from ufo.agents.agent.host_agent import HostAgent


@dataclass
class HostAgentAdditionalMemory:
    """
    The additional memory for the host agent.
    """

    Step: int
    RoundStep: int
    AgentStep: int
    Round: int
    ControlLabel: str
    SubtaskIndex: int
    Action: str
    FunctionCall: str
    ActionType: str
    Request: str
    Agent: str
    AgentName: str
    Application: str
    Cost: float
    Results: str
    error: str
    time_cost: Dict[str, float]
    ControlLog: Dict[str, Any]


@dataclass
class HostAgentRequestLog:
    """
    The request log data for the AppAgent.
    """

    step: int
    image_list: List[str]
    os_info: Dict[str, str]
    plan: List[str]
    prev_subtask: List[str]
    request: str
    blackboard_prompt: List[str]
    prompt: Dict[str, Any]


class HostAgentProcessor(BaseProcessor):
    """
    The processor for the host agent at a single step.
    """

    def __init__(self, agent: "HostAgent", context: Context) -> None:
        """
        Initialize the host agent processor.
        :param agent: The host agent to be processed.
        :param context: The context.
        """

        super().__init__(agent=agent, context=context)

        self.host_agent = agent

        self._desktop_screen_url = None
        self._desktop_windows_dict = None
        self._desktop_windows_info = None
        self.bash_command = None
        self.knowledge_graph = kgb.KnowledgeGraph()

    def print_step_info(self) -> None:
        """
        Print the step information.
        """
        utils.print_with_color(
            "Round {round_num}, Step {step}, HostAgent: Analyzing the user intent and decomposing the request...".format(
                round_num=self.round_num + 1, step=self.round_step + 1
            ),
            "magenta",
        )

        #检查是否为host agent第一次运行, 是就打开对应程序
        if self.round_step == 0:
            if any(substring in self.request for substring in ['Radeon', 'AMD Software', 'AMD Settings']):
                app_path = r'C:\Program Files\AMD\CNext\CNext\RadeonSoftware.exe'
                subprocess.Popen([app_path])
                time.sleep(5)

            if any(substring in self.request for substring in ['DSAT']):
                pyautogui.press("win")
                pyautogui.press("D")
                pyautogui.press("S")
                pyautogui.press("A")
                pyautogui.press("T")
                time.sleep(2)
                pyautogui.press("ENTER")
                time.sleep(2)
                pyautogui.press("ENTER")
                # time.sleep(10)
                # pyautogui.press("LEFT")
                # pyautogui.press("ENTER")
                time.sleep(20)

            if any(substring in self.request for substring in ['结果记录CPU']):
                with open('结果记录CPU.txt', 'r+') as file:
                    file.truncate(0)  # 清空文件内容
                txt_path = os.getcwd() + '\结果记录CPU.txt'
                subprocess.Popen(['notepad.exe', txt_path])

            if any(substring in self.request for substring in ['结果记录Disk']):
                with open('结果记录Disk.txt', 'r+') as file:
                    file.truncate(0)  # 清空文件内容
                txt_path = os.getcwd() + '\结果记录Disk.txt'
                subprocess.Popen(['notepad.exe', txt_path])

            if any(substring in self.request for substring in ['结果记录DPC']):
                with open('结果记录DPC.txt', 'r+') as file:
                    file.truncate(0)  # 清空文件内容
                txt_path = os.getcwd() + '\结果记录DPC.txt'
                subprocess.Popen(['notepad.exe', txt_path])

            if any(substring in self.request for substring in ['测试视频', 'test video']):
                mp4_path = os.getcwd() + '\测试视频.mp4'
                os.startfile(mp4_path)

            if any(substring in self.request for substring in ['WPR']):
                process = subprocess.Popen(
                    'start wprui',  # command to run
                    stdout=subprocess.PIPE,  # capture stdout
                    stderr=subprocess.PIPE,  # capture stderr
                    shell=True,
                    text=True,
                    # executable=powershell_path,
                )

    @BaseProcessor.exception_capture
    @BaseProcessor.method_timer
    def capture_screenshot(self) -> None:
        """
        Capture the screenshot.
        """

        desktop_save_path = self.log_path + f"action_step{self.session_step}.png"

        self._memory_data.add_values_from_dict({"CleanScreenshot": desktop_save_path})

        # Capture the desktop screenshot for all screens.
        self.photographer.capture_desktop_screen_screenshot(
            all_screens=True, save_path=desktop_save_path
        )

        # Encode the desktop screenshot into base64 format as required by the LLM.
        self._desktop_screen_url = self.photographer.encode_image_from_path(
            desktop_save_path
        )

    @BaseProcessor.exception_capture
    @BaseProcessor.method_timer
    def get_control_info(self) -> None:
        """
        Get the control information.
        """

        # Get all available windows on the desktop, into a dictionary with format {index: application object}.
        self._desktop_windows_dict = self.control_inspector.get_desktop_app_dict(
            remove_empty=True
        )

        # Get the textual information of all windows.
        self._desktop_windows_info = self.control_inspector.get_desktop_app_info(
            self._desktop_windows_dict
        )

    @BaseProcessor.exception_capture
    @BaseProcessor.method_timer
    def get_prompt_message(self) -> None:
        """
        Get the prompt message.
        """

        if not self.host_agent.blackboard.is_empty():
            blackboard_prompt = self.host_agent.blackboard.blackboard_to_prompt()
        else:
            blackboard_prompt = []

        # Construct the prompt message for the host agent.
        self._prompt_message = self.host_agent.message_constructor(
            image_list=[self._desktop_screen_url],
            os_info=self._desktop_windows_info,
            plan=self.prev_plan,
            prev_subtask=self.previous_subtasks,
            request=self.request,
            blackboard_prompt=blackboard_prompt,
            current_node=self.context.current_node,
        )

        request_data = HostAgentRequestLog(
            step=self.session_step,
            image_list=[self._desktop_screen_url],
            os_info=self._desktop_windows_info,
            plan=self.prev_plan,
            prev_subtask=self.previous_subtasks,
            request=self.request,
            blackboard_prompt=blackboard_prompt,
            prompt=self._prompt_message,
        )

        # Log the prompt message. Only save them in debug mode.
        request_log_str = json.dumps(asdict(request_data), ensure_ascii=False)
        self.request_logger.debug(request_log_str)

    @BaseProcessor.exception_capture
    @BaseProcessor.method_timer
    def get_response(self) -> None:
        """
        Get the response from the LLM.
        """
        successors = list(self.knowledge_graph.graph.successors(self._context.current_node))
        if self.previous_subtasks == []:
            period_index = self.request.find('。')
            CurrentSubtask = self.request[:period_index + 1]
            for i in range(len(successors)):
                if eval(successors[i]).get('Reference_task') == CurrentSubtask:
                    SimilarTask = i + 1
                    self._response = '{\n  "Observation": "",\n  "Thought": "",\n  "CurrentSubtask": ' + '"' + CurrentSubtask + '"' + ',\n  "Message": "",\n  "Similar Task": ' + str(SimilarTask) + ',\n  "ControlLabel": "",\n  "ControlText": "",\n  "Status": "ASSIGN",\n  "Plan": [],\n  "Bash": "",\n  "Questions": [],\n  "Comment": ""\n}'
                    break
        else:
            previous_subtask = self.previous_subtasks[-1]['subtask']
            if previous_subtask in self.request:
                period_index = self.request[self.request.find(previous_subtask) + len(previous_subtask):].find('。')
                CurrentSubtask = self.request[self.request.find(previous_subtask) + len(previous_subtask):][:period_index + 1]
                if len(successors)>1:
                    #只有多分支且无分支完全符合current subtask时调用模型选取similar task
                    for i in range(len(successors)):
                        if eval(successors[i]).get('Reference_task') == CurrentSubtask:
                            SimilarTask = i + 1
                            self._response = '{\n  "Observation": "",\n  "Thought": "",\n  "CurrentSubtask": ' + '"' + CurrentSubtask + '"' + ',\n  "Message": "",\n  "Similar Task": ' + str(SimilarTask) + ',\n  "ControlLabel": "",\n  "ControlText": "",\n  "Status": "ASSIGN",\n  "Plan": [],\n  "Bash": "",\n  "Questions": [],\n  "Comment": ""\n}'
                            break
                elif len(successors)==1:
                    SimilarTask = 1
                    self._response = '{\n  "Observation": "",\n  "Thought": "",\n  "CurrentSubtask": ' + '"' + CurrentSubtask + '"' + ',\n  "Message": "",\n  "Similar Task": ' + str(
                        SimilarTask) + ',\n  "ControlLabel": "",\n  "ControlText": "",\n  "Status": "ASSIGN",\n  "Plan": [],\n  "Bash": "",\n  "Questions": [],\n  "Comment": ""\n}'
                else:
                    SimilarTask = 0
                    self._response = '{\n  "Observation": "",\n  "Thought": "",\n  "CurrentSubtask": ' + '"' + CurrentSubtask + '"' + ',\n  "Message": "",\n  "Similar Task": ' + str(
                        SimilarTask) + ',\n  "ControlLabel": "",\n  "ControlText": "",\n  "Status": "FINISH",\n  "Plan": [],\n  "Bash": "",\n  "Questions": [],\n  "Comment": ""\n}'

        if "SimilarTask" not in locals():
            retry = 0
            while retry < configs.get("JSON_PARSING_RETRY", 3):
                # Try to get the response from the LLM. If an error occurs, catch the exception and log the error.
                self._response, self.cost = self.host_agent.get_response(
                    self._prompt_message, "HOSTAGENT", use_backup_engine=True
                )

                try:
                    self.host_agent.response_to_dict(self._response)
                    break
                except Exception as e:
                    print(f"Error in parsing response into json, retrying: {retry}")
                    retry += 1

    @BaseProcessor.exception_capture
    @BaseProcessor.method_timer
    def parse_response(self) -> None:
        """
        Parse the response.
        """

        self._response_json = self.host_agent.response_to_dict(self._response)
        # 如果任务需求包含(1)(2)(3)等编号，则根据编号设定subtask
        pattern = r'\)(.*?)(?=\(|$)'
        matches = re.findall(pattern, self.request)
        if len(matches) > 1 and '(2)' in self.request:
            self._response_json['CurrentSubtask'] = matches[0]
            formatted_matches = [f"({i}){match.strip()}" for i, match in enumerate(matches[1:], start=1)]
            self._response_json['Plan'] = formatted_matches

        self.subtask = self._response_json.get("CurrentSubtask", "")
        self.host_message = self._response_json.get("Message", [])

        # Convert the plan from a string to a list if the plan is a string.
        self.plan = self.string2list(self._response_json.get("Plan", ""))
        self._response_json["Plan"] = self.plan


        self.question_list = self._response_json.get("Questions", [])

        successors = list(self.knowledge_graph.graph.successors(self._context.current_node))
        if self._response_json.get('Similar Task') and successors:
            self._context.current_node = successors[int(self._response_json.get('Similar Task')) - 1]
        # else:
        #     self._context.current_node = '{"Reference_task": "The user\'s request has been fulfilled."}'
        selected_task = eval(self._context.current_node)
        if 'Corresponding_application' in selected_task:
            self._response_json['ControlText'] = selected_task['Corresponding_application']
            self._response_json["ControlLabel"] = ''
            for i in range(len(self._desktop_windows_dict)):
                if self._desktop_windows_dict[
                    str(i + 1)].element_info.name == self._response_json["ControlText"]:
                    self._response_json["ControlLabel"] = str(i + 1)
                    break
            else:
                print_with_color("Control Text not Found in List", "red")

        if 'Corresponding_application_contain' in selected_task:
            for i in range(len(self._desktop_windows_dict)):
                if selected_task['Corresponding_application_contain'] in self._desktop_windows_dict[str(i + 1)].element_info.name:
                    self._response_json['ControlText'] = self._desktop_windows_dict[str(i + 1)].element_info.name
                    self._response_json["ControlLabel"] = str(i + 1)
                    break
            else:
                selected_task['Corresponding_application'] = ''
                print_with_color("Control Text not Found in List", "red")

        if 'Corresponding_application_contain_list' in selected_task:
            for i in range(len(self._desktop_windows_dict)):
                if any(substring in self._desktop_windows_dict[str(i + 1)].element_info.name for substring in
                       selected_task['Corresponding_application_contain_list']):
                    self._response_json['ControlText'] = self._desktop_windows_dict[str(i + 1)].element_info.name
                    self._response_json["ControlLabel"] = str(i + 1)
                    break
            else:
                selected_task['Corresponding_application'] = ''
                print_with_color("Control Text not Found in List", "red")

        if 'Bash' in selected_task:
            self._response_json['Bash'] = selected_task['Bash']
        self.bash_command = self._response_json.get("Bash", None)

        if 'Status' in selected_task:
            self._response_json['Status'] = selected_task['Status']
        self.status = self._response_json.get("Status", "")

        self.control_text = self._response_json.get("ControlText", "")
        self.control_label = self._response_json.get("ControlLabel", "")

        self.host_agent.print_response(self._response_json)

    @BaseProcessor.exception_capture
    @BaseProcessor.method_timer
    def execute_action(self) -> None:
        """
        Execute the action.
        """

        new_app_window = self._desktop_windows_dict.get(self.control_label, None)

        # If the new application window is available, select the application.
        if new_app_window is not None:
            self._select_application(new_app_window)

        # If the bash command is not empty, run the shell command.
        if self.bash_command:
        #     if any(substring in self.bash_command for substring in ['Radeon','AMD Software','AMD Settings']):
        #         app_path = r'C:\Program Files\AMD\CNext\CNext\RadeonSoftware.exe'
        #         subprocess.run([app_path])
        #
        #         app_path = os.getcwd() + '\结果记录.txt'
        # else:
            self._run_shell_command()
            time.sleep(5)
        # If the new application window is None and the bash command is None, set the status to FINISH.
        if new_app_window is None and self.bash_command is None:
            self.status = self._agent_status_manager.FINISH.value
            return

    def _is_window_interface_available(self, new_app_window: UIAWrapper) -> bool:
        """
        Check if the window interface is available for the visual element.
        :param new_app_window: The new application window.
        :return: True if the window interface is available, False otherwise.
        """
        try:
            new_app_window.is_normal()
            return True
        except Exception:
            utils.print_with_color(
                "Window interface {title} not available for the visual element.".format(
                    title=self.control_text
                ),
                "red",
            )
            return False

    def _is_same_window(self, window1: UIAWrapper, window2: UIAWrapper) -> bool:
        """
        Check if two windows are the same.
        :param window1: The first window.
        :param window2: The second window.
        :return: True if the two windows are the same, False otherwise.
        """

        equal = False

        try:
            equal = window1 == window2
        except:
            pass
        return equal

    def _switch_to_new_app_window(self, new_app_window: UIAWrapper) -> None:
        """
        Switch to the new application window if it is different from the current application window.
        :param new_app_window: The new application window.
        """

        if (
            not self._is_same_window(new_app_window, self.application_window)
            and self.application_window is not None
        ):
            utils.print_with_color("Switching to a new application...", "magenta")

        self.application_window = new_app_window

        self.context.set(ContextNames.APPLICATION_WINDOW, self.application_window)
        self.context.set(ContextNames.APPLICATION_ROOT_NAME, self.app_root)
        self.context.set(ContextNames.APPLICATION_PROCESS_NAME, self.control_text)

    def _select_application(self, application_window: UIAWrapper) -> None:
        """
        Create the app agent for the host agent.
        :param application_window: The application window.
        """

        action = OneStepAction(
            control_label=self.control_label,
            control_text=self.control_text,
            after_status=self.status,
            function="set_focus",
        )

        action.control_log = BaseControlLog(
            control_class=application_window.element_info.class_name,
            control_type=application_window.element_info.control_type,
            control_automation_id=application_window.element_info.automation_id,
        )

        self.actions = ActionSequence([action])

        # Get the root name of the application.
        self.app_root = self.control_inspector.get_application_root_name(
            application_window
        )

        # Check if the window interface is available for the visual element.
        if not self._is_window_interface_available(application_window):
            self.status = self._agent_status_manager.ERROR.value

            return

        # Switch to the new application window, if it is different from the current application window.
        self._switch_to_new_app_window(application_window)
        self.application_window.set_focus()
        if configs.get("MAXIMIZE_WINDOW", False):
            self.application_window.maximize()

        if configs.get("SHOW_VISUAL_OUTLINE_ON_SCREEN", True):
            self.application_window.draw_outline(colour="red", thickness=3)

    def _run_shell_command(self) -> None:
        """
        Run the shell command.
        """
        self.agent.create_puppeteer_interface()
        self.agent.Puppeteer.receiver_manager.create_api_receiver(
            self.app_root, self.control_text
        )

        action = OneStepAction(
            control_label=self.control_label,
            control_text=self.control_text,
            after_status=self.status,
            function="run_shell",
            args={"command": self.bash_command},
        )

        try:
            return_value = self.agent.Puppeteer.execute_command(
                "run_shell", {"command": self.bash_command}
            )
            error = ""
        except Exception as e:
            return_value = ""
            error = str(e)

        action.results = ActionExecutionLog(
            return_value=return_value, status=self.status, error=error
        )

        self.actions: ActionSequence = ActionSequence([action])

    def sync_memory(self):
        """
        Sync the memory of the HostAgent.
        """

        additional_memory = HostAgentAdditionalMemory(
            Step=self.session_step,
            RoundStep=self.round_step,
            AgentStep=self.host_agent.step,
            Round=self.round_num,
            ControlLabel=self.control_label,
            SubtaskIndex=-1,
            FunctionCall=self.actions.get_function_calls(),
            Action=self.actions.to_list_of_dicts(),
            ActionType="Bash" if self.bash_command else "UIControl",
            Request=self.request,
            Agent="HostAgent",
            AgentName=self.host_agent.name,
            Application=self.app_root,
            Cost=self._cost,
            Results=self.actions.get_results(),
            error=self._exeception_traceback,
            time_cost=self._time_cost,
            ControlLog=self.actions.get_control_logs(),
        )

        self.add_to_memory(self._response_json)
        self.add_to_memory(asdict(additional_memory))

    def update_memory(self) -> None:
        """
        Update the memory of the Agent.
        """

        # Sync the memory
        self.sync_memory()

        self.host_agent.add_memory(self._memory_data)

        # Log the memory item.
        self.context.add_to_structural_logs(self._memory_data.to_dict())
        # self.log(self._memory_data.to_dict())

        # Only memorize the keys in the HISTORY_KEYS list to feed into the prompt message in the future steps.
        memorized_action = {
            key: self._memory_data.to_dict().get(key) for key in configs["HISTORY_KEYS"]
        }

        self.host_agent.blackboard.add_trajectories(memorized_action)
