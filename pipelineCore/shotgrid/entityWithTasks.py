from .entity import Entity
from .task import Task


class EntityWithTasks(Entity):

    def __init__(self, shotgridDict=None, shotgridInstance=None):
        super(EntityWithTasks,self).__init__(
            shotgridDict=shotgridDict,
            shotgridInstance=shotgridInstance
            )
        self._tasks = []
        self._filters =[
            ["entity", "is", {"type":self.TYPE, "id":self.id} ]
            ]
    
    def getTask(self, taskName:str) -> Task:
        """get a specific task from the task list

        :param taskName: name of the task
        :type taskName: str
        :return: task object containing various task data
        :rtype: Task
        """
        return self.getEntity(taskName, self.tasks)

    @property
    def tasks(self) -> list[Entity]:
        self._tasks = self.getEntities(Task, self._filters, self._tasks)
        return self._tasks
