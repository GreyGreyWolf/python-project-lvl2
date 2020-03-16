import json
from gen_diff.formatters.to_str import sort_diff


def make_format(diff):
    diff.sort(key=sort_diff)
    return json.dumps(diff) + '\n'
