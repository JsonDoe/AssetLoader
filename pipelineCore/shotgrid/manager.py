inToolKit = False

#checks if we are using a DCC, if DCC use DDC else uses the shotgrid API
try:
    import  sgtk
    inToolKit = True
except:
    pass


hasShotgunAPI = False
try:
    import shotgun_api3
    hasShotgunAPI = True
except:
    pass

from.project import Project


class Manager(object):
    """Class to handle the different datas from shotgrid.

    :param object: shotgrid manager
    :type object: object
    """
    def __init__(self) -> None:
        self.sg = None

        if(inToolKit is True):
            self.sg = sgtk.platform.current_engine().shotgun
        elif(hasShotgunAPI is True):
            self.sg = shotgun_api3.Shotgun("https://p3d.shotgunstudio.com/",
                                            script_name='ScriptAccessJulienM',
                                            api_key='b4llipivr(xnicpfuPyzjzyrj')
        self._projects = []

    def filterProjectByLevel(self, text:str) -> list[Project]:
        """Filter the project if they contains the text string.

        :param text: The text to use
        :type text: str

        :return: list[Project]: filtered objects
        :rtype: list['Project']
        """

        return[project
               for project in self.projects
               if project.level if project.level.find(text) != -1]

    @property
    def projects(self) -> list[Project]:
        if len(self._projects) == 0:
            #return avec liste compréhensive
            self._projects = [
                Project(
                    shotgridDict=project, shotgridInstance=self.sg
                    ) for project in self.sg.find(
                    "Project", [], Project.FIELDS)]
            return self._projects
        return self._projects

    @property
    def activeProjects(self) -> list[Project]:
        return[
            project
            for project in self.projects
            if project.status == "Active" and project.archived == False]

    def getProject(self, name:str) -> Project:
        """Get a specific project from the project list

        :param name: name of the project
        :type name: str
        :return: object containg the various datas from a specific project
        :rtype: Project
        """
        for project in self.projects:
            if(project.name == name):
                return project
        return None
