from dataclasses import dataclass

@dataclass
class KoreanTranslations:
    LANGUAGE_NAME = "한국어"
    LANGUAGE_CODE = "ko"

    WRONG_VALUE_ERROR = "❌ {{ variable_name }} 변수에 잘못된 값이 입력되었습니다."

    START_MSG = (
        "👋 안녕하세요! 저는 **Mesh Rename Bot**입니다.\n\n"
        "🌟 오픈 소스: [GitHub](https://github.com/yash-dk/Mesh-RenameBot/tree/master)\n"
        "🚀 직접 인스턴스를 배포할 수 있습니다!"
    )

    CANCEL_MESSAGE = "⚠️ 이름 변경이 **취소**되었습니다. 곧 업데이트될 예정입니다."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **필터가 일치하지 않음 - 이름 변경 중단**\n\n"
        "🔍 이름이 지정되지 않아 필터를 사용하여 이름을 변경합니다.\n"
        "📌 /filters를 사용하여 필터를 관리하세요."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ 이름이 지정되지 않아 필터를 사용하여 이름을 변경합니다.\n"
        "📌 /filters를 사용하여 필터를 관리하세요."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ 새 파일 이름을 다음 형식으로 입력하세요:\n"
        "```/rename my_new_filename.extension```\n"
        "또는 `/filters`를 사용하여 이름 변경 필터를 설정하세요."
    )

    RENAME_CANCEL = "❌ 이 이름 변경을 취소합니다."

    RENAMING_FILE = "🔄 파일 이름을 변경 중입니다... 잠시만 기다려 주세요."

    DL_RENAMING_FILE = "📥 파일을 다운로드 중입니다... 잠시만 기다려 주세요."

    RENAME_ERRORED_REPORT = "❗ 다운로드 중 오류가 발생했습니다. 이 문제를 보고하세요."

    RENAME_CANCEL_BY_USER = "🚫 **사용자에 의해 취소되었습니다.**"

    FLTR_ADD_LEFT_STR = "➕ 필터 추가됨: `<code>{{ text_1 }}</code>` **왼쪽에**."
    FLTR_ADD_RIGHT_STR = (
        "➕ 필터 추가됨: `<code>{{ text_1 }}</code>` **오른쪽에**."
    )
    FLTR_RM_STR = "❌ 필터 제거됨: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 필터 교체됨: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "⚙️ **현재 필터:**"
    ADD_FLTR = "➕ 필터 추가"
    RM_FLTR = "❌ 필터 제거"

    FILTERS_INTRO = (
        "🛠 **필터 가이드:**\n"
        "필터에는 3가지 유형이 있습니다:\n\n"
        "🔄 **교체 필터:** 지정된 단어를 다른 단어로 교체합니다.\n"
        "➕ **추가 필터:** 시작 또는 끝에 단어를 추가합니다.\n"
        "❌ **제거 필터:** 파일 이름에서 단어를 제거합니다."
    )

    ADD_REPLACE_FLTR = "➕ 교체 필터 추가"
    ADD_ADDITION_FLTR = "➕ 추가 필터 추가"
    ADD_REMOVE_FLTR = "➕ 제거 필터 추가"
    BACK = "🔙 뒤로"

    REPALCE_FILTER_INIT_MSG = "✍️ 형식 전송: `<code>교체할_내용 | 대체할_내용</code>` 또는 돌아가려면 `/ignore`를 입력하세요."

    NO_INPUT_FROM_USER = "⚠️ 사용자로부터 입력을 받지 못했습니다."
    INPUT_IGNORE = "✅ **무시됨.**"
    WRONG_INPUT_FORMAT = "❌ 형식이 잘못되었습니다. 제공된 형식을 확인하세요."
    REPLACE_FILTER_SUCCESS = (
        "✅ **교체 필터가 추가되었습니다:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ 추가할 텍스트를 `<code>|</code>`로 구분하여 입력하세요.\n"
        "예시: `<code>| 추가할 텍스트 |</code>`\n"
        "또는 돌아가려면 `/ignore`를 입력하세요."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ 필터가 추가되었습니다: `<code>{{ text_1 }}</code>` **왼쪽에**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ 필터가 추가되었습니다: `<code>{{ text_1 }}</code>` **오른쪽에**."
    )

    ADDITION_LEFT = "🔄 왼쪽에 추가"
    ADDITION_RIGHT = "🔄 오른쪽에 추가"

    ADDITION_POSITION_PROMPT = "📍 **텍스트를 어디에 추가하시겠습니까?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ 제거할 텍스트를 입력하거나 돌아가려면 `/ignore`를 입력하세요."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **제거 필터가 추가되었습니다:** `<code>{{ text_1 }}</code>`이(가) 제거됩니다."
    )

    REPLY_TO_MEDIA = "📂 미디어 파일에 `/rename`으로 회신하세요."

    RENAME_DOWNLOADING_DONE = "✅ 다운로드 완료. 이제 파일 이름을 변경합니다..."
    RENAME_ERRORED = "❗ 이름 변경 과정에서 오류가 발생했습니다."
    RENAME_CANCEL_BY_USER = "🚫 **다운로드가 취소되었습니다.**"

    UPLOADING_THE_FILE = "📤 파일 업로드 중: **{{ new_file_name }}**"

    RENAME_UPLOAD_CANCELLED_BY_USER = "🚫 **사용자에 의해 업로드가 취소되었습니다.**"
    RENAME_UPLOADING_DONE = "✅ **이름 변경 과정이 완료되었습니다.**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **이름 변경 작업 실행 시작**\n"
        "🆔 작업 ID: `{{ uid }}`\n\n"
        "👤 **사용자 이름:** @{{ username }}\n"
        "📛 **이름:** {{ name }}\n"
        "🆔 **사용자 ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **파일 이름:** `<code>{{ file_name }}</code>`"
    )

    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **이름 변경 작업이 추가되었습니다**\n\n"
        "👤 **사용자 이름:** @{{ username }}\n"
        "📛 **이름:** {{ name }}\n"
        "🆔 **사용자 ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "📌 **참고:** `/setcaption`과 원하는 텍스트를 사용하여 캡션을 설정할 수 있습니다.\n"
        "📂 캡션에 이름이 변경된 파일 이름을 동적으로 삽입하려면 `<code>{file_name}</code>`을 사용하세요."
    )

    DELETE_CAPTION = "🗑 캡션 삭제"
    CLOSE = "❌ 닫기"

    CAPTION_CURRENT = "📝 **현재 캡션:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **캡션이 설정되지 않았습니다.**"
    CAPTION_SET = "✅ **캡션이 다음으로 업데이트되었습니다:** {{ caption }}"
    CAPTION_DELETED = "🗑 **캡션이 성공적으로 삭제되었습니다.**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **이름 변경 작업이 큐에 추가되었습니다**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "📌 **미디어 ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **이름 변경 큐 상태:**\n"
        "📌 **큐의 총 작업 수:** {{ total_tasks }}\n"
        "📌 **큐 용량:** {{ queue_capacity }}\n"
        "⏳ **현재 처리 중:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **귀하의 작업이 현재 실행 중입니다**\n"
        "🆔 **작업 ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **큐에서의 작업 위치:** {{ task_number }}\n"
        "🆔 **작업 ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "🚷 **채팅에서 제거되었습니다. 이 봇을 사용할 수 없습니다.**"
    USER_NOT_PARTICIPANT = "⚠️ **이 봇을 사용하려면 필요한 채팅에 참여하세요.**"
    JOIN_CHANNEL = "🔗 **업데이트 채널에 가입하세요**"

    MODE_INITIAL_MSG = (
        "📂 **파일 출력 모드:**\n\n"
        "1️⃣ **보낸 것과 동일한 형식.**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **문서로 강제.**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **일반 미디어로 업로드.**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "📌 **이름 변경 모드를 선택하세요:**\n"
        "🅰️ **명령어로 이름 변경.**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **명령어 없이 이름 변경.**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 썸네일로 설정하려면 이미지에 회신하세요."
    THUMB_SET_SUCCESS = "✅ **썸네일이 성공적으로 설정되었습니다.**"
    THUMB_NOT_FOUND = "⚠️ **썸네일을 찾을 수 없습니다.**"
    THUMB_CLEARED = "🗑 **썸네일이 성공적으로 삭제되었습니다.**"

    HELP_STR = (
        "📖 **봇 명령어:**\n"
        "`{{ startcmd }}` - ✅ 봇이 작동 중인지 확인합니다.\n"
        "`{{ renamecmd }}` - ✍️ 미디어 파일에 `/rename filename.extension`으로 회신하여 이름을 변경합니다.\n"
        "`{{ filterscmd }}` - ⚙️ 이름 변경 필터를 관리합니다.\n"
        "`{{ setthumbcmd }}` - 📷 영구 썸네일을 설정합니다 (이미지에 회신).\n"
        "`{{ getthumbcmd }}` - 📸 현재 설정된 썸네일을 가져옵니다.\n"
        "`{{ clrthumbcmd }}` - ❌ 설정된 썸네일을 제거합니다.\n"
        "`{{ modecmd }}` - 🔄 3가지 출력 모드 간 전환:\n"
        "    - 📝 보낸 것과 동일한 형식.\n"
        "    - 📂 문서로 강제.\n"
        "    - 🎥 일반 미디어 (스트리밍 가능한 비디오/오디오).\n\n"
        "    🔄 이름 변경 모드 간 전환:\n"
        "    - 🏷 명령어로 **이름 변경**.\n"
        "    - ✨ 명령어 없이 **이름 변경**.\n\n"
        "`{{ queuecmd }}` - 📊 봇의 이름 변경 큐 상태를 확인합니다.\n"
        "`{{ setcaptioncmd }}` - 📝 이름이 변경된 파일의 캡션을 설정합니다.\n"
        "`{{ helpcmd }}` - 📖 이 도움말 메시지를 표시합니다.\n"
        "`{{ setlaguagecmd }}` - 🌐 봇의 언어를 설정합니다.\n"
    )

    CURRENT_LOCALE = "🌐 **현재 사용 중인 언어:** {{ user_locale }}"

