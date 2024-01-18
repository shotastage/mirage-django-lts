from mirage.core import Void
from mirage import system as mys

class WorkflowNext:

    def __init__(self, parser):
        self.inherited = parser
        self.action = self.inherited[0]
        self.subaction = self.inherited[1]
        self.option = self.inherited[2]
        self.option_detail = self.inherited[3]
        self.values = self.inherited[4]
        self.step_flows = []

    def get_first_arg(self) -> str:
        if not self.values:
            raise ValueError("No values provided")
        return self.values[0]

    def register(self, flow) -> Void:
        self.step_flows.append(flow)

    def main(self) -> bool:
        # Main flow struct
        return True

    def run(self) -> Void:
        if not self.main():
            return

        for flow in self.step_flows:
            try:
                flow.run()
            except Exception as e:
                mys.log(f"Error running flow: {e}", withError=True)
                raise

class StepFlow:
    def __init__(self, parser):
        self.inherited = parser
        self.action = parser.action
        self.subaction = parser.subaction
        self.option = parser.option
        self.option_detail = parser.option_detail
        self.values = parser.values
        self.flows = []

    def add(self, func) -> Void:
        self.flows.append(func)

    def run(self) -> Void:
        for flow in self.flows:
            try:
                flow()
            except Exception as e:
                mys.log(f"Error in step flow: {e}", withError=True)
                raise
