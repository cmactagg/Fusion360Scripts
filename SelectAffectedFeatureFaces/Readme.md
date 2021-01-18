Description:
A Fusion 360 script to help to quickly select all the faces that were affected by a feature.

Install:
Copy the whole SelectedAffectedFeatureFaces folder to drop it into your API/Scripts folder.  On windows this is something similar to C:\Users\<your windows user>\AppData\Roaming\Autodesk\Autodesk Fusion 360\API\Scripts
Restart Fusion 360

How to use:
Select a feature in your timeline (Extrude, Combine, Rectangular Pattern, Offset Face, etc)
Run the SelectedAffectedFeatureFaces.  You can find the script in the Design workspace menu.  Tools -> Add-ins -> Scrips and Add-ins -> Scripts -> My Scripts -> SelectedAffectedFeatureFaces -> Run

Why use this script:
Often you will want to apply a new feature to the faces that were created/modified by a previous feature.  Many faces can be created by a feature, so this just makes it very easy to select them all in one step.
For example:  You want to Combine (cut) of two components, then you want to have some clearance between these two components.  Do the combine of the two components and this creates many new faces on the target body.  Instead of selected all the newly created faces by clicking each one (there may be many and its possible to miss a few), simply run the SelectedAffectedFeatureFaces script and all the new faces will be selected for you.  Now apply Offset Faces and set the offset (clearance you want between the components).
