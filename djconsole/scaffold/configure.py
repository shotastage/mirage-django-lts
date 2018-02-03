from djconsole.project import load_djfile

def get_all_conf():
    return load_djfile()

def get_app_name():
    data = load_djfile()
    return data["project"]["name"]

def get_app_ver():
    data = load_djfile()
    return data["project"]["version"]


def get_proj_config(conf_name):

    data = None

    try:
        data = load_djfile()
    except:
        return "Invalid DjFile"

    if conf_name == "all":
        return data
    elif conf_name == "name":
        return data["project"]["name"]
    elif conf_name == "version":
        return data["project"]["version"]
    elif conf_name == "author":
        return data["project"]["author"]
    elif conf_name == "git":
        return data["project"]["git"]
    elif conf_name == "license":
        return data["project"]["license"]
    elif conf_name == "description":
        return data["project"]["description"]
    elif conf_name == "iyashi":
        try:
            return data["additional_options"]["iyashi"]
        except:
            return False






"""
{'project': {'name': 'sample', 'version': '0.0.1', 'author': 'Shota Shimazu', 'git': 'https://github.com/shotastage/django-console.git', 'license': 'restricted', 'description': 'This is template!'}, 'django': {'path': 'sample', 'package': 'pipenv'}, 'frontend': {'path': 'shell', 'package': 'yarn'}, 'djworkspace': {'path': '.djc'}}
"""
