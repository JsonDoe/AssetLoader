from pipelineCore.shotgrid import Manager

mng = Manager()

project = mng.getProject("DOLL")

print(project.shots)


