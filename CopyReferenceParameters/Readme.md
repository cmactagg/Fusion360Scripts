Description: A Fusion 360 script to copy the references of dimension from one component to another

Install: Copy the whole CopyReferenceParameters folder and drop it into your API/Scripts folder. 
On windows this is something similar to C:\Users\<your windows user>\AppData\Roaming\Autodesk\Autodesk Fusion 360\API\Scripts 
Restart Fusion 360

How to use: 
Select two components.  The first one (component1) being the source of the parameters, and the second one (component2) will be the destination.  
Run the script.  You can find the script in the Design workspace menu. Tools -> Add-ins -> Scrips and Add-ins -> Scripts -> My Scripts -> CopyReferenceParameters -> Run
After running the script, all the parameters for component1 will reference parameters from component2.

The parameters are copied in the order they appear in the Parameter (Change Parameter) list.  They are only copied if the unit is the same (won't copy a length parameter into an angle parameter).
If you are running this script against a freshly copied component and its original, then things should work as you expect.
But you can also run this script agaist two completely unrelated components, and get some interesting results.  
Example:  It may try to reference the diameter of a circle in a sketch in component1 to an extrude in component2.  In this case, when you change the dimension of the circle in component 1 to 100mm, the extrude in component2 will now be 100mm. 

Why use this script: 
Out of the box, Fusion 360 give you two ways to copy a component.  
Using Copy-Paste, the second instance of the component will be directly tied back to the original instance.  When ever you change anything about one of the instances, it will reflected in the other instance.
Using Copy-PasteNew, the second instance of the componet will be completely independent of the original instance.  When you change anything about one of the instances it will not reflect in the other instance.
But what if you want some aspects of your copied component to be tied back to the original, and other aspect to not be.  
For example:  if you were to model a piece of metal tubing that is 2" wide and 4" high and a wall thickness of 0.25", but you need 3 of these in you assembly, all of different lengths.  You want the width, height, and wall thickness to all reference back to the same dimension, but have the length be specific to each component.
To do this, create your first metal tubing.
Copy-PasteNew for twice, so you now have 3 components that are all independent of each other.
Select component1 and component2 and run the CopyReferenceParameters script.
Select component1 and component3 and run the CopyReferenceParameters script.
Now view the Parameters (Change Parameters) of your model.  You will see that all the parameters for component2 and component3 reference the parameters of component1.
If you change the parameters of component1, component2 and component3 will also change.  
If you enter a new length for component2, only component2 will change as the parameter no longer references back to component1.

