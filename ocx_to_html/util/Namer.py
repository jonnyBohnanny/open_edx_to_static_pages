from urllib import parse


class NameNormalizer:
    @staticmethod
    def normalize(name):
        name = parse.quote_plus(name.encode('utf-8'), safe=':/')
        name = name.replace("+", "_")
        while "__" in name:
            name = name.replace("__", "_")

        name = name.lower()
        return name
