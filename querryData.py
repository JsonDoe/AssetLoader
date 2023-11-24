import shotgun_api3

"""To use while outside a DCC"""

sge = shotgun_api3.Shotgun("https://p3d.shotgunstudio.com/", script_name='PipelineFramework', api_key='Nsqbkyrqmvnecs7wyk&xflhwl')


filters = [
    ["sg_status_list", "is_not", "act"],
    ["permission_rule_set", "is", {"type" : "PermissionRuleSet", "id" :18}]
]
fields = ["id", "type", "name", "sg_status_list", "permission_rule_set"]

people = sge.find("HumanUser", filters, fields)

for user in people:
    print(user)