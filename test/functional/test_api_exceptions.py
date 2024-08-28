import pytest
from tasks.api import (
    Task,
    start_tasks_db,
    add,
    update,
    TaskNotFoundException,
)


def test_start_db():
    with pytest.raises(ValueError) as exc:
        start_tasks_db('/some/great/path', 'mysql')
    exc_message = exc.value.args[0]
    assert exc_message == "db_type must be a 'tiny'"


class TestUpdate():
    '''Test api.update() exceptions.'''

    def test_bad_id(self):
        with pytest.raises(TaskNotFoundException):
            update(0, Task('some task'))


class TestAdd():
    '''Test api.add() exceptions.'''

    def test_add_raises(self):
        with pytest.raises(TypeError):
            add(task='not a task')

    @pytest.mark.skip('skipped because the db is being initilized by the fixtures')
    def test_add_raises_unitiliazed_db(self):
        '''Run pytest -rs to see the sḱipped tests.'''
        with pytest.raises(ValueError):
            add(Task('New task'))

    @pytest.mark.xfail
    def test_add_raises_unitiliazed_db_fail(self):
        '''This task should fail because the db is being initialized by the fixtures.'''
        with pytest.raises(ValueError):
            add(Task('New task'))
