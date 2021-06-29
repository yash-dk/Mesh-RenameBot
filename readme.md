# Mesh Rename Bot

This bot has a concept of filters which allows to auto-rename the files. This bot is aimed to be the best rename bot around. 

### This is a beta release. Report the errors/features.
Use of filters is easy just do what the bot says.

# Features
 - Auto Rename files with the help of filters.
 - Permanent Thumbnail support.
 - 3 Different upload modes.
 - Queue implement to maintain consistent speed across rename tasks.

# Upcoming Features
 - These features will be included if users are there for this repo.
 - [ ] Settings Menu for easier managing.
 - [ ] Rename tasks resume after reboot.
 - [ ] More Admin Control and Dump channel.

# Variables

`DB_URI` - Database URL.

`API_HASH` - Telegram API HASH.

`API_ID` - Telegram API ID.

`BOT_TOKEN` - Bot token. Get from bot father.

`COMPLETED_STR` - Completed symbol marker.

`REMAINING_STR` - Remaining symbol marker.

`MAX_QUEUE_SIZE` - Max simultaneous renames. 5 is recommended can be increased.

`SLEEP_SECS` - Seconds to sleep before edit. 10 is recommended can be increased.

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

# Credits
[Me](https://github.com/yash-dk)

[Dan for Pyrogram](https://github.com/pyrogram/pyrogram)

