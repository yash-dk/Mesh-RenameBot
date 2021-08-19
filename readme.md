# Mesh Rename Bot

This bot has a concept of filters which allows to auto-rename the files. This bot is aimed to be the best rename bot around. 

## This is a beta release. Report the errors/features.
Use of filters is easy just do what the bot says.

## Bot is still is Beta try and let me know any bugs will be appreciated.

### If any issue/doubt file issue.

# Features
 - Auto Rename files with the help of filters.
 - Permanent Thumbnail support.
 - 3 Different upload modes.
 - Queue implement to maintain consistent speed across rename tasks.
 - Supports both Mongo and Postgres DB.
 - Track user activity.
 - Force join for the user for use.

# Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yash-dk/Mesh-RenameBot)


# Upcoming Features
 - These features will be included if users are there for this repo.
 - [ ] Rename tasks resume after reboot.
 - [ ] More Admin Control and Dump channel.

# Filters Explained
Filter can be added using the /filter.
- ## Addition Filter
  - This filter will add the given text to the left or right of the file name.
- ## Remove Filter
  - This filter will remove the given text if it is present at all in the file name.
- ## Replace
  - This filter will replace the specific text with the new text.

# Variables

update the config.py file inside the MeshRenameBot to change the config and commands.

`DB_URI` - Database URL. Mongo or Postgres DB URL.

`API_HASH` - Telegram API HASH.

`API_ID` - Telegram API ID.

`BOT_TOKEN` - Bot token. Get from bot father.

`COMPLETED_STR` - Completed symbol marker.

`REMAINING_STR` - Remaining symbol marker.

`MAX_QUEUE_SIZE` - Max simultaneous renames. 5 is recommended can be increased.

`SLEEP_SECS` - Seconds to sleep before edit. 10 is recommended can be increased.

`IS_PRIVATE` - Is the bot for private use.

`AUTH_USERS` - ID of the users that are allowed to use the bot. It works only when `IS_PRIVATE` is True.

`OWNER_ID` - ID of the owner.

`FORCEJOIN` - Enter the public username url or invite link of private chat for that the user should join chat. Keep blank to disable.

`FORCEJOIN_ID` - ID of the chat for which is specified in `FORCEJOIN`.

`TRACE_CHANNEL` - ID of the channel to which the track of the uses is sent who are using the bot. Put 0 for no tracking.

# Commands
`/start` - Check if the bot is running.

`/rename` - Reply to media to rename `/rename filename.extension`. If only `/rename` is used filters will be used.

`/filters` - Add/Remove Filters.

`/setthumb` - Reply to image to set the thumbnail permanently.

`/getthumb` - Get the thumbnail which is currently set.

`/clrthumb` - Remove the thumbnail which is set.

`/mode` - Change between 3 modes:-
- Same format as it was sent. [If doc is sent doc is uploaded if video is sent video is uploaded.]
- Force to Document. [Everything is uploaded as a file.]
- Upload general media. [In streamable video/audio. etc.]

`/queue` - Gives the state of your rename and the load on bot.

# For VPS Deploy
- Install ffmpeg and python.
- Run the bot using `python3 -m MeshRenameBot` or `python -m MeshRenameBot`

# Credits
[Me](https://github.com/yash-dk)

[Dan for Pyrogram](https://github.com/pyrogram/pyrogram)

