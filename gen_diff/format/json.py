import json
from gen_diff.format.default import sort_diff


def format(diff):
    diff.sort(key=sort_diff)
    return json.dumps(diff)
