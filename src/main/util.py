from pathlib import Path
from typing import Dict
from typing import Optional
from typing import Union

from framework.dirs import DIR_TEMPLATES


def render_template(
    template_path: Union[str, Path],
    context: Optional[Dict] = None,
) -> str:
    template = read_template(template_path)
    context = context or {}
    document = template.format(**context)
    return document


def read_template(template_path: Union[str, Path]) -> str:
    template = DIR_TEMPLATES / template_path

    assert template.is_file(), f"template {template_path!r} is not a file"

    with template.open("r") as fd:
        content = fd.read()

    return content
