from django.test import TestCase
from appTodolist.models import Task, TaskList



class TodoTest (TestCase):
    
    def test_empty(self):
        #arrange
        t = TaskList()
        #act
        #assert
        self.assertTrue(t.is_empty())
        
    def test_add_task(self):
        '''
        add task, is empty, 
        '''
        #arrange
        tasks_list = TaskList()
        tasks_list.save()
        task = Task(name="name!!")
        task.save()
        #act
        tasks_list.add_task(task)
        #assert
        self.assertFalse(tasks_list.is_empty())
        