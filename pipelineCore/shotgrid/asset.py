from .entityWithTasks import EntityWithTasks


class Asset(EntityWithTasks):
    """Classe to handle a shotgrid asset

    :param EntityWithTasks: Class to handle a shotgrid entity with task
    :type EntityWithTasks: object
    :return: various datas of the shotgrid asset
    :rtype: object
    """
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
