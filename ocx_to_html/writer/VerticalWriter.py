from ocx_to_html.util import Utf8UrlRepair

class VerticalWriter:
    @staticmethod
    def write(html_blob, navigation):
        print("*********** WRITING TO: " + navigation.subsection_url)

        if navigation.subsection_name != "":
            title = navigation.subsection_name
            html_blob = "<h1>" + title + "</h1>" + html_blob
        else:
            title = "No Title"

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
        page += '<a href="' + navigation.outline_url + '">' + navigation.outline_name + '</a> &gt; '
        page += '<a href="' + navigation.chapter_url + '">' + navigation.chapter_name + '</a> &gt; '
        page += '<a href="' + navigation.section_url + '">' + navigation.section_name + '</a>'
        page += '</div></p>'

        previous_next = ''

        previous_next += '<p><div>'
        if navigation.last_subsection_url != '':
            previous_next += '( <a href="' + navigation.last_subsection_url + '">Previous</a>&nbsp;'
        else:
            previous_next += '(&nbsp;'
        if navigation.next_subsection_url != '' and navigation.last_subsection_url != '':
            previous_next +='|&nbsp;'
        if navigation.next_subsection_url != '':
            previous_next += '<a href="' + navigation.next_subsection_url + '">Next</a> )'
        else:
            previous_next += ')'
        previous_next += '</div></p>'

        page += previous_next
        page += html_blob
        page += previous_next

        page += '''
</body>
</html>'''

        page = page.replace("/static", "../static")
        # TODO: this does nothing at the moment UTF-8 in src or href attributes may not work
        page = Utf8UrlRepair.Utf8UrlRepair.repair(page)
        return page
