class ConfigurationDto:

    def __init__(self):
        self.name = ""
        self.min_gt = ""
        self.max_gt = ""
        self.min_minute = ""
        self.max_minute = -1
        self.min_quota = -1
        self.max_quota = -1
        self.collection_name = ""
        self.bet_exchange = ""
        self.min_attacchi=0
        self.max_attacchi=0

    def load_from_json(self, js: dict):
        self.name = js['name']
        self.min_gt = round(js['min_gt'], 2) if "min_gt" in js else "0"
        self.max_gt = round(js['max_gt'], 2) if "max_gt" in js else "0"
        self.min_minute = js['min_minute'] if "min_minute" in js else "0"
        self.max_minute = js['max_minute'] if "max_minute" in js else "0"
        self.min_quota = round(js['min_quota'], 2) if "min_quota" in js else "0"
        self.max_quota = round(js['max_quota'], 2) if "max_quota" in js else "0"
        self.collection_name = js['collection_name'] if "collection_name" in js else ""
        self.bet_exchange = js['bet_exchange'] if "bet_exchange" in js else ""
        self.min_attacchi = js['min_attacchi'] if "min_attacchi" in js else 0
        self.max_attacchi = js['max_attacchi'] if "max_attacchi" in js else 0


def get_configuration_from_json(js: dict):
    configuration = ConfigurationDto()
    configuration.load_from_json(js)
    return configuration
