from superbettingcommons.dtos.basedto import BaseDto


class _MatchParam:
    def __init__(self):
        self.min_gt = ""
        self.max_gt = ""
        self.min_minute = ""
        self.max_minute = -1
        self.min_quota = -1
        self.max_quota = -1
        self.min_attacchi = 0
        self.max_attacchi = 0


class _BetParam:
    def __init__(self):
        self.stake = 0
        self.start_verde = 0
        self.start_rosso = 0
        self.pendenza = 1.1
        self.soglia_booster = 1
        self.soglia_freezer = 1
        self.booster_multiplier = 1
        self.freezer_multiplier = 1
        self.verde_rosso_diff = 0


class _PublishParam:
    def __init__(self):
        self.collection_name = ""
        self.routing_key = ""
        self.chat_id = ""


class ConfigurationDto(BaseDto):

    def __init__(self):
        self.name = ""
        self.type = ""
        self.publish_param = _PublishParam()
        self.match_param = _MatchParam()
        self.bet_param = _BetParam()
