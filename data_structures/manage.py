import  all_files
import sys
import os

def generate_test_file(module_name:str, *args, **kwargs) -> None:
    # TODO: generate test functions for each custom 'public' method on a class.
    module = getattr(all_files, module_name) 
    entity = getattr(module, module_name, None)
    entity_name = module_name
    if not entity:
        entity_name = to_camelcase(module_name)
        entity = getattr(module, entity_name, None)
    if not entity:
        print(entity_name, module_name)
        raise Exception("Error")
    entity_test_classname = f"Test{entity_name}"
    with open(f"./{module_name}_test.py", "w") as test_file:
        test_file.writelines([
            "import unittest\n",
            f"from {module_name} import {entity_name}\n\n"
            f"class {entity_test_classname}(unittest.TestCase):\n",
            f'\tdef test_{module_name}(self):\n\t\t""" test {entity_name} """',
            "\n\n",
            'if __name__ == "__main__":\n',
            "\tunittest.main()"
        ])

def generate_test_files() -> None:
    files = [a.replace(".py", "") for a in os.listdir(os.getcwd()) if ".py" in a]
    filtered_files = [a for a in files if not any([k in a for k in ("all_files", "_test", "manage", "utils")])]
    for file_name in filtered_files:
        if not os.path.exists(f"{file_name}_test.py"):
            generate_test_file(file_name)

def test() -> None:
    test_files = [a for a in os.listdir(os.getcwd()) if "_test" in a]
    for test_file in test_files:
        os.system(f"python3 {test_file}")

def to_camelcase(val:str) -> str:
    return "".join([a.capitalize() for a in val.split("_")])


if __name__ == "__main__":
    args = sys.argv
    action = args[1]
    thismodule = sys.modules[__name__]
    function = getattr(thismodule, action)
    function(*args[2:])