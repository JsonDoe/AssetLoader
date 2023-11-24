import shotgun_api3
import datetime

sg = shotgun_api3.Shotgun("https://p3d.shotgunstudio.com/",
                                            script_name='ScriptAccessJulienM',
                                            api_key='b4llipivr(xnicpfuPyzjzyrj')



# you can use this method to get the exact time of a query
startTime = datetime.datetime.now()

fields = ["name", "id", ]
projects = sg.find("Project", [["sg_status", "is", "Active"]], fields)

for project in projects:
    if project["name"] == "DOLL":
        filters = [
            ["project", "is", {"type":"Project", "id":project["id"]}]
        ]
        assets = sg.find("Asset", filters, ["project", "code"])
        for asset in assets:
            print(asset)

endTime = datetime.datetime.now()

print(endTime-startTime)
