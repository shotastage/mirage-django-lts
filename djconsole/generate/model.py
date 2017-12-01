import os
from djconsole.console import log
from djconsole.generate.model_template import create_model_py

def dj_model_flow(third_args):

    model_classies = third_args[0]
    model_contents = third_args[1:len(third_args)]        
    model_body = __make_model_body(model_contents)

    modelpy = create_model_py(model_classies, model_body)


    if os.path.isfile("manage.py"):
        log("Please generate model inside the Django app directory.", withError = True)


    try:
        with open("models.py", "a") as writing:
            writing.write(modelpy)
    except:
        log("Failed to open models.py", withError = True)


def __make_model_body(model_contents):

    body = ""

    for content in model_contents:

        data_name = content.split(":")[0]
        data_type = content.split(":")[1]

        try:
            ___data_name_validator(data_name)
        except:
            log("The data name is invalid!", withError = True)
        

        if "string" == data_type:
            body += '    {0}\n'.format(__model_string(data_name))
        elif "text" == data_type:
            body += '    {0}\n'.format(__model_text(data_name))
        elif "integer" == data_type:
            body += '    {0}\n'.format(__model_integer(data_name))
        else:
            log("Unsuported type " + data_type + ".", withError = True)

    return body


def __model_string(name):
    return '{0} = models.CharField(max_length=255)'.format(name)

def __model_text(name):
    return '{0} = models.CharField(max_length=65536)'.format(name)

def __model_integer(name):
    return '{0} = models.IntegerField()'.format(name)


def ___data_name_validator(name):
    forbiddens = ["from"]

    for word in forbiddens:
        if name == word:
            raise ValueError("This data name is forbidden.")
