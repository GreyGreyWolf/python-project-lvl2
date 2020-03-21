from gen_diff.format.json import format as json
from gen_diff.format.plain import format as plain
from gen_diff.format.default import format as default


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)
