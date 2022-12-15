import json
from types import SimpleNamespace

from superbettingcommons.utilities.json_utils import dump_function


class BaseDto:
    def to_json(self):
        return json.dumps(self, default=lambda o: dump_function(o), sort_keys=True, indent=4)

    @staticmethod
    def load_from_json(js: str):
        return json.loads(js, object_hook=lambda d: SimpleNamespace(**d))
