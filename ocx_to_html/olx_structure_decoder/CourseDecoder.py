import xml.etree.ElementTree as ET
from ocx_to_html.util import Namer


class CourseDecoder:
    @staticmethod
    def decode(paths, navigation, course):
        path = paths.check_url('course', course)
        tree = ET.parse(path)
        root = tree.getroot()

        navigation.set_course_name(root.attrib['display_name'])

        chapters = []

        for child in root:
            chapters.append(child.attrib['url_name'])

        return chapters
