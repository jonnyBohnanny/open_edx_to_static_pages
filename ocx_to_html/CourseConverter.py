import os.path
import os
import json
import copy

from ocx_to_html.olx_structure_decoder import VerticalDecoder
from ocx_to_html.olx_structure_decoder import CourseDecoder
from ocx_to_html.olx_structure_decoder import ChapterDecoder
from ocx_to_html.olx_structure_decoder import SequentialDecoder

from ocx_to_html.leaf_decoder import TabsDecoder
from ocx_to_html.leaf_decoder import AboutDecoder
from ocx_to_html.derived_decoder import OutlineDecoder

from ocx_to_html.writer import VerticalWriter
from ocx_to_html.writer import TabWriter
from ocx_to_html.writer import HomePageWriter
from ocx_to_html.writer import OutlineWriter

from ocx_to_html.util import OxlPaths
from ocx_to_html.util import Navigation


# TODO: output warning when linking content that does not exist

class CourseConverter:
    def __init__(self, path):
        self.path = path
        self.output_path = os.path.join(self.path, 'no_open_edx')

    def convert(self):
        paths = OxlPaths.OlxPaths(path=self.path)

        navigation = Navigation.Navigation()
        self.create_output_directory()
        outline = []

        policy = self.load_policy(paths)
        chapters = CourseDecoder.CourseDecoder.decode(paths, navigation, 'course')
        tabs = TabsDecoder.TabsDecoder.decode(paths, navigation, policy)

        # home page
        data = AboutDecoder.AboutDecoder.tohtml(paths, 'overview')
        data = HomePageWriter.HomePageWriter.write(data, navigation)
        with open(self.output_path + '/' + navigation.course_id + '.html', 'wb+') as f:
            b = bytes(data, 'utf-8')
            f.write(b)
        f.closed

        # tabs
        for tab in tabs:
            print("############ TAB ###################")
            data = TabWriter.TabWriter.write(tab['data'], navigation, tab['tab'])
            with open(self.output_path + '/' + tab['tab'].id + '.html', 'wb+') as f:
                b = bytes(data, 'utf-8')
                f.write(b)
            f.closed

        # home page


        # chapters
        chapters = CourseDecoder.CourseDecoder.decode(paths, navigation, 'course')
        print(navigation.course_name)
        print(navigation.course_url)

        c = None
        last_vertical = None
        last_nav = None
        for chapter in chapters:
            sequantials = ChapterDecoder.ChapterDecoder.decode(paths, navigation, chapter)
            o_c = {'name': navigation.chapter_name, 'id': navigation.chapter_id, 'sections': []}
            outline.append(o_c)

            for sequential in sequantials:
                verticals = SequentialDecoder.SequentialDecoder.decode(paths, navigation, sequential)
                o_s = {'name': navigation.section_name, 'id': navigation.section_id, 'subsections': []}
                o_c['sections'].append(o_s)

                for vertical in verticals:
                    c = VerticalDecoder.VerticalDecoder(paths, navigation, vertical)
                    o_ss = {'name': navigation.subsection_name, 'url': navigation.subsection_url}
                    o_s['subsections'].append(o_ss)

                    if last_nav:
                        last_nav.next_subsection_url = navigation.subsection_url
                        last_nav.next_subsection_url = navigation.subsection_url
                        data = VerticalWriter.VerticalWriter.write(last_vertical.cat(), last_nav)
                        with open(self.output_path + '/' + last_nav.subsection_id +'.html', 'wb+') as f:
                            b = bytes(data, 'utf-8')
                            f.write(b)
                        f.closed
                    last_vertical = c
                    last_nav = copy.deepcopy(navigation)


        navigation.next_subsection_url = ""
        data = VerticalWriter.VerticalWriter.write(c.cat(), navigation)
        with open(self.output_path + '/' + navigation.subsection_url, 'wb+') as f:
            b = bytes(data, 'utf-8')
            f.write(b)
        f.closed

        data = OutlineDecoder.OutlineDecoder.tohtml(outline)
        data = OutlineWriter.OutlineWriter.write(data, navigation, paths)
        with open(self.output_path + '/' + navigation.outline_id + '.html', 'wb+') as f:
            b = bytes(data, 'utf-8')
            f.write(b)
        f.closed

    def create_output_directory(self):

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        for the_file in os.listdir(self.output_path):
            file_path = os.path.join(self.output_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    def load_policy(self, paths):

        with open(paths["policy_json"], 'r') as f:
            policy = json.load(f)
        f.closed
        return policy
