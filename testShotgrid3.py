from pipelineCore.shotgrid import Manager

mng = Manager()

project = mng.getProject("DOLL")

"""
for asset in project.assets:
    print(asset)

for asset in project.assets:
    print(asset)
"""

"""assetCat = project.getAssetsCategories()

for cat in assetCat:
    print(cat)
    assets = project.getAssetsByCategory(cat)
    print(assets)
"""
# print(project.getAssetsByCategory("Character"))

# for sequence in project.sequences:
#     print(sequence)
#     print(sequence.shots)

for shot in project.sequences:
    print(shot.tasks)
