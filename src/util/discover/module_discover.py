import os
from typing import List


def discover_python_modules() -> List[str]:
    """
    This is find every .py file in project template architecture.
    Some of the path excepted, cause of Circular reference.
    :return: module names
    """
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(current_file_path))
    if len(project_root.split("src")) != 1:
        project_root = project_root.split("src")[0] + "src"

    modules = []
    for dirpath, _, filenames in os.walk(project_root):
        for filename in filenames:
            if filename.endswith(".py") and filename != "__init__.py":
                file_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(file_path, project_root)
                module_path = relative_path.replace(os.path.sep, ".").rsplit(".", 1)[0]
                modules.append(module_path)

    return [
        module
        for module in modules
        if module[: module.find(".")]
        not in ["container", "main", "core", "domain", "logs"]
        and module != "main"
    ]
