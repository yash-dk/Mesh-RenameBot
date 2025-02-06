from dataclasses import dataclass


@dataclass
class ChineseTranslations:
    LANGUAGE_NAME = "中文"
    LANGUAGE_CODE = "zh"

    WRONG_VALUE_ERROR = "❌ 为 {{ variable_name }} 变量输入了无效的值。"

    START_MSG = (
        "👋 你好！我是 **Mesh 重命名机器人**。\n\n"
        "🌟 开源项目: [GitHub](https://github.com/yash-dk/Mesh-RenameBot/tree/master)\n"
        "🚀 你可以部署你自己的实例！"
    )

    CANCEL_MESSAGE = "⚠️ 重命名已被 **取消**。将会尽快更新。"

    RENAME_NO_FILTER_MATCH = (
        "🚫 **没有匹配的过滤器 - 取消重命名**\n\n"
        "🔍 由于未指定名称，使用过滤器进行重命名。\n"
        "📌 使用 /filters 管理你的过滤器。"
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ 由于未指定名称，使用过滤器进行重命名。\n"
        "📌 使用 /filters 管理你的过滤器。"
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ 以以下格式输入新文件名：\n"
        "```/rename my_new_filename.extension```\n"
        "或使用 `/filters` 设置重命名过滤器。"
    )

    RENAME_CANCEL = "❌ 取消此重命名。"

    RENAMING_FILE = "🔄 正在重命名文件... 请稍候。"

    DL_RENAMING_FILE = "📥 正在下载文件... 请稍候。"

    RENAME_ERRORED_REPORT = "❗ 下载过程中遇到错误。请报告此问题。"

    RENAME_CANCEL_BY_USER = "🚫 **由用户取消。**"

    FLTR_ADD_LEFT_STR = "➕ 已添加过滤器：`<code>{{ text_1 }}</code>` **在左侧**。"
    FLTR_ADD_RIGHT_STR = "➕ 添加过滤器：`<code>{{ text_1 }}</code>` **在右侧**。"
    FLTR_RM_STR = "❌ 移除过滤器：`<code>{{ text_1 }}</code>`。"
    FLTR_REPLACE_STR = (
        "🔄 替换过滤器：`<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`。"
    )

    CURRENT_FLTRS = "⚙️ **你当前的过滤器：**"
    ADD_FLTR = "➕ 添加过滤器"
    RM_FLTR = "❌ 移除过滤器"

    FILTERS_INTRO = (
        "🛠 **过滤器指南：**\n"
        "共有 3 种类型的过滤器：\n\n"
        "🔄 **替换过滤器：**用另一个词替换指定的词。\n"
        "➕ **添加过滤器：**在开头或结尾添加一个词。\n"
        "❌ **移除过滤器：**从文件名中移除一个词。"
    )

    ADD_REPLACE_FLTR = "➕ 添加替换过滤器"
    ADD_ADDITION_FLTR = "➕ 添加添加过滤器"
    ADD_REMOVE_FLTR = "➕ 添加移除过滤器"
    BACK = "🔙 返回"

    REPALCE_FILTER_INIT_MSG = (
        "✍️ 发送格式：`<code>要替换的内容 | 替换内容</code>` 或 `/ignore` 返回。"
    )

    NO_INPUT_FROM_USER = "⚠️ 未收到你的输入。"
    INPUT_IGNORE = "✅ **已忽略。**"
    WRONG_INPUT_FORMAT = "❌ 格式无效。请检查提供的格式。"
    REPLACE_FILTER_SUCCESS = (
        "✅ **已添加替换过滤器：**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ 输入要添加的文本，使用 `<code>|</code>` 分隔\n"
        "示例：`<code>| 要添加的文本 |</code>`\n"
        "或 `/ignore` 返回。"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ 已添加过滤器：`<code>{{ text_1 }}</code>` **在左侧**。"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ 已添加过滤器：`<code>{{ text_1 }}</code>` **在右侧**。"
    )

    ADDITION_LEFT = "🔄 添加到左侧"
    ADDITION_RIGHT = "🔄 添加到右侧"

    ADDITION_POSITION_PROMPT = "📍 **你想在哪里添加文本？**"

    REMOVE_FILTER_INIT_MSG = "✍️ 输入你想移除的文本或 `/ignore` 返回。"

    REMOVE_FILTER_SUCCESS = (
        "✅ **已添加移除过滤器：** `<code>{{ text_1 }}</code>` 将被移除。"
    )

    REPLY_TO_MEDIA = "📂 回复 `/rename` 到一个媒体文件。"

    RENAME_DOWNLOADING_DONE = "✅ 下载完成。现在正在重命名文件..."
    RENAME_ERRORED = "❗ 重命名过程遇到错误。"
    RENAME_CANCEL_BY_USER = "🚫 **下载已取消。**"

    UPLOADING_THE_FILE = "📤 正在上传文件：**{{ new_file_name }}**"

    RENAME_UPLOAD_CANCELLED_BY_USER = "🚫 **上传已被用户取消。**"
    RENAME_UPLOADING_DONE = "✅ **重命名过程完成。**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **重命名任务执行开始**\n"
        "🆔 任务 ID: `{{ uid }}`\n\n"
        "👤 **用户名:** @{{ username }}\n"
        "📛 **姓名:** {{ name }}\n"
        "🆔 **用户 ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **文件名:** `<code>{{ file_name }}</code>`"
    )

    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **已添加重命名任务**\n\n"
        "👤 **用户名:** @{{ username }}\n"
        "📛 **姓名:** {{ name }}\n"
        "🆔 **用户 ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "📌 **注意：** 你可以使用 `/setcaption` 加上你想要的文本来设置标题。\n"
        "📂 使用 `<code>{file_name}</code>` 动态插入重命名后的文件名到标题中。"
    )

    DELETE_CAPTION = "🗑 删除标题"
    CLOSE = "❌ 关闭"

    CAPTION_CURRENT = "📝 **你当前的标题：** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **未设置标题。**"
    CAPTION_SET = "✅ **标题已更新为：** {{ caption }}"
    CAPTION_DELETED = "🗑 **标题已成功删除。**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **重命名任务已加入队列**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "📌 **媒体 ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **重命名队列状态：**\n"
        "📌 **队列中的总任务数：** {{ total_tasks }}\n"
        "📌 **队列容量：** {{ queue_capacity }}\n"
        "⏳ **当前处理中：** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **你的任务正在执行中**\n"
        "🆔 **任务 ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **你在队列中的任务位置：** {{ task_number }}\n"
        "🆔 **任务 ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "🚷 **你已被移出聊天。你无法使用此机器人。**"
    USER_NOT_PARTICIPANT = "⚠️ **加入所需的聊天以使用此机器人。**"
    JOIN_CHANNEL = "🔗 加入更新频道"

    MODE_INITIAL_MSG = (
        "📂 **文件输出模式：**\n\n"
        "1️⃣ **与发送的格式相同。**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **强制为文档。**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **作为通用媒体上传。**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "📌 **选择重命名模式：**\n"
        "🅰️ **使用命令重命名。**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **不使用命令重命名。**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 回复一张图片以设置为缩略图。"
    THUMB_SET_SUCCESS = "✅ **缩略图设置成功。**"
    THUMB_NOT_FOUND = "⚠️ **未找到缩略图。**"
    THUMB_CLEARED = "🗑 **缩略图已成功清除。**"

    HELP_STR = (
        "📖 **机器人命令：**\n"
        "`{{ startcmd }}` - ✅ 检查机器人是否正在运行。\n"
        "`{{ renamecmd }}` - ✍️ 回复一个媒体文件，使用 `/rename filename.extension` 来重命名它。\n"
        "`{{ filterscmd }}` - ⚙️ 管理你的重命名过滤器。\n"
        "`{{ setthumbcmd }}` - 📷 设置一个永久缩略图（回复一张图片）。\n"
        "`{{ getthumbcmd }}` - 📸 获取当前设置的缩略图。\n"
        "`{{ clrthumbcmd }}` - ❌ 移除设置的缩略图。\n"
        "`{{ modecmd }}` - 🔄 在 3 种输出模式之间切换：\n"
        "    - 📝 与发送的格式相同。\n"
        "    - 📂 强制为文档。\n"
        "    - 🎥 通用媒体（可流式传输的视频/音频）。\n\n"
        "    🔄 在重命名模式之间切换：\n"
        "    - 🏷 使用 **命令** 重命名。\n"
        "    - ✨ 不使用 **命令** 重命名。\n\n"
        "`{{ queuecmd }}` - 📊 查看机器人的重命名队列状态。\n"
        "`{{ setcaptioncmd }}` - 📝 为重命名的文件设置标题。\n"
        "`{{ helpcmd }}` - 📖 显示此帮助信息。\n"
        "`{{ setlaguagecmd }}` - 🌐 设置机器人的语言。\n"
    )

    CURRENT_LOCALE = "🌐 **您当前的语言:** {{ user_locale }}"
