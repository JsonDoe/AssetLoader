from pipelineCore.shotgrid.manager import Manager
from pipelineCore.shotgrid.asset import Asset
from pipelineCore.shotgrid.task import Task
from pipelineCore.shotgrid.publishedFile import PublishedFile


class CategorySelectorWidgetModel(object):

    def __init__(self):

        self._manager = Manager()

        self.currentProject = self._manager.getProject("SOUR")

        self.selectedCategory = None

        self.selectedAsset:Asset = None

        self.selectedTask:Task = None

        self.selectedPublish:PublishedFile = None

    @property
    def categories(self):
        return self.currentProject.getAssetsCategories()
    
    @property
    def sequences(self):
        return self.currentProject.sequences

    @property
    def assets(self):
        return self.currentProject.getAssetsByCategory(
            category=self.selectedCategory)

    @property
    def tasks(self):
        if self.selectedAsset is not None:
            return self.selectedAsset.tasks
        else:
            return None

    @property
    def publishedFiles(self):
        if self.selectedTask is not None:
            return self.selectedTask.publishedFiles
        else:
            return None