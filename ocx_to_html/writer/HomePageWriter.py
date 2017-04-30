class HomePageWriter:
    @staticmethod
    def write(html_blob, navigation):

        if navigation.course_name != "":
            title = navigation.course_name
            html_blob = "<h1>" + title + "</h1>" + html_blob
        else:
            title = "No Course Title"

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
        page += '''<a href="''' + navigation.outline_url + '''">Course Outline</a>'''
        for tab in navigation.tabs:
            page += ' | <a href="' + tab.url + '">' + tab.name + '</a>'
        page += '</div></p>'

        # link to "Course Outline"
        # links to tabs
        page += html_blob

        page += '''
</body>
</html>'''

        page = page.replace("/static", "../static")
        return page
