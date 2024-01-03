
try: 
    from maya import cmds
    mayaContext = 1
except:
    mayaContext = 0
    pass

"""// Warning: file: C:/Program Files/Autodesk/Maya2023/scripts/others/setWorkingDirectory.mel line 233: P:/shows/M13D/assets/Character/bob/work/MDL/maya/scenes is not a valid directory.  Using P:/shows/M13D/assets/Character/bob/work/MDL/maya/ instead.
file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "MDL_bob_master_v001" -options "v=0;"  -pr  -importTimeRange "combine" "P:/SHOWS/M13D/assets/Character/bob/work/MDL/maya/MDL_bob_master.v001.ma";"""


class Loader(object):

    def __init__(self):
        pass

    # TODO see how to implement this with DnD
    def loadScene(self, path:str) -> None:
        """load a scene.

        :param path: the scene path
        :type path: str
        """
        if mayaContext == 1:
            cmds.file(path, o=True, force=True)
        if mayaContext == 0:
            print("load")
