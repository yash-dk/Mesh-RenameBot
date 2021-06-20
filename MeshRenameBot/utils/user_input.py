import time
import asyncio
from typing import Union
from pyrogram import Client, types


class userin:

    track_users = {}

    def __init__(self, client):
        self._client = client
    
    async def get_value(self, client: Client, e: types.MessageEntity, file: bool = False, del_msg: bool = False) -> Union[None, str]:
        # todo replace with conver. - or maybe not Fix Dont switch to conversion
        # this function gets the new value to be set from the user in current context

        self.track_users[e.from_user.id] = []
        start = time.time()
        val = None

        while True:
            if (time.time() - start) >= 20:
                break
            
            if len(self.track_users[e.from_user.id]) != 0:
                msg_obj = self.track_users[e.from_user.id].pop(0)
                
                if msg_obj.text == "/ignore":
                    val = "ignore"
                    break

                if file:
                    if msg_obj.document is not None:
                        val = await msg_obj.download()
                        break
                else:
                    val = msg_obj.text
                    break
            
            await asyncio.sleep(1)
        
        if val is not None and del_msg:
            await msg_obj.delete()

        self.track_users.pop(e.from_user.id)
        print("val is", val)
        return val


async def interactive_input(client: Client, msg: types.MessageEntity) -> None:
    if msg.from_user.id in userin.track_users.keys():
        userin.track_users[msg.from_user.id].append(msg)
    else:
        msg.continue_propagation()
