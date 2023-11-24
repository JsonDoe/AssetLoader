import shotgun_api3

"""To use while outside a DCC"""

sge = shotgun_api3.Shotgun("https://p3d.shotgunstudio.com/", script_name='PipelineFramework', api_key='qxcmfx-iRqncmb9bekxypdqya')


filters = [
]
fields = ["id", "type", "name"]

people = sge.find("Project", filters, fields)

for user in people:
    print(user)