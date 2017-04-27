import os
from ocx_to_html.leaf_decoder import Tab


class TabsDecoder:
    @staticmethod
    def decode(paths, navigation, policy):
        tabs = []
        for j_tab in policy['course/course']['tabs']:
            if j_tab['type'] == "static_tab" and j_tab['course_staff_only'] == False:
                tab = j_tab["url_slug"]
                path = paths.check_url('tabs', tab, 'html')

                if path:
                    name = j_tab["name"]
                    t = navigation.add_tab(name)

                    with open(path, 'rb') as f:
                        read_data = f.read()
                    f.closed

                    print("*** adding data from: " + path)
                    tabs.append({"data": read_data.decode("utf-8"), "tab": t})
        return tabs




        # "course_staff_only": false,
        # "name": "Special Conditions",
        # "type": "static_tab",
        # "url_slug": "a5f2531487f9477fa17dff6560714d3c"
