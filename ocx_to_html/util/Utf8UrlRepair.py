from urllib import parse
import re

class Utf8UrlRepair:
    @staticmethod
    def repair(html_blob):

        # src\s*=\s*"(.+?)"
        # href\s*=\s*"(.+?)"
        # html_blob =  re.sub(r'src\s*=\s*"(.+?)"', 'src = \"\1\"',html_blob, flags=re.S)
        # s_encoded = parse.quote_plus(s.encode('utf-8'), safe=':/')

        return html_blob

