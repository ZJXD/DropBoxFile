import arcpy
arcpy.env.workspace = "D:\数据\BufferDemo"
arcpy.Buffer_analysis("point", "D:\数据\BufferDemo", "10000 Feet", "FULL", "ROUND", "LIST", "Distance")
