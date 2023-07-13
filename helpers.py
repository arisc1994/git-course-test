class Greetings:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Welcome {self.name}"