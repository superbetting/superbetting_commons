import enum

Index_Emoji_Converter_Dictionary = {
    -1: '',
    1: '❌',
    2: '✋',
    3: '👉',
    4: '🔊',
    5: '🎾',
    6: '🏥',
    7: '⌚',
    8: '👀',
    9: '📊',
    10: '🎥',
    11: '🔗',
    12: '✅',
    13: '❓',
    14: '🤑',
    15: '😈',
    16: '👹',
    17: '👺',
    18: '🔴',
    19: '🔥',
    20: '🦾',
    21: '📌',
    22: '🔵',
    23: '😎',
    24: '🙏'

}


class Emoji(enum.Enum):
    RED_CROSS = 1,
    HAND = 2,
    HAND_RIGHT = 3,
    SPEAKER = 4,
    TENNIS_BALL = 5,
    HOSPITAL = 6,
    CLOCK = 7,
    OPENED_EYES = 8,
    STATISTICS_GRAPH = 9,
    VIDEO_CAM = 10,
    LINK = 11,
    GREEN_CHECK = 12,
    QUESTION = 13,
    MONEY_EYES = 14,
    EVIL = 15,
    RED_MASK_1 = 16,
    RED_MASK_2 = 17,
    RED_CIRCLE = 18,
    FIRE = 19,
    ARM = 20,
    PUSH_PIN = 21,
    BLUE_CIRCLE = 22,
    GLASSES_FACE = 23,
    DOUBLE_HANDS = 24,
    NONE = -1

    def __str__(self):
        global Index_Emoji_Converter_Dictionary
        return str(Index_Emoji_Converter_Dictionary[self.value[0]])
