from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, project_id, assignee_id) -> None:
        pass

    def update_status(self, new_status) -> bool:
        pass

    def is_overdue(self) -> bool:
        pass

    def to_dict(self) -> dict:
        pass
        import datetime

class Task:
    def __init__(self, title, description, priority, due_date, project_id, assignee_id):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority  # 1-высокий, 2-средний, 3-низкий
        self.status = 'pending'  # 'pending', 'in_progress', 'completed'
        self.due_date = due_date
        self.project_id = project_id
        self.assignee_id = assignee_id
        self.created_at = datetime.datetime.now()
    
    def update_status(self, new_status):
        valid_statuses = ['pending', 'in_progress', 'completed']
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False
    
    def is_overdue(self):
        return datetime.datetime.now() > self.due_date and self.status != 'completed'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'due_date': self.due_date.strftime('%Y-%m-%d %H:%M:%S'),
            'project_id': self.project_id,
            'assignee_id': self.assignee_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'is_overdue': self.is_overdue()
        }
        
