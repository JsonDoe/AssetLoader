from pipelineCore.shotgrid import Manager

mng = Manager()

project = mng.getProject("DOLL")

for asset in project.assets:
    print(asset)


