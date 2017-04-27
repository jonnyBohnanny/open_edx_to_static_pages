import xml.etree.ElementTree as ET

class VideoDecoder:

    @staticmethod
    def tohtml(paths, name):
        path = paths.check_url('video', name, 'xml')

        iframe_blob=""
        static_link_blob=""

        tree = ET.parse(path)
        root = tree.getroot()

        if "youtube_id_1_0" in root.attrib:
            youtube_id=root.attrib['youtube_id_1_0']
            iframe_blob='''<iframe width="560" height="315" src="https://www.youtube.com/embed/''' \
            + youtube_id.strip('"') + \
            '''" frameborder="0" allowfullscreen > </iframe >'''

        source_elements = root.findall("./source")

        if len(source_elements) == 1:
            if 'src' in source_elements[0].attrib:
                static_link = source_elements[0].attrib['src'].strip('"')
                if len(static_link) > 0:
                    static_link_blob='''<div><a href="''' + static_link + '''">open/download video</a><div>'''

        print("*** adding data from: " + path)
        print("******************************************************")
        return iframe_blob+static_link_blob
