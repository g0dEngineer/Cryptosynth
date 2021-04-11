#Author: Written from scratch, by God Bennett, Cryptosynth Labs founder
#Blender3d addon to enable cryptosynth Ai/GPT2 input and response texts as well as associated 3d behaviour 

#How to use:
#1. "I" key : *Initialize* Cryptosynth Aeon being.
#2. Right click anywhere in 3d scene (like beside the synth) to enable Cryptosynth Aeon Communicate.
#3. "T" key : Start Aeon *thinking*/reading cycle. 
#4. "R" key : Get *response* from Aeon being.


bl_info = {
    "name": "Cryptosynth Aeon Communicate",
    "author": "God Bennett",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location_": "Right click anywhere in scene > Object Context Menu > Cryptosynth Aeon Communicate",
    "location" : "[1]'I' key : *Initialize*, [2]Right click anywhere in scene/send message, [3]'T' key start Aeon think cycle, [4]'R' key get Aeon *response*",
    "description": "Cryptosynth Aeon is a sequence of artificial intelligence powered 3d beings - Crypto Art NFTs you can actually hold a conversation with.", 
    "warning": "",
    "doc_url": "facebook.com/CryptosynthLabs"
}


########################################################
#BLOCK_A. Conversational Neural Network Module
#Note 1: Setup function is invoked in aeonInitializeBeing (), before 3d model realism is invoked
#Note 2: Neural network/ai response is called in "UserTransmission" class @execute func, where aeon_output variable is updated.
from . import interact_cryptosynth 
CONVERSATIONAL_NEURAL_NETWORK = interact_cryptosynth.NeuralNetConversationalModule()


########################################################
#BLOCK_B. Cryptosynth Blender3d Modules
import bpy


def aeonInitializeBeing (context):
    CONVERSATIONAL_NEURAL_NETWORK.setup()
    
    bpy.context.scene.render.engine = 'CYCLES'
    
    #B. Enable God Bennett's original "photorealistic" fidelity/graphics
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            space = area.spaces.active
            if space.type == 'VIEW_3D':
                space.shading.type = 'RENDERED'



