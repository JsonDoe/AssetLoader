from .entityWithTasks import EntityWithTasks
from .asset import Asset


class Shot(EntityWithTasks):
    """Class to handle a shot

    :param EntityWithTasks: Inherit from a class handling the basic data of an
    entity with tasks.
    :type EntityWithTasks: object
    :return: Diverses datas of a shotgrid shot file
    :rtype: Object
    """
    TYPE = "Shot"

    FIELDS = [
        "type",
        "id",
        "code"
    ]

    def __init__(self, shotgridDict=None, shotgridInstance=None):
        super(Shot,self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance
            )

    def __repr__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.sgDict["code"]
