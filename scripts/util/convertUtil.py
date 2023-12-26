

import re

def name_convert_to_camel(name: str) -> str:
    """下划线转驼峰"""
    contents = re.findall('_[a-z]+', name)
    for content in set(contents):
        name = name.replace(content, content[1:].title())
    return name


def name_convert_to_snake(name: str) -> str:
    """驼峰转下划线"""
    if re.search(r'[^_][A-Z]', name):
        name = re.sub(r'([^_])([A-Z][a-z]+)', r'\1_\2', name)
        return name_convert_to_snake(name)
    return name.lower()


def name_convert(name: str) -> str:
    """驼峰式命名和下划线式命名互转"""
    name = name.lower()
    is_camel_name = True  # 是否为驼峰式命名
    if re.match(r'[a-z][_a-z]+$', name):
        is_camel_name = False
    elif re.match(r'[a-zA-Z]+$', name) is None:
        raise ValueError(f'Value of "name" is invalid: {name}')
    return name_convert_to_snake(name) if is_camel_name else name_convert_to_camel(name)


