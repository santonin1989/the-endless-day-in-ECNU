label get_up:
    "主角在这里起床。"
    "发现手机日期显示还是“昨天”"
    menu:
        "今天到底去哪上课？"
        "神金，手机也睡懵了是吧":
            "你走向“第二天”的B教室"
            jump class_second_day_B
        "真的假的，今天还上这课？":
            "有些犹疑地走向A教室"
            jump class_second_day_A

label class_second_day_late:
    "我是二周目迟到的上午上课"
    "主角在这里意识到事件循环"

label class_second_day_A:
    "我是二周目准时上课的上午"
    "主角前往了A教室，上了和“昨天”一样的课"

label class_second_day_B:
    "我是二周目准时上课的上午"
    "主角前往了B教室，发现不对劲"