# Classes & OOP — Staged Breakdown

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

    
  


task1=Task(1,"Buy milk", "Get 2% milk")
task2 = Task(2, "Walk dog", "Evening walk")
print(task2.id,task2.name,task2.description,task2.status)
task2.mark_done(True)
print(task1.id ,task1.name,task1.description,task1.status)
print(task2.id,task2.name,task2.description,task2.status)
print(task2)