def printToBlenderConsole(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")   
                


class CryptosynthInitialization(bpy.types.Operator):
    bl_idname = "cryptosynth.initialization"
    bl_label = "Cryptosynth Aeon Initialization"
    bl_options = {'REGISTER', 'UNDO'}

    initializationMessage = bpy.props.StringProperty(name="")

    def execute(self, context):
        aeonInitializeBeing(context)

        return {'FINISHED'}




def _aeon_3d_action_begin_read_behaviour():
    
    #simulate reading movement
    
    #A. Prepare model for animation
    #Focus on eyes, which animate to do reading action
    #...1. Disable rendered mode (Disable God Bennett's original "photorealistic" fidelity/graphics)
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            space = area.spaces.active
            if space.type == 'VIEW_3D':
                space.shading.type = 'MATERIAL'
    #...2. Disable light/focus on overall synth, to place more focus on EYES
    bpy.data.objects['Point.002'].data.energy = 0
    #...3. Disable skin colour, to place more focus on EYES
    bpy.data.images["Std_Skin_Head_Diffuse"].colorspace_settings.name = 'Non-Color'
  
    
    #B. Start animation
    bpy.ops.screen.animation_play() 

    

def _aeon_3d_action_end_read_behaviour ():
    
    #simulate stop reading movement
    
    #A. Restore still state
    bpy.ops.screen.animation_cancel(restore_frame=True)
    bpy.ops.scene.frame_current = 0 #God Bennett's lucky guess, this reset's animation frame to 0
    
                
    #Re-focus on entire synth which restores default position prior to animation to do reading action
    
    #...2. Enable rendered mode (Enable God Bennett's original "photorealistic" fidelity/graphics)
    for area in bpy.context.screen.areas: 
        if area.type == 'VIEW_3D':
            space = area.spaces.active
            if space.type == 'VIEW_3D':
                space.shading.type = 'RENDERED'
    #...2. Restore point light/focus on synth
    bpy.data.objects['Point.002'].data.energy = 100
    #...3. Restore default skin colour, to restore focus on entire synth
    bpy.data.images["Std_Skin_Head_Diffuse"].colorspace_settings.name = 'sRGB'
      

def _aeon_3d_action_response_sequence ():
    bpy.app.timers.register(_aeon_3d_action_begin_read_behaviour, first_interval=1)
    bpy.app.timers.register(_aeon_3d_action_end_read_behaviour, first_interval=7)
    
class UserTransmission(bpy.types.Operator):
    bl_idname = "user.transmission"
    bl_label = "User Transmission"
    bl_options = {'REGISTER', 'UNDO'}

    #initializationMessage = bpy.props.StringProperty(name="")

    def execute(self, context):
        _aeon_3d_action_response_sequence()
        bpy.types.VIEW3D_MT_object_context_menu.prepend(CryptosynthDialogFunc)
        wm_c = bpy.context.window_manager
        km_c = wm_c.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi_c = km_c.keymap_items.new(CryptosynthDialog.bl_idname, 'R', 'PRESS', ctrl=False, shift=False)
        #kmi_c.properties.aeon_output = "wtf!"
        #AEON_INPUT = kmi_c.properties.user_input #This does not reflect latest user input!
        LATEST_AEON_INPUT = bpy.context.window_manager.operator_properties_last("cryptosynth.dialog")
        LATEST_AEON_INPUT = LATEST_AEON_INPUT.user_input
        #printToBlenderConsole(AEON_INPUT)
        kmi_c.properties.aeon_output = interact_cryptosynth.getNeuralNetConversationalResponse ( LATEST_AEON_INPUT, CONVERSATIONAL_NEURAL_NETWORK )
        addon_keymaps_communicate_with_aeon_being.append(km_c)
        return {'FINISHED'}

class CryptosynthDialog(bpy.types.Operator):
    bl_idname = "cryptosynth.dialog"
    bl_label = "Cryptosynth Aeon Dialog"
    bl_options = {'REGISTER', 'UNDO'}

    user_input = bpy.props.StringProperty(name="User Input", default="<To be sent to Synth-Aeon>")
    aeon_output = bpy.props.StringProperty(name="Aeon Output", default="<To be replied by Synth-Aeon>")

    
    def execute(self, context):
        pass

        return {'FINISHED'}
    

           
# store keymaps here to access after registration
addon_keymaps_communicate_with_aeon_being = []
addon_keymaps_init_aeon_being = []

def CryptosynthDialogFunc(self, context):
    self.layout.operator(CryptosynthDialog.bl_idname)
  
def register():
    ################################
    ################Communication
    bpy.utils.register_class(UserTransmission)
    bpy.utils.register_class(CryptosynthDialog)
    bpy.types.VIEW3D_MT_object_context_menu.prepend(CryptosynthDialogFunc)
    
    
    #keymap for communication
    wm_c = bpy.context.window_manager
    km_c = wm_c.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi_c = km_c.keymap_items.new(UserTransmission.bl_idname, 'T', 'PRESS', ctrl=False, shift=False)
    #kmi_c.properties.initializationMessage = "Initialization complete!"
    addon_keymaps_communicate_with_aeon_being.append(km_c)
    
    ################################
    ################initialization
    bpy.utils.register_class(CryptosynthInitialization)
    
    #keymap for initialization
    
    wm_i = bpy.context.window_manager
    km_i = wm_i.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi_i= km_i.keymap_items.new(CryptosynthInitialization.bl_idname, 'I', 'PRESS', ctrl=False, shift=False)
    kmi_i.properties.initializationMessage = "Initialization complete!"
    addon_keymaps_init_aeon_being.append(km_i)
    
def unregister():
    bpy.utils.unregister_class(CryptosynthDialog)
    bpy.types.VIEW3D_MT_object.remove(CryptosynthDialogFunc)
    bpy.utils.unregister_class(CryptosynthInitialization)
    """
    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]
    """




if __name__ == "__main__":
    register()

