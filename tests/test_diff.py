import pytest
import yaml
import json
from gen_diff.parsers import parser
from gen_diff.engine import get_diff
from gen_diff.format import default, plain, json


def read(file):
    with open(file, 'r') as input_file:
        answer = input_file.read()
    return answer


def test_answer():
    assert read(
        './tests/fixtures/result.txt') == get_diff(
                                        './tests/fixtures/before.json',
                                        './tests/fixtures/after.json',
                                        default.format)
    assert yaml.safe_load(open(
        './tests/fixtures/before.yml')) == parser(
            './tests/fixtures/before.yml')
    assert isinstance(get_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml',
        default.format), str)
    assert read(
        './tests/fixtures/recursion_result.txt') == get_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        default.format)
    assert read('./tests/fixtures/text_result.txt') == get_diff(
        './tests/fixtures/complex_before.json',
        './tests/fixtures/complex_after.json',
        plain.format)
    assert read('tests/fixtures/json_result.json') == get_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        json.format)
