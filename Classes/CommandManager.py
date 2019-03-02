class CommandManager:
    def __init__(self):
        self.stack = []
    
    def run(self,command):
        command.execute()
        self.stack.append(command)
        return True