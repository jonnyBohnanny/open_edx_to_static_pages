import xml.etree.ElementTree as ET
from ocx_to_html.util import Namer


class ChapterDecoder:
    @staticmethod
    def decode(paths, navigation, chapter):
        path = paths.check_url('chapter', chapter)
        tree = ET.parse(path)
        root = tree.getroot()

        navigation.set_chapter_name(root.attrib['display_name'])

        sequentials = []

        for child in root:
            sequentials.append(child.attrib['url_name'])

        return sequentials
