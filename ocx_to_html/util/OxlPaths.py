import os.path


class OlxPaths(dict):
    def __init__(self, *args, **kwargs):
        self.__artifact_path = kwargs.pop('path', ".")
        dict.__init__(self, *args, **kwargs)
        # path = kwargs.pop('path', '')
        super(OlxPaths, self).__init__()
        # not used:
        ## "drafts", "problem"
        __folder_names = ["about", "assets", "chapter", "course", "policies", "policies/course",
                          "sequential", "static", "vertical", ]
        self[''] = self.__artifact_path
        for folder in __folder_names:
            full_path = os.path.join(self.__artifact_path, folder)
            if os.path.exists(full_path):
                self[folder] = full_path
            else:
                # pass
                raise ValueError('Folder ' + folder + " is missing from the export artifact.")

        __not_required_folder_names = ["drafts", "problem", "tabs", "video", "html"]
        for folder in __not_required_folder_names:
            full_path = os.path.join(self.__artifact_path, folder)
            if os.path.exists(full_path):
                self[folder] = full_path
            else:
                print('Folder ' + folder + " is missing from the export artifact, that maybe ok.")

        self.add_file("policy_json", "policies/course/policy.json")
        self.add_file("about_page", "about/overview.html")

    def add_file(self, name, path):
        full_path = os.path.join(self.__artifact_path, path)
        if os.path.exists(full_path):
            self[name] = full_path
        else:
            pass
            # TODO: find essential and non-essential paths, raise on essential paths missing
            raise ValueError('File ' + file + " is missing from the export artifact.")

    def check_url(self, type, name, file_extension='xml'):
        file_name = name + '.' + file_extension
        full_path = os.path.join(self[type], file_name)
        if os.path.exists(full_path):
            pass
        else:
            raise ValueError(type + ' ' + full_path + " is missing from the export artifact.")
        return full_path
