import platform
from .entity import Entity

class PublishedFile(Entity):

    TYPE = "PublishedFile"

    FIELDS = [
        "type",
        "id",
        "code",
        "path",
        "published_file_type",
        "version_number",
        "image",
        "created_at"
    ]

    def __init__(self, shotgridDict=None, shotgridInstance=None):
        super(PublishedFile, self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance
            )

    def __repr__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.sgDict["code"]
    
    @property
    def publishedFileType(self) -> dict:
        return self.sgDict["published_file_type"]
    
    @property
    def publishType(self):
        return self.publishedFileType["name"]
    @property
    def pathDict(self) -> dict:
        return self.sgDict["path"]
    
    @property
    def versionNumber(self) -> int:
        return self.sgDict["version_number"]
    
    @property
    def thumbnailURL(self):
        return self.sgDict["image"]

    @property
    def createdAt(self):
        return self.sgDict["created_at"]


    @property
    def path(self): # TODO fix 
        sys = platform.system()
        if sys == "Windows":
            return self.pathDict["local_path_windows"]
        if sys == "Darwin":
            return self.pathDict["local_path_mac"]
        if sys == "Linux":
            return self.pathDict["local_path_linux"]
        return None
