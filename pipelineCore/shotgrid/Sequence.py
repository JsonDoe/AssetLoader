from .entityWithTasks import EntityWithTasks
from .asset import Asset
from .shot import Shot


class Sequence(EntityWithTasks):
    """Class to handle a sequence entity

    :param EntityWithTasks: Inherit from a class handling the basic data of an
    entity with tasks.
    :type EntityWithTasks: object
    :return: Diverses datas of a shotgrid sequence file
    :rtype: Object
    """
    TYPE = "Sequence"

    FIELDS = [
        "type",
        "id",
        "code"
    ]

    def __init__(self, shotgridDict=None, shotgridInstance=None):
        super(Sequence,self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance
            )
        self._shots     = []
        self.filters    = [
            ["sg_sequence", "is", {"type":self.TYPE, "id":self.id}]
        ]

    def __repr__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.sgDict["code"]

    @property
    def shots(self) -> list[Shot]:
        self._shots = self.getEntities(Shot, self.filters, self._shots)
        return self._shots
