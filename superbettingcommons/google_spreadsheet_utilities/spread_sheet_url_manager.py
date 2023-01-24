from superbettingcommons.utilities.environment_utils import load_env_var
from superbettingcommons.google_spreadsheet_utilities.url_manager_base import _UrlProvider

class SpreadSheetUrlProvider(_UrlProvider):
    def get_scopes(self):
        scopes = [load_env_var("SPREADSHEET_SERVICE_ACCOUNT_SCOPE_FEEDS"), load_env_var("SPREADSHEET_SERVICE_ACCOUNT_SCOPE_DRIVE")]
        return [self._get_url_(x) for x in scopes]

    def get_base_url(self):
        return self._get_url_(load_env_var("SPREADSHEET_URL"))

