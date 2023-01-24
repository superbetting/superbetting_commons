import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
from superbettingcommons.utilities.environment_utils import load_env_var
from superbettingcommons.google_spreadsheet_utilities.spread_sheet_url_manager import SpreadSheetUrlProvider

sheet_url_manager = SpreadSheetUrlProvider()


def get_worksheet_or_clone_template(sheet_name: str, worksheet_title: str, worksheet_template_title: str):
    try:
        return get_worksheet_by_name(sheet_name, worksheet_title)
    except Exception as e:
        print(e)
        sheet = get_sheet_by_name(sheet_name)
        sheet.duplicate_sheet(sheet.worksheet(worksheet_template_title).id, new_sheet_name=worksheet_title)
        return sheet.worksheet(worksheet_title)


def get_sheet_by_name(name: str) -> Spreadsheet:
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        filename=load_env_var("SPREADSHEET_CREDENTIALS_FILENAME"),
        scopes=sheet_url_manager.get_scopes()
    )

    client = gspread.authorize(credentials)
    return client.open(name)


def get_worksheet_by_name(sheet_name: str, worksheet_title: str) -> Worksheet:
    sheet = get_sheet_by_name(sheet_name)
    return sheet.worksheet(title=worksheet_title)


def get_sheet() -> Spreadsheet:
    return get_sheet_by_name(load_env_var("SPREADSHEET_NAME"))


def get_worksheet() -> Worksheet:
    return get_worksheet_by_name(load_env_var("SPREADSHEET_NAME"), load_env_var("WORKSHEET_ADMIN_MODULE_NAME"))
