from .entity import Entity
from .asset import Asset
from.Sequence import Sequence

class Project(Entity):
    """Class to handle a shotgrid project.

    :param dict: The shotgrid dictionnary of the project.
    :type shotgridDict: dict

    """

    TYPE = "Project"

    FIELDS = [
        "sg_type",
        "id",
        "name",
        "archived",
        "sg_status",
        "sg_level"
        ]

    def __init__(self, shotgridDict=None, shotgridInstance=None) -> None:
        super(Project, self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance)
        self._assets    = []
        self._sequences = []
        self._filters   = [
            ["project", "is", {"type": self.TYPE,"id":self.id}]
            ]
    
    def __repr__(self) -> str:
        return self.name

    def getAssetsCategories(self) -> list[str]:
        """Get list of the of the categories from the list of assets.

        :return: The categories list.
        :rtype: list[str]
        """
        listCategories = []

        for asset in self.assets:
            if(asset.category not in listCategories):
                listCategories.append(asset.category)

        return listCategories


    def getAssetsByCategory(
            self, category:str) -> list[Asset]:
        """get all assets that match the category.

        :param category: The name of the category.
        :type category: str

        :return: The asset that match.
        :rtype: list[Asset]
        """
        return [asset
                for asset in self.assets
                if asset.category == category]


    def getAsset(self, assetName:str) -> Asset:
        return self.getEntity(assetName, self.assets)
            
    def getSequence(self, sequenceName:str) -> Sequence:
        return self.getEntity(sequenceName, self.sequences)

    """    @property
    def assets(self) -> list[Asset]:
        if len(self._assets) == 0:
            filters = [
                ["project", "is", {"type": "Project", "id": self.id}]
                       ]
            self._assets = [
                Asset(shotgridDict=asset, shotgridInstance=self.sg)
                for asset in self.sg.find("Asset", filters, Asset.FIELDS)
                ]
            return self._assets
        return self._assets"""

    @property
    def name(self) -> str:
        return self.sgDict["name"]
    
    @name.setter
    def name(self, value:str) -> None:
        self.sgDict["name"] = value

    @property
    def status(self) -> str:
        return self.sgDict["sg_status"]

    @property
    def archived(self) -> str:
        return self.sgDict["archived"]

    @property
    def level(self) -> str:
        return self.sgDict["sg_level"]
    # ensuite on va y définir des fonctions pour récupérer les diffents objets contenu dans le projet (asset, users, ect)

    """    @property
    def sequences(self) -> list[Sequence]:
        if len(self._sequences) == 0:
            filters = [
                ["project", "is", {"type": "Project", "id": self.id}]
                       ]
            self._sequences = [
                Sequence(shotgridDict=sequence, shotgridInstance=self.sg)
                for sequence in self.sg.find("Sequence", filters, Sequence.FIELDS)
                ]
            return self._sequences
        return self._sequences"""
    
    @property
    def sequences(self):
        self._sequences = self.getEntities(
            Sequence, self._filters, self._sequences)
        return self._sequences
    
    @property
    def assets(self):
        self._assets = self.getEntities(
            Asset, self._assets, self._assets)
        return self._assets

