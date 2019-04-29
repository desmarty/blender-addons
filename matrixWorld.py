import bpy

bl_info = {
    "name": "Matrix World Data",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "Properties Editor > Navigation Bar > Matrix World Data",
    "description": "Shows Matrix World Data of a selected object",
    "category": "Object"}
    
class PanelWorldData(bpy.types.Panel):
    
    bl_label = "Matrix World Data"
    bl_idname = "OBJECT_PT_wmdata"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    
    """
    def update_object(self, context):
        obj = bpy.context.object
        wm1 = context.window_manager
        obj.location.x = wm1.xVal
        obj.location.y = wm1.yVal
        obj.location.z = wm1.zVal
    """
    
    x_loc_val = bpy.props.FloatProperty(name="x", default=0.0, description="Matrix World - X Location value")
    y_loc_val = bpy.props.FloatProperty(name="y", default=0.0, description="Matrix World - Y Location value")
    z_loc_val = bpy.props.FloatProperty(name="z", default=0.0, description="Matrix World - Z Location value")
    
    x_rot_val = bpy.props.FloatProperty(name="x", default=0.0, description="Matrix World - X Rotation value in Degrees")
    y_rot_val = bpy.props.FloatProperty(name="y", default=0.0, description="Matrix World - Y Rotation value in Degrees")
    z_rot_val = bpy.props.FloatProperty(name="z", default=0.0, description="Matrix World - Z Rotaiton value in Degrees")
    
    bpy.types.WindowManager.xLocVal = x_loc_val
    bpy.types.WindowManager.yLocVal = y_loc_val
    bpy.types.WindowManager.zLocVal = z_loc_val
    
    bpy.types.WindowManager.xRotVal = x_rot_val
    bpy.types.WindowManager.yRotVal = y_rot_val
    bpy.types.WindowManager.zRotVal = z_rot_val
    
    def draw(self, context):
        
        obj = bpy.context.object
        wLocData = obj.matrix_world.translation
        wRotData = obj.matrix_world.to_euler()
        
        wm = context.window_manager
        
        wm.xLocVal = wLocData.x
        wm.yLocVal = wLocData.y
        wm.zLocVal = wLocData.z
        
        wm.xRotVal = wRotData.x * 57.2958
        wm.yRotVal = wRotData.y * 57.2958
        wm.zRotVal = wRotData.z * 57.2958
        
        
        layout = self.layout
        
        row = layout.row()
        row.label(text="Location Data")
        
        row = layout.row()
        row.prop(wm, "xLocVal")
        
        row = layout.row()
        row.prop(wm, "yLocVal")
        
        row = layout.row()
        row.prop(wm, "zLocVal")
        
        row = layout.row()
        row.label(text="Rotation Data")
        
        row = layout.row()
        row.prop(wm, "xRotVal")
        
        row = layout.row()
        row.prop(wm, "yRotVal")
        
        row = layout.row()
        row.prop(wm, "zRotVal")
        
        
def register():
    bpy.utils.register_class(PanelWorldData)

def unregister():
    bpy.utils.unregister_class(PanelWorldData)

if __name__ == "__main__":
    register()