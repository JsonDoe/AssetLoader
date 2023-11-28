from pipelineCore.shotgrid.manager import Manager


class FileSelectorWidgetModel(object):

    def __init__(self):

        self._manager = Manager()

        self.currentProject = self._manager.getProject("DOLL")

        self._categories = ["Character", "Environment", "Prop"]

        

    @property
    def categories(self):
        return self.currentProject.getAssetsCategories()