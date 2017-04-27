class TabWriter:
    @staticmethod
    def write(html_blob, navigation, tab):

        if navigation.subsection_name != "":
            title = tab.name
            html_blob = "<h1>" + title + "</h1>" + html_blob
        else:
            title = "No Tab Title"

        page = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
    '''
        page += "<title>" + title + "</title>"
        page += '''
</head
<body>'''

        page += '<p><div>'
        page += '''<a href="''' + navigation.course_url + '''">''' + navigation.course_name + '''</a> | '''
        page += '''<a href="''' + navigation.outline_url + '''">Course Outline</a>'''
        page += '</div></p>'
        page += html_blob

        page += '''
</body>
</html>'''

        page = page.replace("/static", "../static")
        return page