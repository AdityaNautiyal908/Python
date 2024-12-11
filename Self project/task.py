class Task:
    def __init__(self,description,completed = False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        """ Mark the task as completed """
        self.completed = True

    def __str__(self):
        """Return a string representation of the task."""
        return f"Task: {self.description} | Completed: {'Yes' if self.completed else 'No'}"