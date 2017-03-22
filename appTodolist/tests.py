from django.test import TestCase
from appTodolist.models import Task, TaskList


class TodoTest (TestCase):

    def test_empty(self):
        # arrange
        t = TaskList()
        # act
        # assert
        self.assertTrue(t.is_empty())
    
    def test_get_empty(self):
        # arrange
        t = TaskList()
        # act
        # assert
        self.assertTrue(len(t.get_tasks()) == 0)


    def test_add_task(self):
        '''
        add task, is empty,
        '''
        # arrange
        tasks_list = TaskList()
        tasks_list.save()
        task = Task(name="name!!")
        task.save()
        #act
        tasks_list.add_task(task)
        # assert
        self.assertFalse(tasks_list.is_empty())


class TasksTest (TestCase):

    def test_name(self):
        # arrange
        name = "Name"
        task = Task(name=name)
        # act
        # assert
        self.assertEquals(name, task.name)

    def test_pending(self):
        # arrange
        task = Task(name="Name")
        # act
        # assert
        self.assertFalse(task.done)

    def test_done(self):
        # arrange
        task = Task(name="Name")
        # act
        task.complete()
        # assert
        self.assertTrue(task.done)
