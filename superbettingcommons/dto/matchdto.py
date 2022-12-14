from datetime import datetime


class MatchDto:

    def __init__(self):
        self.event_id = ""
        self.match_name = ""
        self.match_team_1 = ""
        self.match_team_2 = ""
        self.point_1 = -1
        self.point_2 = -1
        self.minutes = -1
        self.goal_interceptor = 0
        self.over_type = -1
        self.closed = False
        self.modified = False
        self.closed_date: datetime = None
        self.modified_date: datetime = None
        self.scanned_date: datetime = None
        self.last_results: list = []
        self.attacchi: int = 0
        self.quota: int = 0
        self.multiplier: int = -1

    def to_mongo_object(self) -> dict:
        return {
            "_id": self.match_name + self.event_id,
            "event_id": self.event_id,
            "match_name": self.match_name,
            "match_team_1": self.match_team_1,
            "match_team_2": self.match_team_2,
            "point_1": self.point_1,
            "point_2": self.point_2,
            "minutes": self.minutes,
            "goal_interceptor": self.goal_interceptor,
            "over_type": self.over_type,
            "closed": self.closed,
            "modified": self.modified,
            "closed_date": self.closed_date,
            "modified_date": self.modified_date,
            "scanned_date": self.scanned_date,
            "quota": self.quota,
            "attacchi": self.attacchi,
            "multiplier": self.multiplier
        }

    def load_from_json(self, js: dict):
        self.event_id = js['event_id']
        self.match_team_1 = js['match_team_1']
        self.match_team_2 = js['match_team_2']
        self.point_1 = js['point_1']
        self.point_2 = js['point_2']
        self.minutes = js['minutes']
        self.goal_interceptor = round(js['goal_interceptor'], 2) if "goal_interceptor" in js else "0"
        self.match_name = js['match_name'] if 'match_name' in js is not None else ""
        self.over_type = js['over_type'] if 'over_type' in js else "-1"
        self.closed = js['closed'] if 'closed' in js else False
        self.modified = js['modified'] if 'modified' in js else False
        self.closed_date = js['closed_date'] if 'closed_date' in js else None
        self.modified_date = js['modified_date'] if 'modified_date' in js else None
        self.scanned_date = js['scanned_date'] if 'scanned_date' in js else None
        self.quota = js['quota'] if 'quota' in js else 0
        self.attacchi = js['attacchi'] if 'attacchi' in js else 0
        self.multiplier = js['multiplier'] if 'multiplier' in js else -1

def get_match_from_json(js: dict):
    match = MatchDto()
    match.load_from_json(js)
    return match
