from pipelineCore.shotgrid.manager import Manager
from pipelineCore.shotgrid.asset import Asset


class CategorySelectorWidgetModel(object):

    def __init__(self):

        self._manager = Manager()

        self.currentProject = self._manager.getProject("DOLL")

        self.selectedCategory = None

        self.selectedAsset:Asset = None

        self.selectedTask = None

    @property
    def categories(self):
        return self.currentProject.getAssetsCategories()

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