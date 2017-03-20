from django.test import TestCase
from appTodolist.models import *

# Create your tests here!

class Task:
    def __init__(self, name):
        self.name = name
        self.done = False
        
class TasksList:
    def __init__(self):
        self.tasks = []
        
    def is_empty(self):
        return len(self.tasks) == 0
        
    def add_task(self, new_task):
        self.tasks.append(new_task)
        
    def size(self):
        return len(self.tasks)
        
class TodoTest (TestCase):
    
    def test_empty(self):
        #arrange
        t = TasksList()
        #act
        #assert
        self.assertTrue(t.is_empty())
        
    def test_add_task(self):
        '''
        add task, is empty, 
        '''
        #arrange
        tasks_list = TasksList()
        task = Task(name="name!!")
        #act
        tasks_list.add_task(task)
        #assert
        self.assertFalse(tasks_list.is_empty())
        self.assertEquals(1, tasks_list.size())
        #self.assertEquals(task, tasks_list.get_last())
    
    def test_weird_encoding(self):
        flag = False
        #arrange
        tasks_list = TasksList()
        try:
            task = Task(name="ñ")
        except:
            flag = True
        #act
        tasks_list.add_task(task)
        #assert
        assertTrue(flag)
    
    '''
    def test_list_tasks(self):
        #arrange
        t1 = Task.objects.create(name="Task 1")
        t2 = Task.objects.create(name="Task 2")
        t3 = Task.objects.create(name="Task 3")
        #act
        tasks = Task.objects.all()
        #assert
        self.assertEquals([t1, t2, t3], list(Task.objects.all()))
        
     '''