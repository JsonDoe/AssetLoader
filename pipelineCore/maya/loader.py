from PySide2 import QtWidgets
try: 
    from maya import cmds
    mayaContext = 1
except:
    mayaContext = 0
    pass


class Loader(object):

    def __init__(self):
        pass

    # TODO see how to implement this with DnD
    def loadAsset(self, path:str) -> None:
        """load an asset in the scene from an .ma or .abc file

        :param path: path to the file
        :type path: str
        """
        if path.endswith(".ma"):
            cmds.file(path, i=True, ignoreVersion=True,
                      mergeNamespacesOnClash=False, namespace=":")
        elif path.endswith(".abc"):
            cmds.AbcImport(path, mode='import')
        else:
            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle('Error')
            dlg.setText('Wrong file type selected')
            dlg.setStandardButtons(
                QtWidgets.QMessageBox.Ok)
            dlg.setIcon(QtWidgets.QMessageBox.Warning)
            dlg.exec()
    
    def loadAssetWithNamespace(self, path:str, assetName:str) -> None:
        """load an asset in the scene from an .ma or .abc file and place it
        into a namespace named form the asset

        :param path: asset path
        :type path: str
        :param assetName: asset name
        :type assetName: str
        """
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
        """load an asset in the scene from an .ma or .abc file as a reference

        :param path: asset path
        :type path: str
        :param assetName: asset name
        :type assetName: str
        """
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
