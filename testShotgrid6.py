from pipelineCore.shotgrid import Manager
import platform


mng = Manager()

project = mng.getProject("DOLL")
asset = project.getAsset("betty")
task = asset.getTask("modeling")

# print(project)
# print(asset)
# print(task)

alembicPu = task.getPublishedFileByType("Alembic Cache")

for publish in task.getPublishedFileByType("Alembic Cache"):
    print(publish.versionNumber)
    print(publish.path)
