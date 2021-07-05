import asyncio
from ..core.get_config import get_var
from .Executor import Executor
from .Default import DefaultManeuver


class ExecutorManager:
    maneuvers_queue = asyncio.Queue(maxsize=0)
    all_maneuvers_log = []
    active_executors = []
    canceled_uids = []

    def __init__(self) -> None:
        self._max_simultaneous = get_var("MAX_QUEUE_SIZE")
        self.create_executors()
    
    def create_executors(self) -> None:
        if len(self.active_executors) == 0:
            for i in range(1, self._max_simultaneous + 1):
                self.active_executors.append(Executor(self.maneuvers_queue, i))

    def close_executors(self) -> None:
        for i in self.active_executors:
            i.stop()

    async def create_maneuver(self, maneuver: DefaultManeuver) -> None:
        await self.maneuvers_queue.put(maneuver)
        self.all_maneuvers_log.append(maneuver)

    def stop(self) -> None:
        self.close_executors()
