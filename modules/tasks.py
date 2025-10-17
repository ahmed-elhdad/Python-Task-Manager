tasks=[]

class Task:
    def __init__(self,id,title,description,created_at,endded_at,status):
        self.title=title
        self.description=description
        self.created_at=created_at
        self.endded_at=endded_at
        self.status=status
    def show_tasks():
        for i in range(len(tasks)):
            print(f"""
                TASK {i}: 
                    Title: {tasks[i].name}
                    Desctiption: {tasks[i].description}
                    Created_at: {tasks[i].created_at}
                    Created_at: {tasks[i].created_at}
                    Status: {tasks[i].status}
                """)