from dataclasses import dataclass


@dataclass
class EnglishTranslations:

    WRONG_VALUE_ERROR = "Invalid value entered for {{ variable_name }} variable."

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

    FLTR_ADD_LEFT_STR = (
        "Addition Filter: <code>{{ text_1 }}</code> <code>To Left</code>"
    )
    FLTR_ADD_RIGHT_STR = (
        "Addition Filter: <code>{{ text_1 }}</code> <code>To Right</code>"
    )
    FLTR_RM_STR = "Remove Filter: <code>{{ text_1 }}</code>"
    FLTR_REPLACE_STR = (
        "Replace Filter: <code>{{ text_1 }}</code> with <code>{{ text_2 }}</code>"
    )

    CURRENT_FLTRS = "Your Current Filters:-"
    ADD_FLTR = "Add Filter."
    RM_FLTR = "Remove Filter."

    FILTERS_INTRO = (
        "Welcome to adding filter.\n"
        "3 Types of filter.\n\n"
        "Replace Filter:- This filter will replace a "
        "given word with the one you specified.\n\n"
        "Addition Filter:- This filter will add a given word "
        "at the end or beginning.\n\n"
        "Remove Filter:- This filter will remove a given word "
        "from the whole file name.\n"
    )

    ADD_REPLACE_FLTR = "Add Replace Filter."
    ADD_ADDITION_FLTR = "Add Addition Filter."
    ADD_REMOVE_FLTR = "Add Remove Filter."
    BACK = "Back."

    REPALCE_FILTER_INIT_MSG = "Send the msg in this format. <code>what to replace | what to replace with</code> or /ignore to go back.\nNote that sapce after and before '|' will be considered."

    NO_INPUT_FROM_USER = "No input received from you."
    INPUT_IGNORE = "Received ignore from you."
    WRONG_INPUT_FORMAT = "The input is not valid. Check the format which is given."
    REPLACE_FILTER_SUCCESS = "Added the Replace filter successfully. <code>'{{ text_1 }}'</code> will be replaced with <code>'{{ text_2 }}'</code>."

    ADDITION_FILTER_INIT_MSG = "Enter the text that you want to add within <code>|</code> \nExample: <code>| text to add |</code>\n  or /ignore to go back."

    ADDITION_FILTER_SUCCESS_LEFT = "Added the Addition filter successfully. <code>{{ text_1 }}</code> will be added to <code>LEFT</code>."

    ADDITION_FILTER_SUCCESS_RIGHT = "Added the Addition filter successfully. <code>{{ text_1 }}</code> will be added to <code>RIGHT</code>."

    ADDITION_LEFT = "Addition to LEFT."
    ADDITION_RIGHT = "Addition to RIGHT."

    ADDITION_POSITION_PROMPT = "Where do you want to add the text."

    REMOVE_FILTER_INIT_MSG = (
        "Enter the text that you want to remove or /ignore to go back."
    )

    REMOVE_FILTER_SUCCESS = "Added the Remove filter successfully. <code>{{ text_1 }}</code> will be removed."

    REPLY_TO_MEDIA = "Reply /rename to a media file."

    HELP_STR = """
`{{ startcmd }}` - Check if the bot is running.
`{{ renamecmd }}` - Reply to media to rename `/rename filename.extension`. If only `/rename` is used filters will be used.
`{{ filterscmd }}` - Add/Remove Filters. Use this command to see what are these.
`{{ setthumbcmd }}` - Reply to image to set the thumbnail permanently.
`{{ getthumbcmd }}` - Get the thumbnail which is currently set.
`{{ clrthumbcmd }}` - Remove the thumbnail which is set.
`{{ modecmd }}` - Change between 3 output modes:-
    - Same format as it was sent. [If doc is sent doc is uploaded if video is sent video is uploaded.]
    - Force to Document. [Everything is uploaded as a file.]
    - Upload general media. [In streamable video/audio. etc.]

    Change between 2 renaming modes:-
    - Rename with command.
    - Rename without command.
`{{ queuecmd }}` - Gives the state of your rename and the load on bot.
    """

    RENAME_DOWNLOADING_DONE = "Downloading done. Now renaming the file."
    RENAME_ERRORED = "Rename process errored."
    RENAME_CANCEL_BY_USER = "Download canceled."

    TRACK_MESSAGE_EXECUTION_START = (
        "Execution Started for Rename Task. `{{ uid }}`\n\n"
        "Username: @{{ username }}\n"
        "Name: {{ name }}\n"
        "User ID: <code>{{ user_id }}</code>\n"
        "File Name: <code>{{ file_name }}</code>\n"
    )

    UPLOADING_THE_FILE = "Uploading the file {{ new_file_name }}."

    RENAME_UPLOAD_CANCELLED_BY_USER = "Upload Cancelled by the user."
    RENAME_UPLOADING_DONE = "Rename Process Done."

    CAPTION_FOOT_NOTE = (
        "NOTE: You can set the caption by sending /setcaption followed by a space and then the caption. "
        "You can include <code>{file_name}</code> in the caption to include the filename of the file being renamed."
    )

    DELETE_CAPTION = "Delete Caption"
    CLOSE = "Close"

    CAPTION_CURRENT = "Your current caption is: {{ caption }}"
    CAPTION_NOT_SET = "No caption set."
