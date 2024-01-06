from PySide2 import QtWidgets
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
    def loadAsset(self, path:str) -> None:
        """load a scene.

        :param path: the scene path
        :type path: str
        """
        if mayaContext == 1:
            if path.endswith(".ma"):
                cmds.file(path, i=True, ignoreVersion=True, mergeNamespacesOnClash=False, namespace=":")
            if path.endswith(".abc"):
                cmds.AbcImport(path, mode='import')
            else:
                dlg = QtWidgets.QMessageBox()
                dlg.setWindowTitle('Error')
                dlg.setText('Wrong file type selected')
                dlg.setStandardButtons(
                    QtWidgets.QMessageBox.Ok)
                dlg.setIcon(QtWidgets.QMessageBox.Warning)
                dlg.exec()

        if mayaContext == 0:
                dlg = QtWidgets.QMessageBox()
                dlg.setWindowTitle('Error')
                dlg.setText('Wrong file type selected')
                dlg.setStandardButtons(
                    QtWidgets.QMessageBox.Ok)
                dlg.setIcon(QtWidgets.QMessageBox.Warning)
                dlg.exec()
    
    def loadAssetWithNamespace(self, path:str, assetName:str) -> None:
            if path.endswith(".ma"):
                namespace = assetName.replace('.ma', '')
                namespace = namespace.replace('.', '_')
                cmds.file(
                    path, i=True, ignoreVersion=True,
                    mergeNamespacesOnClash=False, namespace=namespace)
                cmds.namespace(set=':')
                return
            if path.endswith(".abc"):
                namespace = assetName.replace('.abc', '')
                namespace = namespace.replace('.', '_')
                cmds.file(
                    path, i=True, ignoreVersion=True,
                    mergeNamespacesOnClash=False, namespace=namespace)
                cmds.namespace(set=':')
                return
            else:
                dlg = QtWidgets.QMessageBox()
                dlg.setWindowTitle('Error')
                dlg.setText('Wrong file type selected')
                dlg.setStandardButtons(
                    QtWidgets.QMessageBox.Ok)
                dlg.setIcon(QtWidgets.QMessageBox.Warning)
                dlg.exec()

    def loadAssetAsReference(self, path:str, assetName:str) -> None:
            if path.endswith(".ma"):
                namespace = assetName.replace('.ma', '')
                namespace = namespace.replace('.', '_')
                cmds.file(
                    path, ignoreVersion=True, mergeNamespacesOnClash=False,
                    namespace=namespace, reference=True, returnNewNodes=True)
                cmds.namespace(set=':')
                return
            if path.endswith(".abc"):
                namespace = assetName.replace('.abc', '')
                namespace = namespace.replace('.', '_')
                cmds.file(
                    path, ignoreVersion=True, mergeNamespacesOnClash=False,
                    namespace=namespace,  reference=True, returnNewNodes=True)
                cmds.namespace(set=':')
                return
            else:
                dlg = QtWidgets.QMessageBox()
                dlg.setWindowTitle('Error')
                dlg.setText('Wrong file type selected')
                dlg.setStandardButtons(
                    QtWidgets.QMessageBox.Ok)
                dlg.setIcon(QtWidgets.QMessageBox.Warning)
                dlg.exec()