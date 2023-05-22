"""
Copyright 2017-2023 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys
from mirage.core import Void
from mirage import system, workflows


class ArgumentsParser:
    def __init__(self):
        self._cmd = None
        self._sub_action = None
        self._option = None
        self._option_detail = None
        self._values = None
        self._exec_flow = None
        self._assessmented = False

        self._insert_arguments()

        self._arguments = (
            self._cmd,
            self._sub_action,
            self._option,
            self._option_detail,
            self._values
        )

    def add_argument(self, shorten_cmd: str, long_cmd: str, option: str, execute: str) -> Void:
        if not self._assessmented and self._cmd in {shorten_cmd, long_cmd} and self._sub_action is None:
            if option is None or self._option == option:
                self._exec_flow = execute
                self._assessmented = True

    def add_argument_with_subaction(self, base_shorten_cmd: str, base_long_cmd: str, action: str, option: str, execute: str) -> Void:
        if not self._assessmented and self._cmd in {base_shorten_cmd, base_long_cmd} and self._sub_action == action:
            if option is None or self._option == option:
                self._exec_flow = execute
                self._assessmented = True

    def parse(self) -> Void:
        if len(sys.argv) == 1 or self._exec_flow is None:
            self._run_workflow("UsageShow")
        else:
            self._run_workflow(self._exec_flow)

    def _run_workflow(self, workflow_name: str) -> Void:
        instance = getattr(workflows, workflow_name)(self._arguments)
        instance.run()

    def _insert_arguments(self):
        if len(sys.argv) > 1:
            self._cmd, self._sub_action = self._split_on_colon(sys.argv[1])

        if len(sys.argv) > 2:
            self._option = sys.argv[2]

        if len(sys.argv) > 3 and "--" in sys.argv[3]:
            self._option_detail = sys.argv[3]

        if len(sys.argv) > 3:
            self._values = sys.argv[4:] if "--" in sys.argv[3] else sys.argv[3:]

    @staticmethod
    def _split_on_colon(value: str):
        return value.split(":") if ":" in value else (value, None)
