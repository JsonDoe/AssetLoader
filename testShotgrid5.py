from pipelineCore.shotgrid import Manager
import platform


mng = Manager()

project = mng.getProject("DOLL")
asset = project.getAsset("betty")
task = asset.getTask("modeling")

# print(project)
# print(asset)
# print(task)

for publish in task.publishedFiles:
    print(publish)
    print(publish.path)
    print(publish.versionNumber)

print(platform.system())