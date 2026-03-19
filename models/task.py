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
        from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, project_id, assignee_id, id=None, status='pending'):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.project_id = project_id
        self.assignee_id = assignee_id
    
    def update_status(self, new_status):
        valid_statuses = ['pending', 'in_progress', 'completed']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
    
    def is_overdue(self):
        if self.status == 'completed':
            return False
        return datetime.now() > self.due_date
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'project_id': self.project_id,
            'assignee_id': self.assignee_id
        }
