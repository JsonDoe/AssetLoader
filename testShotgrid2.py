import shotgun_api3
import datetime

sg = shotgun_api3.Shotgun("https://p3d.shotgunstudio.com/",
                                            script_name='ScriptAccessJulienM',
                                            api_key='b4llipivr(xnicpfuPyzjzyrj')



# you can use this method to get the exact time of a query
startTime = datetime.datetime.now()

fields = ["name", "id", ]
project = sg.find("Project", [["sg_status", "is", "Active"]], fields)
project1 = sg.find("Project", [["id", "is", 650 ]])
project2 = sg.find("Project", [["id", "is", 652 ]])
project3 = sg.find("Project", [["id", "is", 916 ]])

endTime = datetime.datetime.now()


print(project + project2 + project3 + project1)
print(endTime-startTime)
