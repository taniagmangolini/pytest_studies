from click.testing import CliRunner

from contextlib import contextmanager

import pytest

from tasks.api import Task

import tasks.cli

import tasks.config


@contextmanager
def stub_tasks_db():
    yield


def test_list_no_args(mocker):
    '''mocker is an interface to unittest.mock.'''

    mocker.patch.object(tasks.cli, '_tasks_db', new=stub_tasks_db)
    mocker.patch.object(tasks.cli.api, 'list_tasks', return_value=[])
    runner = CliRunner()
    result = runner.invoke(tasks.cli.tasks_cli, ['list'])
    expected_output = '  ID      owner  done summary\n  --      -----  ---- -------\n'
    assert result.output == expected_output
    tasks.cli.api.list_tasks.assert_called_once_with(None)
