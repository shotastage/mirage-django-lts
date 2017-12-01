from djconsole.console import log
from djconsole.generate.model_template import create_model_py

def dj_model_flow(third_args):

    model_classies = third_args[0]

    log("Creating model class " + model_classies + ".")

    model_contents = third_args[1:len(third_args)]        
    model_body = __make_model_body(model_contents)

    modelpy = create_model_py(model_classies, model_body)

    try:
        with open("models.py", "w") as writing:
            writing.write(modelpy)
    except:
        log("Failed to open models.py", withError = True)


def __make_model_body(model_contents):

    body = ""

    for content in model_contents:

        data_name = content.split(":")[0]
        data_type = content.split(":")[1]

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
