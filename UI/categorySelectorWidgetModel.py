from pipelineCore.shotgrid.manager import Manager
from pipelineCore.shotgrid.asset import Asset
from pipelineCore.shotgrid.task import Task
from pipelineCore.shotgrid.publishedFile import PublishedFile


class CategorySelectorWidgetModel(object):
    """Class to handle the different datas of the shotgrid entities
    """
    def __init__(self):

        self._manager = Manager()

        self.currentProject = self._manager.getProject("M13D")

        self.selectedCategory = None

        self.selectedAsset:Asset = None

        self.selectedTask:Task = None

        self.selectedPublish:PublishedFile = None


    @property
    def categories(self):
        return self.currentProject.getAssetsCategories()
    
    @property
    def categoriesList(self):
        catList = []
        for cat in self.categories:
            catList.append(cat)
        catList.append("Sequence")
        return catList

    @property
    def sequences(self):
        return self.currentProject.sequences

    @property
    def assets(self):
        return self.currentProject.getAssetsByCategory(
            category=self.selectedCategory)

    @property
    def assetList(self):
        astList = []
        for ast in self.assets:
            astList.append(ast.name)
        return astList

    @property
    def tasks(self):
        if self.selectedAsset is not None:
            return self.selectedAsset.tasks
        else:
            return None

    @property
    def taskList(self):
        if self.selectedAsset is not None:
            tskList = []
            for tsk in self.tasks:
                tskList.append(tsk.name)
            return tskList
        else:
            return None

    @property
    def publishedFiles(self):
        if self.selectedTask is not None:
            return self.selectedTask.publishedFiles
        else:
            return None

    @property
    def publishList(self):
        if self.selectedTask is not None:
            pubList = []
            for pub in self.tasks:
                pubList.append(pub.name)
            return pubList
        else:
            return None

    @property
    def shots(self):
        return self.currentProject.shots

    @property
    def shotList(self):
        shtList = []
        for sht in self.shots:
            shtList.append(sht.name)
        return shtList
