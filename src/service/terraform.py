from logging import getLogger


logger = getLogger("src").getChild(__name__)

class TerraformService():
    def __init__(self) -> None:
        pass

    def search_query(json: dict, dep: str):
        dep_array = name.split('.')
        module = ""
        type   = ""
        name   = ""
        # data module
        if 'data' in dep_array and dep_array[0] == 0:
            type = dep_array[0]
            name = dep_array[1]        
        # module
        elif dep_array[0] == 'module':
            module = dep_array[0] + dep_array[1]
            type = dep_array[2]
            name = dep_array[3]
        # other
        else:
            type = dep_array[0]
            name = dep_array[1]
        

    def lookup_dependencies(json: dict, name: str):

        
