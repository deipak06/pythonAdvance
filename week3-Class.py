# Classes & OOP — Staged Breakdown
import json

class Task:
    def __init__(self,task_id,name,description,status=False):
        self.name= name
        self.description=description
        self.id=task_id
        self.status=status

    def mark_done(self,status):
        self.status = status
        
    def __str__(self):
        return (f"{self.id} {self.name} {self.description} {self.status}")
    

class TodoList:

    def __init__(self):
        self.tasks = []
        self.next_id = 0

    def add_task(self,name,description):
            self.next_id +=1
            new_task= Task(self.next_id,name,description)
            self.tasks.append(new_task)
    
    def list_task(self):
         for details in self.tasks:
              print(f"{details}")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id==task_id:
                self.tasks.remove(task)
                return
        print(f" task_id {task_id} doesn't exist")
        
    def mark_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_done(True)
                return
        print(f"id doesn't belong for status" )

    def save(self):
        tasks_as_dicts = []
        for task in self.tasks:
            task_dict={"id":task.id,
                       "name":task.name,
                       "description":task.description,
                       "status":task.status
                }
            tasks_as_dicts.append(task_dict)
        
        with open("tasks_list.json","w") as file:
            json.dump(tasks_as_dicts,file)

        
        
    

my_list = TodoList()
# print(my_list.tasks)       # should print []
# print(my_list.next_id)     # should print 0
my_list.add_task("Buy milk", "Get 2% milk")
my_list.add_task("Walk dog", "Evening walk")
my_list.add_task("Buy bread", "Get sourdough")

my_list.mark_done(2)
my_list.save()
my_list.list_task()


# print(my_list.tasks)            # what do you expect this to show?
# for t in my_list.tasks:
#     print(t) 
        