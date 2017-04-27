
class OutlineDecoder:

    @staticmethod
    def tohtml(outline):
        blob = ""
        blob += "<ol>\n"
        for chapter in outline:
            blob += "<li><h2>"
            blob +='<a id="'+chapter['id']+'">'+chapter['name']+'</a>\n'
            blob += "</h2></li>\n"

            blob += "<ol>\n"
            for section in chapter['sections']:
                blob += "<li><h3>"
                blob += '<a id="' + section['id'] + '">' + section['name'] + '</a>\n'
                blob += "</h3></li>\n"

                blob += "<ol>\n"
                for subsection in section['subsections']:
                    blob += "<li>"
                    blob += '<a href="' + subsection['url'] + '">' + subsection['name'] + '</a>\n'
                    blob += "</li>\n"
                blob += "</ol>\n"
            blob += "</ol>\n"
        blob += "</ol>\n"

        return blob
