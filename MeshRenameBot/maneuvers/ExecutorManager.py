import asyncio
from ..core.get_config import get_var
from .Executor import Executor

class ExecutorManager:
    maneuvers_queue = asyncio.Queue(maxsize=0)
    active_executors = []

    def __init__(self):
        self._max_simultaneous = get_var("MAX_QUEUE_SIZE")
        self.create_executors()
    
    def create_executors(self):
        if len(self.active_executors) == 0:
            for i in range(1, self._max_simultaneous + 1):
                self.active_executors.append(Executor(self.maneuvers_queue, i))

    def close_executors(self):
        for i in self.active_executors:
            print("clossing")
            i.stop()

    def stop(self):
        self.close_executors()    
    
