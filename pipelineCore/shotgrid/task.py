from .entity import Entity
from .publishedFile import PublishedFile


class Task(Entity):
    """Class to handle a task

    :param Entity: Inherit from a class handling the basic data of an
    entity with tasks.
    :type Entity: object
    :return: Diverses datas of a shotgrid task file
    :rtype: Object
    """
    TYPE = "Task"

    FIELDS = [
        "type",
        "id",
        "content",
        "sg_status_list"
    ]

    def __init__(self, shotgridDict=None, shotgridInstance=None):
        super(Task, self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance
            )
        self._publishedFiles    = []
        self._filters           = [
            ["task", "is", {"type":self.TYPE, "id":self.id}]
        ]

    def __repr__(self) -> str:
        return self.name

    def getPublishedFileByType(self, typeName:str) -> list[PublishedFile]:
        """get the published file that match the type name.

        :param typeName: the type name
        :type typeName: str
        :return: the published files or []
        :rtype: list[PublishedFile]
        """
        return [publish
                for publish in self.publishedFiles
                if publish.publishType == typeName]

    @property
    def name(self) -> str:
        return self.sgDict["content"]
    
    @property
    def publishedFiles(self) -> list[PublishedFile]:
        self._publishedFiles = self.getEntities(
            PublishedFile, self._filters, self._publishedFiles)
        return sorted(self._publishedFiles, key=lambda x: x.versionNumber, reverse=True)
    
    @property
    def status(self) -> str:
        return self.sgDict["sg_status_list"]
