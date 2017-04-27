from ocx_to_html.util import Namer
from ocx_to_html.leaf_decoder import Tab


class Navigation():
    def __init__(self):
        self.course_name = ""
        self.course_id = ""
        self.course_url = ""

        # this page always has this name for any course
        self.outline_name = "Course Outline"
        self.outline_id = Namer.NameNormalizer.normalize(self.outline_name)
        self.outline_url = Namer.NameNormalizer.normalize(self.outline_id) + '.html'

        self.tabs = []

        self.chapter_name = ""
        self.chapter_id = ""
        self.chapter_url = ""
        self.chapter_number = 0

        self.section_name = ""
        self.section_id = ""
        self.section_url = ""
        self.section_number = 0

        self.subsection_name = ""
        self.subsection_id = ""
        self.subsection_url = ""
        self.subsection_number = 0

        self.last_subsection_url = ""
        self.next_subsection_url = ""

    def set_course_name(self, name):
        self.chapter_number = 0
        self.section_number = 0
        self.subsection_number = 0
        self.course_name = name
        self.course_id = Namer.NameNormalizer.normalize(self.course_name)
        self.course_url = Namer.NameNormalizer.normalize(self.course_id) + '.html'

    def add_tab(self,name):
        mytab = Tab.Tab()
        mytab.name = name
        mytab.id = Namer.NameNormalizer.normalize(mytab.name)
        mytab.url = Namer.NameNormalizer.normalize(mytab.id) + '.html'

        self.tabs.append(mytab)
        return mytab

    def set_chapter_name(self, name):
        self.section_number = 0
        self.subsection_number = 0
        self.chapter_number += 1
        self.chapter_name = name
        self.chapter_id = Namer.NameNormalizer.normalize(self.chapter_name) + '_' + str(self.chapter_number)
        self.chapter_url = self.outline_url + '#' + self.chapter_id

    def set_section_name(self, name):
        self.subsection_number = 0
        self.section_number += 1
        self.section_name = name
        self.section_id = Namer.NameNormalizer.normalize(
            self.section_name) + '_' + str(self.chapter_number) + '_' + str(self.section_number)
        self.section_url = self.outline_url + '#' + self.section_id

    def set_subsection_name(self, name):
        self.last_subsection_url = self.subsection_url
        self.subsection_number += 1
        self.subsection_name = name
        self.subsection_id = Namer.NameNormalizer.normalize(
            self.subsection_name) + '_' + str(self.chapter_number) + '_' + str(self.section_number) + '_' + str(
            self.subsection_number)
        self.subsection_url = Namer.NameNormalizer.normalize(self.subsection_id) + '.html'
