import bpy
from bpy.app.handlers import persistent
from bpy.types import TextCurve

bl_info = { "name": "subtitle text render", "category": "Object" }

class SubtitleLinkerPanel(bpy.types.Panel):
    """Creates a Panel in the object properties window"""

    bl_label = "Subtitle Link"
    bl_idname = "OBJECT_PT_subtitle_link"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        # return True
        return (type(context.curve) is TextCurve)

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text="aru wor", icon='WORLD_DATA')

        row = layout.row()
        row.prop(obj, 'name')



@persistent
def frame_pre(scene):
    print("Frame Change", scene.frame_current)

def register():
    print('registering')

    # TMP
    bpy.app.handlers.frame_change_pre.clear()

    bpy.app.handlers.frame_change_pre.append(frame_pre)
    bpy.utils.register_class(SubtitleLinkerPanel)

def unregister():
    print('unregistering')

    bpy.utils.unregister_class(SubtitleLinkerPanel)
    bpy.app.handlers.frame_change_pre.remove(frame_pre)


if __name__ == "__main__":
    register()
