from functools import partial
from pyrogram.handlers import MessageHandler
from pyrogram import StopPropagation
from pyrogram import filters
import time, asyncio, re

class userin:
    def __init__(self, client):
        self._client = client
    
    async def get_value(self, client, e,file=False):
        # todo replace with conver. - or maybe not Fix Dont switch to conversion
        # this function gets the new value to be set from the user in current context
        lis = [False,None]

        #func tools works as expected ;);)    
        cbak = MessageHandler(lambda a,b:print("her989889er"),  filters.regex("/helloo", re.IGNORECASE))
        
        client.add_handler(
            cbak,
            2
        )
        await asyncio.sleep(1)

        start = time.time()

        while not lis[0]:
            if (time.time() - start) >= 20:
                break
            print("waiting")

            await asyncio.sleep(3)
        
        val = lis[1]
        
        print("val is", val)
        client.remove_handler(cbak,2)
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
