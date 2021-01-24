#Author-cmactagg
#Description-Copies the parameter reference and applies them to another component

import adsk.core, adsk.fusion, adsk.cam, traceback
import logging

def run(context):
    ui = None
    

    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        hasMisalignment = False #whether some parameters werent able to copy due to incompatible units

        #ensure the select items are components
        if ui.activeSelections.count == 2 \
            and isinstance(ui.activeSelections[0].entity, adsk.fusion.Occurrence) \
            and isinstance(ui.activeSelections[0].entity.component, adsk.fusion.Component) \
            and isinstance(ui.activeSelections[1].entity, adsk.fusion.Occurrence) \
            and isinstance(ui.activeSelections[1].entity.component, adsk.fusion.Component):            
            comp0 =  ui.activeSelections[0].entity.component
            comp1 =  ui.activeSelections[1].entity.component

            index = 0
            #loop through the parameters of component1 and reference the parameter in component2
            for index, param in enumerate(comp0.modelParameters):  
                #only apply/copy the reference if they are the same unit type - a length parameter cant reference an angle parameter
                # if they are of different unit types, skip it and try to apply to the next parameter            
                if comp1.modelParameters.count > index and param.unit == comp1.modelParameters[index].unit:
                    comp1.modelParameters[index].expression = param.name
                    index = index + 1
                else:
                    hasMisalignment = True

        else:
            ui.messageBox('Select two components')

        if hasMisalignment:
            ui.messageBox('Some parameters were not able to copy due to the order of the parameters and incompatible units.')
                
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
