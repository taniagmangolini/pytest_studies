import os
from utils.calculator import Calculator
from unittest.mock import Mock
import tasks.api as api


def test_set_env(tmpdir, monkeypatch):
    '''Use monkeypatch.setenv to set an env variable.'''
    expected = 'Test'
    fake_home_dir = 'home'
    monkeypatch.setenv('HOME', tmpdir.mkdir(fake_home_dir))
    full_path = os.path.expanduser('~/file.json')
    with open(full_path, 'w') as f:
        f.write(expected)
    with open(full_path, 'r') as f:
        assert f.readline() == expected


def test_use_calculator(monkeypatch):
    ''' Use monkeypatch.setattr to mock to replace Calculator.add.'''

    def mock_add(self, a, b):
        return 10

    monkeypatch.setattr("utils.calculator.Calculator.add", mock_add)

    calc = Calculator()
    result = calc.add(1, 2)
    assert result == 10


def test_get_api_key(monkeypatch):
    '''Use monkeypatch.setitem to set an environment variable.'
    This method can be used to change dicts.'''
    monkeypatch.setitem(os.environ, 'API_KEY', 'mykey')
    assert os.environ['API_KEY'] == 'mykey'


def test_get_api_key(monkeypatch):
    '''Monkeypath can be used in conjuction with unittest.mock.'''
    mock_response = Mock()
    return_value = {'summary': 'test'}
    mock_response.json.return_value = return_value

    def mock_get(task_id):
        return mock_response.json()

    monkeypatch.setattr("tasks.api.get", mock_get)

    task = api.get(task_id=154354)
    assert task == return_value
