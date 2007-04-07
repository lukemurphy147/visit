# ----------------------------------------------------------------------------
#  CLASSES: nightly
#
#  ENV: VISIT_SILO_DONT_FORCE_SINGLE=1
#
#  Test Case:  xform_precision.py 
#
#  Tests:      Transform manager's conversion to float 
#
#  Programmer: Mark C. Miller
#  Date:       September 24, 2006 
#
# ----------------------------------------------------------------------------

# Turn off all annotation
a = AnnotationAttributes()
a.axesFlag2D = 0
a.axesFlag = 0
a.triadFlag = 0
a.bboxFlag = 0
a.userInfoFlag = 0
a.databaseInfoFlag = 0
a.legendInfoFlag = 0
a.backgroundMode = 0
a.foregroundColor = (0, 0, 0, 255)
a.backgroundColor = (255, 255, 255, 255)
SetAnnotationAttributes(a)

OpenDatabase("../data/quad_disk.silo")

#
# Test ordinary float data (no conversion) first
#
AddPlot("Mesh","mesh")
DrawPlots()
Test("float_xform_01")
DeleteAllPlots()

#
# Ok, now read a mesh with double coords
#
AddPlot("Mesh","meshD")
DrawPlots()
Test("float_xform_02")
DeleteAllPlots()

CloseDatabase("../data/quad_disk.silo")
OpenDatabase("../data/quad_disk.silo")

#
# test float data on a float mesh
#
AddPlot("Pseudocolor","sphElev_on_mesh")
DrawPlots()
Test("float_xform_03")
DeleteAllPlots()

#
# test float data on a double mesh
#
AddPlot("Pseudocolor","sphElev_on_meshD")
DrawPlots()
Test("float_xform_04")
DeleteAllPlots()

#
# test double data on a float mesh
#
AddPlot("Pseudocolor","sphElevD_on_mesh")
DrawPlots()
Test("float_xform_05")
DeleteAllPlots()

CloseDatabase("../data/quad_disk.silo")
OpenDatabase("../data/quad_disk.silo")

#
# test double data on a double mesh
#
AddPlot("Pseudocolor","sphElevD_on_meshD")
DrawPlots()
Test("float_xform_06")
DeleteAllPlots()

Exit()
