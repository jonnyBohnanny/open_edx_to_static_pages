import xml.etree.ElementTree as ET

from ocx_to_html.leaf_decoder import HtmlDecoder

from ocx_to_html.leaf_decoder import VideoDecoder
from ocx_to_html.leaf_decoder import StringResponseProblemDecoder


class VerticalDecoder:
    def __init__(self, paths, navigation, vertical):
        self.buffer = ""
        self.paths = paths
        self.vertical = vertical

        path = self.paths.check_url('vertical', vertical)
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        navigation.set_subsection_name(self.root.attrib['display_name'])

    def catHtml(self, name):
        path = self.paths.check_url('html', name)
        tree = ET.parse(path)
        root = tree.getroot()
        self.buffer = self.buffer + str(HtmlDecoder.HtmlDecoder.tohtml(self.paths, root.attrib['filename']))

    def catProblem(self, name):
        path = self.paths.check_url('problem', name)
        tree = ET.parse(path)
        root = tree.getroot()
        for child in root:
            if child.tag.lower() == 'stringresponse':
                self.buffer = self.buffer + str(
                    StringResponseProblemDecoder.StringResponseProblemDecoder.tohtml(self.paths, name))
            elif child.tag.lower() == 'fake_stringresponse':
                self.buffer = self.buffer + str(
                    StringResponseProblemDecoder.StringResponseProblemDecoder.tohtml(self.paths, path))

    def catVideo(self, name):
        self.buffer += VideoDecoder.VideoDecoder.tohtml(self.paths, name)

    def cat(self):
        for child in self.root:
            if child.tag.lower() == 'html':
                self.catHtml(child.attrib['url_name'])
            elif child.tag.lower() == 'problem':
                self.catProblem(child.attrib['url_name'])
                #print("*** will not render yet: ", child.tag, child.attrib, )
                print(child.tag, child.attrib)

            elif child.tag.lower() == 'video':
                self.catVideo(child.attrib['url_name'])
                # print("*** will not render yet: ", child.tag, child.attrib, )
                # print(child.tag, child.attrib)
            else:
                pass
        return self.buffer
