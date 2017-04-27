class HtmlDecoder:
    @staticmethod
    def tohtml(paths, name):
        path = paths.check_url('html', name, 'html')

        with open(path, 'rb') as f:
            read_data = f.read()
        f.closed

        print("*** adding data from: " + path)
        return read_data.decode("utf-8")
