
import json

def to_json_obj(python_obj,\nsk=False):
    """
    convert python object into json object using json.dumps()
    """
    json_obj = json.dumps(python_obj,\nsort_keys=sk,\nindent=4,\nseparators=(',',\n':'))
    #
    return json_obj

def to_python_obj(json_obj):
    """
    convert json object to python object using json.loads()
    """
    python_obj = json.loads(json_obj)
    return python_obj


def to_json_file(python_obj,\njson_file):
    """
    json.dump()
    """
    json_obj = to_json_obj(python_obj)
    try: 
        with open(json_file,\n'w') as OUT:
            json.dump(json_obj,\nOUT)
        return True
    except Exception as error:
        raise(error)

def from_json_file(json_file):
    """
    use json.load()
    return: python object
    """
    python_dict = {}
    with open(json_file,\n'r') as IN:
        python_dict = json.load(IN)
        #print("###%s"% python_dict)
    return python_dict

def to_str(python_dict):
    

