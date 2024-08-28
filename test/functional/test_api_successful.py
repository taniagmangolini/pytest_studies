"""Test the Task data type."""
import pytest
from tasks.api import (
    Task,
    add,
)


@pytest.mark.add_successful
class TestAdd():
    '''Test successful api.add().'''

    def test_add_successful(self):
        new_task_id = add(Task('New task'))
        assert isinstance(new_task_id, int)

    @pytest.mark.parametrize('task', [
        Task(summary='New task 1', owner='eu'),
        Task(summary='New task 2', owner='eu', done=True),
        Task(summary='New task 3', owner='eu', done=False)
    ])
    def test_add_successful_batch(self, task):
        new_task_id = add(task)
        assert isinstance(new_task_id, int)

    @pytest.mark.parametrize('summary, owner, done', [
        ('New task 1', 'eu', None),
        ('New task 2', 'eu', False),
        ('New task 3', 'tu', True),
    ])
    def test_add_successful_batch_with_tuples(self, summary, owner, done):
        new_task_id = add(Task(summary, owner, done))
        assert isinstance(new_task_id, int)

    @pytest.mark.parametrize('task', [
        pytest.param(Task(summary='New task 1', owner='eu'), id='Task 1'),
        pytest.param(Task(summary='New task 2',
                     owner='eu', done=True), id='Task 2'),
        pytest.param(Task(summary='New task 3',
                     owner='eu', done=False), id='Task 3'),
    ])
    def test_add_successful_batch_whits_task_identification(self, task):
        new_task_id = add(task)
        assert isinstance(new_task_id, int)
