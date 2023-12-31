from typing import Optional
from PySide2 import QtWidgets, QtCore, QtGui
import PySide2.QtGui
from pipelineCore.shotgrid.task import Task


class TaskWidget(QtWidgets.QFrame):
    """Student Widget
    """
    def __init__(self, task:Task) -> None:
        super(TaskWidget, self).__init__()

        self._task = task

        self.selected = False

        self.initUI()

    def initUI(self):
        """creates and organizes the UI.
        """
        self.mainLayout = QtWidgets.QGridLayout()

        self.nameWidget = QtWidgets.QLabel(self._task.name)

        self.mainLayout.addWidget(self.nameWidget)

        self.setLayout(self.mainLayout)
    

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:

        print("selected %s" % self._task)

        # self.parent().parent().parent().parent().unSelectAll() # TODO adapt 

        if (event.button() == QtCore.Qt.LeftButton):
            self.widgetSelected.emit(self)
            self.selected = True
        
        self.parent().parent().parent().parent().handler.selectedTask = self._task

        self.parent().parent().parent().parent().publishView.refresh() 

        # print(self.parent().parent().parent().parent().handler.assets)


TaskWidget.widgetSelected = QtCore.Signal(TaskWidget)
