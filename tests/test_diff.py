import pytest
import yaml
import json
from gen_diff import engine, parsers
from gen_diff.formatting import to_str


def reader(file):
    with open(file, 'r') as input_file:
        answer = input_file.read()
    return answer


def test_answer():
    assert reader(
        './tests/fixtures/result.txt') == engine.engine_diff(
                                        './tests/fixtures/before.json',
                                        './tests/fixtures/after.json',
                                        to_str.make_format)
    assert yaml.safe_load(open('./tests/fixtures/before.yml')) == parsers.parser('./tests/fixtures/before.yml')
    assert isinstance(engine.engine_diff(
        './tests/fixtures/before.yml', 
        './tests/fixtures/after.yml',
        to_str.make_format), str)
    assert reader('./tests/fixtures/recursion_result.txt') == engine.engine_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        to_str.make_format)
