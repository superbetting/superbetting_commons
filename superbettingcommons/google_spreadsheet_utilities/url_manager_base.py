from furl import furl

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
    "Content-Type": "application/json"
}


class _UrlProvider:
    @staticmethod
    def _get_url_(base_url, path= None, params_dict= None):
        f = furl(base_url)

        if path is not None:
            f.path = path

        if params_dict is not None:
            for param in params_dict.keys():
                param_value = params_dict[param]
                f.add({param: param_value})

        return f.url
