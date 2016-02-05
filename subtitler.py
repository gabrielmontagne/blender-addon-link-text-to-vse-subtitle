import bpy
from bpy.app.handlers import persistent

bl_info = { "name": "subtitle text render", "category": "Object" }

@persistent
def frame_pre(scene):
    print("Frame Change", scene.frame_current)

def register():
    print('registering')

    bpy.app.handlers.frame_change_pre.clear()
    bpy.app.handlers.frame_change_pre.append(frame_pre)


def unregister():
    print('unregistering')


if __name__ == "__main__":
    register()
