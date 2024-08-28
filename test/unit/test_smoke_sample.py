"""Test the Task data type."""
import pytest


@pytest.fixture
def dummy_smoke_fixture():
    return {"key1": "value1", "key2": "value2"}


@pytest.mark.usefixtures('dummy_fixture')
@pytest.mark.smoke
def test_some_smoke_test():
    ''' Run pytest -v -m smoke to run tests marked as smoke'''
    with pytest.raises(TypeError):
        list(1)


@ pytest.mark.smoke
def test_another_smoke_test(dummy_smoke_fixture):
    ''' Run pytest -v -m smoke to run tests marked as smoke'''
    assert dummy_smoke_fixture['key1'] == 'value1'


def test_environment(environment):
    assert environment in ["dev", "staging", "prod"]


def test_print(x=1):
    '''Run pytest with -s to see the prints'''
    print('PRINTED')
