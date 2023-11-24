# to use in maya while in a task context

import sgtk


"""gather data while in a scene"""

# get the current engine
engine = sgtk.platform.current_engine()

# via this shotgun you can acces all the queries and  datas
sg = engine.shotgun

project = sgtk.platform.project

entity = engine.context.entity

step = engine.context.step

task = engine.context.task

print(entity)