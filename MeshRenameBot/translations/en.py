class EnTrans:
    
    WRONG_VALUE_ERROR = "Invalid value entered for {} variable."
    
    START_MSG = "Hello there, I am Mesh Rename Bot. Open Source at https://github.com/yash-dk/Mesh-RenameBot/tree/master. You can deploy your own."
     
    CANCEL_MESSAGE = "The rename has been canceled. Will be updated soon."
    
    RENAME_NO_FILTER_MATCH = "NO FILTER MATCHED ABORTING RENAME \nUsing the filters to Rename. As no name was specified. Manage your Filters using /filters."

    RENAME_FILTER_MATCH_USED = "Using the filters to Rename. As no name was specified. Manage your Filters using /filters"

    RENAME_NOFLTR_NONAME = "Enter the rename file name in format :- ```/rename my new filename.extension``` or ```Use /filters to set some rename filters.```"

    RENAME_CANCEL = "Cancel this rename."

    RENAMING_FILE = "Renaming the file currently hold on."
    
    DL_RENAMING_FILE = "Downloading the file currently hold on."

    RENAME_ERRORED_REPORT = "The download was errored. Report this error."

    RENAME_CANCEL_BY_USER = "Canceled by the user."

    FLTR_ADD_LEFT_STR = "Addition Filter: <code>{}</code> <code>To Left</code>"
    FLTR_ADD_RIGHT_STR = "Addition Filter: <code>{}</code> <code>To Right</code>"
    FLTR_RM_STR = "Remove Filter: <code>{}</code>"
    FLTR_REPLACE_STR = "Replace Filter: <code>{}</code> with <code>{}</code>"

    CURRENT_FLTRS = "Your Current Filters:-"
    ADD_FLTR = "Add Filter."
    RM_FLTR = "Remove Filter."

    FILTERS_INTRO = """
Welcome to adding filter.
3 Types of filter.

Replace Filter:- This filter will replace a
given word with the one you sepcified

Addition Filter:- This filter will add given word
at end or beginning.

Remove Filter:- This filer will remove given word
from the while file name.

"""

    ADD_REPLACE_FLTR = "Add Replace Filter."
    ADD_ADDITION_FLTR = "Add Addition Filter."
    ADD_REMOVE_FLTR = "Add Remove Filter."
    BACK = "Back."

    REPALCE_FILTER_INIT_MSG = "Send the msg in this format. <code>what to replace | what to replace with</code> or /ignore to go back.\nNote that sapce after and before '|' will be considered."

    NO_INPUT_FROM_USER = "No input received from you."
    INPUT_IGNORE = "Received ignore from you."
    WRONG_INPUT_FORMAT = "The input is not valid. Check the format which is given."
    REPLACE_FILTER_SUCCESS = "Added the Replace filter successfully. <code>'{}'</code> will be replaced with <code>'{}'</code>."

    ADDITION_FILTER_INIT_MSG = "Enter the text that you want to add or /ignore to go back."

    ADDITION_FILTER_SUCCESS_LEFT = "Added the Addition filter successfully. <code>{}</code> will be added to <code>LEFT</code>."

    ADDITION_FILTER_SUCCESS_RIGHT = "Added the Addition filter successfully. <code>{}</code> will be added to <code>RIGHT</code>."

    ADDITION_LEFT = "Addition to LEFT."
    ADDITION_RIGHT = "Addition to RIGHT."

    ADDITION_POSITION_PROMPT = "Where do you want to add the text."

    REMOVE_FILTER_INIT_MSG = "Enter the text that you want to remove or /ignore to go back."

    REMOVE_FILTER_SUCCESS = "Added the Remove filter successfully. <code>{}</code> will be removed."

    REPLY_TO_MEDIA = "Reply /rename to a media file."

    HELP_STR = """
`/start` - Check if the bot is running.
`/rename` - Reply to media to rename `/rename filename.extension`. If only `/rename` is used filters will be used.
`/filters` - Add/Remove Filters. Use this command to see what are these.
`/setthumb` - Reply to image to set the thumbnail permanently.
`/getthumb` - Get the thumbnail which is currently set.
`/clrthumb` - Remove the thumbnail which is set.
`/mode` - Change between 3 modes:-
    - Same format as it was sent. [If doc is sent doc is uploaded if video is sent video is uploaded.]
    - Force to Document. [Everything is uploaded as a file.]
    - Upload general media. [In streamable video/audio. etc.]
`/queue` - Gives the state of your rename and the load on bot.
    """