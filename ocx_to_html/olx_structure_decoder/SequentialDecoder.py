import xml.etree.ElementTree as ET
from ocx_to_html.util import Namer


class SequentialDecoder:
    @staticmethod
    def decode(paths, navigation, sequential):
        path = paths.check_url('sequential', sequential)
        tree = ET.parse(path)
        root = tree.getroot()

        navigation.set_section_name(root.attrib['display_name'])

        verticals = []

        for child in root:
            verticals.append(child.attrib['url_name'])

        return verticals
