import datetime

from superbettingcommons.dtos.basedto import BaseDto


class ScrapedMatchDto(BaseDto):
    def __init__(self):
        self.match_data = MatchData()
        self.snapshot: Snapshot = Snapshot()


class MatchData(BaseDto):
    def __init__(self) -> None:
        self.match_name = ""
        self.match_id = ""
        self.home_team = ""
        self.away_team = ""
        self.started: datetime.datetime = datetime.datetime.now()


class Snapshot(BaseDto):
    def __init__(self) -> None:
        self.seconds = 0
        self.minutes = 0
        self.score_home = 0
        self.score_away = 0
        self.score_sum = 0
        self.statistics = Statistics()
        self.bet_list: list[BetData] = []


class BetData(BaseDto):
    def __init__(self) -> None:
        self.bet_type = BetType()


class BetType(BaseDto):
    def __init__(self):
        self.over_type = -1
        self.quota: int = 0


class Statistics(BaseDto):
    def __init__(self):
        self.attacks_home = 0
        self.attacks_away = 0
        self.attacks_sum = 0
        self.dangerous_attacks_home = 0
        self.dangerous_attacks_away = 0
        self.dangerous_attacks_sum = 0
        self.shots_on_target_home = 0
        self.shots_on_target_away = 0
        self.shots_on_target_sum = 0
        self.shots_off_target_home = 0
        self.shots_off_target_away = 0
        self.shots_off_target_sum = 0
        self.yellow_cards_home = 0
        self.yellow_cards_away = 0
        self.yellow_cards_sum = 0
        self.red_cards_home = 0
        self.red_cards_away = 0
        self.red_cards_sum = 0
        self.corners_home = 0
        self.corners_away = 0
        self.corners_sum = 0
