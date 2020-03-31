import pytest
import yaml
import json
import os
from gen_diff import engine
from gen_diff.parser import get_data_from
from gen_diff import format


def read(file):
    with open(file, 'r') as input_file:
        answer = input_file.read()
    return answer


def test_answer():
    assert read(
        './tests/fixtures/result.txt') == format.default(
                                        engine.get_diff(
                                         './tests/fixtures/before.json',
                                         './tests/fixtures/after.json'
                                         ))
    assert yaml.safe_load(open(
        './tests/fixtures/before.yml')) == get_data_from(
            './tests/fixtures/before.yml')
    assert isinstance(format.default(
        engine.get_diff(
         './tests/fixtures/before.yml',
         './tests/fixtures/after.yml'
         )), str)
    assert read(
        './tests/fixtures/recursion_result.txt') == format.default(
        engine.get_diff(
         './tests/fixtures/complex_before.json',
         './tests/fixtures/complex_after.json'))
    assert read('./tests/fixtures/text_result.txt') == format.plain(
        engine.get_diff(
         './tests/fixtures/complex_before.json',
         './tests/fixtures/complex_after.json'))
    assert json.load(
        open(os.path.join(os.getcwd(), 'tests/fixtures/json_result.json'), 'r')) == json.loads(
            format.json(engine.get_diff(
                './tests/fixtures/before.json',
                './tests/fixtures/after.json')))
