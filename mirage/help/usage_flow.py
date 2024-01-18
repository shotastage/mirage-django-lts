from mirage.core import Void
from mirage.flow import Workflow
from mirage.help import description, description_long

class UsageShowWorkFlow(Workflow):

    def main(self) -> Void:
        if self._option == "--detail":
            print(description_long.usage_doc())
        else:
            print(description.usage_doc())


class VersionShowWorkFlow(Workflow):

    def main(self) -> Void:
        print(description.version_doc())
