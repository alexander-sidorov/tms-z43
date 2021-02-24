import enum
from pathlib import Path
from string import Template
from typing import Dict
from typing import Optional
from typing import Union

from framework.dirs import DIR_TEMPLATES


class TemplateEngine(enum.Enum):
    STR_FORMAT = 1
    STD_TEMPLATE = 2


def render_template(
    template_path: Union[str, Path],
    context: Optional[Dict] = None,
    *,
    engine_type: TemplateEngine = TemplateEngine.STR_FORMAT,
) -> str:
    template = read_template(template_path)
    context = context or {}

    engines = {
        TemplateEngine.STR_FORMAT: lambda c: template.format(**c),
        TemplateEngine.STD_TEMPLATE: Template(template).safe_substitute,
    }

    engine = engines[engine_type]
    document = engine(context)

    return document


def read_template(template_path: Union[str, Path]) -> str:
    template = DIR_TEMPLATES / template_path

    assert template.is_file(), f"template {template_path!r} is not a file"

    with template.open("r") as fd:
        content = fd.read()

    return content
