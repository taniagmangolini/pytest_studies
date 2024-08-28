# share fixtures among multiple test files
import os
import pytest
from tasks.api import (
    delete_all,
    start_tasks_db,
    stop_tasks_db,
)


def pytest_addoption(parser):
    '''Add a custom command-line option to pytest.'''
    parser.addoption('--env',
                     action='store',
                     help='set the environment(dev, homolog, prod)',
                     default='dev'
                     )


@pytest.fixture(scope='session')
def environment(request):
    return request.config.getoption("--env")


""" @pytest.fixture(autouse=True, scope='function')
def initialize_db(tmpdir):
    ''' Initialize the dependendencies.
    Fixtures params:
    - tmpdir is a builtin fixture that works with function scope.
    - fixture autouse: indicates that all tests below use this fixture.
    - fixture scope: function , class , module , or session. 
    Default: function (Run once per test function).
    Fixtures can only depend on other fixtures of their same scope or wider.
    To see the fixtures running use the param --setup-show.
    '''
    #
    start_tasks_db(str(tmpdir), 'tiny')
    yield
    stop_tasks_db() """


@pytest.fixture(autouse=True, scope='session', params=['tiny'])
def initialize_db_session_scoped(environment, tmpdir_factory, request):
    ''' Initialize the dependendencies.
    Fixtures params:
    - tmpdir is a builtin fixture that works with session scope.
    - fixture autouse: indicates that all tests below use this fixture.
    - fixture scope: function , class , module , or session. 
    - params: run fixture one time for each param.
    Default: function (Run once per test function).
    Fixtures can only depend on other fixtures of their same scope or wider.
    To see the fixtures running use the param --setup-show.
    '''
    #
    tmpdir = tmpdir_factory.mktemp('temp')
    start_tasks_db(str(tmpdir), request.param)
    create_temp_files(tmpdir)
    yield
    stop_tasks_db()


def create_temp_files(tmpdir):
    '''Create temp files in the temp directory.
    To specify a disered base directory run pytest 
    with --basetemp=my_base_dir.'''
    a_file = tmpdir.join('file.txt')
    a_file.write('testing something...')
    assert a_file.read() == 'testing something...'


@pytest.fixture
def clean_db(create_temp_files):
    delete_all()


@pytest.fixture
def clean_db(initialize_db_session_scoped):
    delete_all()


@pytest.fixture(scope='function')
def dummy_fixture():
    pass
