from pipelineCore.shotgrid import Manager

mng = Manager()

project = mng.getProject("DOLL")
asset = project.getAsset("babyDolls")

print(project)
print(project._assets)
print(asset)

for task in asset.tasks:
    print(task)

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

