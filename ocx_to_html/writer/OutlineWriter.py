class OutlineWriter:
    @staticmethod
    def write(html_blob, navigation, paths):

        if navigation.subsection_name != "":
            title = navigation.course_name + " Course Outline"
            html_blob = "<h1>" + title + '</h1>' + html_blob
        else:
            title = "No Course Outline Title"

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
        page += '''<a href="''' + navigation.course_url + '''">'''+navigation.course_name +'''</a>'''
        for tab in navigation.tabs:
            page += ' | <a href="' + tab.url + '">' + tab.name + '</a>'
        page += '</div></p>'

        page += html_blob
        page +='''

</body>
</html>'''

        page = page.replace("/static", "../static")
        return page
