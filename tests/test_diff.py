import pytest
import yaml
import json
from gen_diff import engine, parsers
from gen_diff.formatters import to_str, to_text, to_json


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
    assert yaml.safe_load(open(
        './tests/fixtures/before.yml')) == parsers.parser(
            './tests/fixtures/before.yml')
    assert isinstance(engine.engine_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml',
        to_str.make_format), str)
    assert reader(
        './tests/fixtures/recursion_result.txt') == engine.engine_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        to_str.make_format)
    assert reader('./tests/fixtures/text_result.txt') == engine.engine_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        to_text.make_format)
    assert reader('tests/fixtures/json_result.json') == engine.engine_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        to_json.make_format)
