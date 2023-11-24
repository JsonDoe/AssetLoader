inToolKit = False

#permet de tester si l'on est dans un DCC, if DCC utilise le DDC else utilise par l'API shotgrid
try:
    import  sgtk
    inToolKit = True
except:
    pass


hasShotgunAPI = False
try:
    import shotgun_api3
    hasShotgunAPI = True
except:
    pass

print(inToolKit)
print(hasShotgunAPI)

shotgrid = None

if(inToolKit is True):
    shotgrid = sgtk.platform.current_engine().shotgun
elif(hasShotgunAPI is True):
    shotgrid = shotgun_api3.Shotgun("https://p3d.shotgunstudio.com/",
                                    script_name='ScriptAccessJulienM',
                                    api_key='b4llipivr(xnicpfuPyzjzyrj')
    

# define the request filters.
filters = [["sg_status", "is", "Active"]]
# define the field filters.
fields = ["name", "id", "type", "sg_description", "updated_at", "updated_by"]
# Send request
projects = shotgrid.find("Project", filters, fields)

for project in projects:
    print(project)
