from functools import partial
from pyrogram.handlers import MessageHandler
from pyrogram import StopPropagation
from pyrogram import filters
import time, asyncio, re

class userin:

    track_users = {}

    def __init__(self, client):
        self._client = client
    
    async def get_value(self, client, e,file=False):
        # todo replace with conver. - or maybe not Fix Dont switch to conversion
        # this function gets the new value to be set from the user in current context

        
        self.track_users[e.from_user.id] = []
        start = time.time()

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
        
        
        self.track_users.pop(e.from_user.id)
        print("val is", val)
        return val

    async def val_input_callback(self, client, e,o_sender,lis,file):
        # get the input value
        print(" I am herere ")
        if o_sender != e.from_user.id:
            print("No sender")
            return
        if not file:
            lis[0] = True
            lis[1] = e.text
            print(e.text)
            await e.delete()
        else:
            if e.document is not None:
                path = await e.download_media()
                lis[0]  = True
                lis[1] = path 
                await e.delete()
            else:
                if "ignore" in e.text:
                    lis[0]  = True
                    lis[1] = "ignore"
                    await e.delete()
                else:
                    await e.delete()
        print("The end")
        raise StopPropagation()

async def interactive_input(client, msg):
    if msg.from_user.id in userin.track_users.keys():
        userin.track_users[msg.from_user.id].append(msg)
    else:
        msg.continue_propagation()
