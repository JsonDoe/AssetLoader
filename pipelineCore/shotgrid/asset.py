from .entityWithTasks import EntityWithTasks


class Asset(EntityWithTasks):

    TYPE = "Asset"

    FIELDS = [
        "type",
        "id", 
        "code",
        "sg_asset_type",
        "sg_status_list",
        "sg_level"
    ]

    def __init__(self, shotgridDict=None, shotgridInstance=None):
        super(Asset, self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance)
        
    def __repr__(self) -> str:
        return self.name


    @property
    def name(self) -> str:
        return self.sgDict["code"]

    @property
    def list(self) -> str:
        return self.sgDict["sg_status_list"]

    @property
    def category(self) -> str:
        return self.sgDict["sg_asset_type"]
    
    # @property
    # def category(self) -> str:
    #     return self.sgDict["sg_asset_category"] #TODO verify