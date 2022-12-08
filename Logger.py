import datetime
import os
from inspect import getframeinfo, currentframe

import requests

TRACE = "TRACE"
DEBUG = "DEBUG"
INFO = "INFO"
WARNING = "WARN"
ERROR = "ERROR"
FATAL = "FATAL"


class Logger:
    _FOLDER_NAME = "Logs"

    def __init__(self, owner_name, can_logonfile, can_logelastic):
        self.owner_name = owner_name
        self.can_logonfile = can_logonfile
        self.can_logelastic = can_logelastic
        self.elastic_host = ""
        self.elastic_username = ""
        self.elastic_password = ""
        self.elastic_index = ""

    def configure_elastic(self, host, username, password, index):
        self.elastic_host = host
        self.elastic_username = username
        self.elastic_password = password
        self.elastic_index = index

    def remove_old_logs(self, number_of_days):
        try:
            path_list = os.listdir(self._FOLDER_NAME)
            path_list_length = len(path_list)
            if path_list_length <= number_of_days:
                return
            to_remove = path_list_length - number_of_days
            for indexToRemove in range(0, to_remove):
                os.remove(self._FOLDER_NAME + '/' + path_list[indexToRemove])
        except Exception as e:
            print("Can't remove old logs")

    def trace(self, message: str, *args, **kwargs):
        frameinfo = getframeinfo(currentframe())
        self._log(TRACE, message, frameinfo, *args, **kwargs)

    def debug(self, message: str, *args, **kwargs):
        frameinfo = getframeinfo(currentframe())
        self._log(DEBUG, message, frameinfo, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        frameinfo = getframeinfo(currentframe())
        self._log(INFO, message, frameinfo, *args, **kwargs)

    def warn(self, message: str, *args, **kwargs):
        frameinfo = getframeinfo(currentframe())
        self._log(WARNING, message, frameinfo, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        frameinfo = getframeinfo(currentframe())
        self._log(ERROR, message, frameinfo, *args, **kwargs)

    def fatal(self, message: str, *args, **kwargs):
        frameinfo = getframeinfo(currentframe())
        self._log(FATAL, message, frameinfo, *args, **kwargs)

    def _log(self, lvl, message: str, frameinfo, *args, **kwargs):
        try:
            message = message.format(*args, **kwargs)
            current_log = self._get_current_log_(lvl, message)
            print(current_log)
            d = datetime.datetime.today()
            if self.can_logonfile:
                self._write_on_file_(current_log, d)
            if self.can_logelastic:
                self.write_elastic(d, lvl, message, frameinfo, *args, **kwargs)
        except Exception as e:
            pass

    def _get_current_log_(self, level, message):
        return "[{}]|{}|{} --> {}".format(
            datetime.datetime.today(),
            level,
            self.owner_name,
            message
        )

    def write_elastic(self, d, lvl, message, frameinfo, *args, **kwargs):
        try:
            metadata = {'args': args}
            for x in kwargs:
                metadata[x] = kwargs[x]
            dumps = {
                "@timestamp": datetime.datetime.now().timestamp() * 1000,
                "app_name": self.owner_name,
                "level": lvl,
                "message": message,
                "metadata": f"{metadata}",
                "project": "superbetting",
                "trace": f"{frameinfo.filename}:{frameinfo.lineno}"
            }
            requests.post(f"https://{self.elastic_host}/{self.elastic_index}/_doc", auth=(self.elastic_username,
                                                                                          self.elastic_password),
                          json=dumps, verify=False)
        except Exception as e:
            print("Can't write to elastic {}".format(e))

    def _write_on_file_(self, current_log, d):
        try:
            with open(self._get_log_file_path_(d), "a+") as f:
                if f is None:
                    return

                f.write(current_log + "\n")
        except Exception as e:
            print("Can't write on file {}".format(e))

    def _get_log_file_path_(self, d):
        return "{}/{}_{}_{}_{}.txt".format(
            self._FOLDER_NAME,
            self.owner_name,
            d.day,
            d.month,
            d.year
        )
