import os.path

from ocx_to_html import CourseConverter

if __name__ == "__main__":
    if len(sys.argv) > 0:
        base = sys.argv[1]
        course = CourseConverter.CourseConverter(base)
        course.convert()

