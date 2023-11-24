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
    

DOLL = shotgrid.find(
    "Project", [["name", "is", "DOLL"]], ["id"])

# define the request filters.
filters = [
    ["project", 'is', {"type":"Project", "id" : DOLL[0]['id']}],
    ["sg_asset_type", "is", "Character"],
    ["sg_status_list", "is", "ip"]]
# define the field filters.
fields = ["name", "id", "code", "sg_asset_type", "sg_status_list",]
# Send request
projects = shotgrid.find("Asset", filters, fields)

for project in projects:
    print(project)