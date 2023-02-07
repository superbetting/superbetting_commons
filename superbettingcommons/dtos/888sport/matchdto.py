import dtos.basedto


class ScrapedMatchDto(dtos.basedto.BaseDto):
    def __init__(self):
        self.match_data = MatchData()
        self.snapshots: list(Snapshot) = []


class MatchData(dtos.basedto.BaseDto):
    def __init__(self) -> None:
        self.match_name = ""
        self.home_team = ""
        self.away_team = ""


class Snapshot(dtos.basedto.BaseDto):
    def __init__(self) -> None:
        self.statistics = Statistics()
        self.bet_list: list(BetData) = []


class BetData(dtos.basedto.BaseDto):
    def __init__(self) -> None:
        self.bet_type = BetType()


class BetType(dtos.basedto.BaseDto):
    def __init__(self):
        self.over_type = -1
        self.quota: int = 0


class Statistics(dtos.basedto.BaseDto):
    def __init__(self):
        self.minutes = 0
        self.score_home = 0
        self.score_away = 0
        self.score_sum = 0
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
