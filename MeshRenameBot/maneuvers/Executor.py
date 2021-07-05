import asyncio
import logging
from .Default import DefaultManeuver

renamelog = logging.getLogger(__name__)


class Executor():
    def __init__(self, queue: asyncio.Queue, workerid: int) -> None:
        self.maneuvers_queue = queue
        renamelog.info("Started executor with id {workerid} successfully".format(workerid=workerid))
        self._stop = False
        self.workerid = workerid
        self._current_maneuver = None

        asyncio.get_event_loop().create_task(self.execute())

    async def execute(self) -> None:
        while True:
            if self._stop:
                break
            
            maneuver = await self.maneuvers_queue.get()

            if maneuver.is_canceled:
                ...
            elif maneuver.is_halted:
                await self.maneuvers_queue.put(maneuver)
            else:
                self._current_maneuver = maneuver
                try:
                    await maneuver.execute()
                    maneuver.done()
                except:
                    maneuver.done()
                    renamelog.exception("Execute failed")
                self._current_maneuver = None

            await asyncio.sleep(3)
        
        # renamelog.debug("Started stopped with id {workerid} successfully".format(workerid=self.workerid))
    
    def stop(self) -> None:
        if self._current_maneuver is not None:
            self._current_maneuver.cancel()
        
        self._stop = True
