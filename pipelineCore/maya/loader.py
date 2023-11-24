

try: 
    from maya import cmds
except:
    pass

class Loader(object):

    def __init__(self):
        pass

    # TODO see how to implement this with DnD
    def loadScene(self, path:str) -> None:
        """load a scene.

        :param path: the scene path
        :type path: str
        """

        cmds.file(path, o=True, force=True)