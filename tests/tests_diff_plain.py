import pytest
from gen_diff import engine

def reader(file):
    with open(file, 'r') as input_file:
        answer = input_file.read()
    return answer


def test_answer():
    assert reader('./tests/fixtures/result.txt') == engine.engine_diff('./tests/fixtures/before.json',
                                                                       './tests/fitures/after.json')