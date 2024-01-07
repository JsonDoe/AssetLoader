

class Entity(object):
    """Class to handle a shotgrid entity.

    :param dict: The shotgrid dictionnary of the project.
    :type shotgridDict: dict
    """
    FIELDS = [
        "sg_type",
        "id",
        "name",
        "archived",
        "sg_status",
        "sg_level"
    ]


    def __init__(self, shotgridDict=None, shotgridInstance=None):
        
        self.sgDict = shotgridDict
        self.sg = shotgridInstance

    def getEntities(self,
                    classType:object,
                    filters:list,
                    result:list) -> list[object]:
        """send a request to get the entities list.

        :param classType: type of the class
        :type classType: object

        :param filters: the request filters
        :type filters: list

        :param result: result of the request
        :type result: list

        :return: result of the request
        :rtype: list[object]
        """
        if len(result) == 0:
            result = [
                    classType(shotgridDict=data, shotgridInstance=self.sg)
                    for data in self.sg.find(
                        classType.TYPE, filters, classType.FIELDS)
                    ]
            return result
        return result

    def getEntity(self, 
                  entityName:str,
                  entityList:list) -> object:
        """get an entity in the project

        :param entityName: the entity name.
        :type entityName: str

        :param entityList: the entity list.
        :type entityList: list[Entity]

        :return: The match entity
        :rtype: Entity
        """
        for entity in entityList:
            if entity.name == entityName:
                return entity
        return None

    @property
    def type(self) -> str:
        return self.sgDict["type"]
    
    @property
    def id(self) -> int:
        return self.sgDict["id"]
    