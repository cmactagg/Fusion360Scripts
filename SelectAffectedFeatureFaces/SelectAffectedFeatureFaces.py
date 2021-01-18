#Author-cmactagg
#Description-Selects all the faces that were affected by the feature

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        #ensure that there is only one selected entity 
        if ui.activeSelections.count == 1:
            selectedEntity = ui.activeSelections[0].entity
            
            #ensure that the selected entity is a Feature (all features have a 'faces' property that is iteratable)
            if isinstance(selectedEntity, adsk.fusion.Feature):
                #clear the current selected entity
                ui.activeSelections.clear()
                #loop through all the faces of the selected entity and make them selected (add them to the active selections)
                for faceFromEntity in selectedEntity.faces:
                    ui.activeSelections.add(faceFromEntity)
            else:
                ui.messageBox('Selected entity is not a feature')
        else:
            ui.messageBox('Select one feature')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
