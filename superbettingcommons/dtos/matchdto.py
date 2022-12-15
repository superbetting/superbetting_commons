import json
from datetime import datetime
from types import SimpleNamespace

from superbettingcommons.dtos.basedto import BaseDto
from superbettingcommons.utilities.json_utils import dump_function


class _MatchData:
    def __init__(self):
        self.event_id = ""
        self.match_name = ""
        self.match_team_1 = ""
        self.match_team_2 = ""
        self.point_1 = -1
        self.point_2 = -1
        self.minutes = -1
        self.goal_interceptor = 0
        self.attacchi = 0


class _BetType:
    def __init__(self):
        self.over_type = -1
        self.quota: int = 0


class _BetStatus:
    def __init__(self):
        self.closed = False
        self.win = False
        self.closed_date: datetime = datetime.now()
        self.scanned_date: datetime = datetime.now()


class BetMultiplier:
    def __init__(self):
        self.multiplier = -1
        self.booster = 1
        self.freezer = 1


class _BetData:
    def __init__(self):
        self.bet_type = _BetType()
        self.bet_status = _BetStatus()
        self.bet_multiplier = BetMultiplier()


class MatchDto(BaseDto):

    def __init__(self):
        self.match_data = _MatchData()
        self.bet_data = _BetData()
