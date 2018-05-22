# New Python Mirage Configuration


```
from mirage import system as mys
from mirage.core import Void
from mirage.confscript import ConfigScript
from mirage.confscript.settings import Settings


MIRAGE_CONFIG_SCRIPT_VERSION = "0.0.1"
MIRAGE_CONFIG_DEFAULT_CLASS = "MirageConfig"


class MirageConfig(ConfigScript):

    BASIC_PROJECT = {
        "NAME": "PINNA",
        "VERSION": "0.0.1",
        "AUTHOR": "Shota Shimazu <hornet.live.mf@gmail.com>",
        "GIT_URL": "git@hplab.work:pinna-music/pinna-music.git",
        "LICENSE": Settings.License.MIT,
        "DESCRIPTION": "MUSIC ON THE MAP!",
    }

    DJANGO_PROJECT = {
        "path": "PINNA",
        "module": "PINNA",
        "package": Settings.PackageManager.pipenv,
        "database": Settings.Database.PostgreSQL,
    }

    FRONT_END_PROJECT = {
        "path": "shell",
        "package": "yarn",
        "builder": "webpack",
    }

    COPYRIGHT = {
        "start_year": 2018,
        "license_doc": "https://github.com/shotastage/mirage/blob/master/LICENSE",
        "copyrightors": [
            "Shota Shimazu",
        ]
    }



    def initialize(self) -> Void:
        mys.log("PINNA Setting Script V0.0.1")


    def main(self) -> int:
        self.register_custom_command("custom_cli", None, "tools/scripts/cli.py")
        self.register_custom_command_with_runtime("custom_cli_rb", "tools/scripts/ruby.rb", "ruby")

        return 0


    def deinitialize(self) -> Void:
        mys.log("Bye : )")

```
