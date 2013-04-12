import GPS

def run_helper():
    """This is helper function with reference to GPS function for fetching properties of project/code."""
    # Create an overlay for an editor:
    b = GPS.EditorBuffer.get(GPS.File("example.adb"))
    o = b.create_overlay("my_overlay_name")
    o.set_property("background", "#ff0000")
    b.apply_overlay(o, GPS.EditorLocation(b, 10, 1), GPS.EditorLocation(b, 10, 10))
#    gps_file = GPS.File('example.adb')
#    old_lines = GPS.Message.list(file=gps_file)
#    for line in old_lines:
#        line.remove()
#    full_cover = GPS.Style("Full covered lines")
#    full_cover.set_background ("#7fff00")    
#    for i in range(5,10):
#        line = GPS.Message("kiasan_highlight", gps_file, i, 1, "message text", 2)
#        line.set_style(full_cover)    
    
#    print "filename:", GPS.current_context().file().name()
#    print "dir:", GPS.current_context().directory()
#    print "entity:", GPS.current_context().entity().name()
#    print "entity category:", GPS.current_context().entity().category()
#    print "entity declaration:", GPS.current_context().entity().declaration()
#    #print "entity body:", GPS.current_context().entity().body()
#    print "entity methods:", GPS.current_context().entity().methods()
#    print "entity primitive_of:", GPS.current_context().entity().primitive_of()
#    print "entity references:", GPS.current_context().entity().references()
#    print "dir(entity)", dir(GPS.current_context().entity())
#    print "project filename:", GPS.current_context().project().file().name()
#    print "root project file/pathname:", GPS.Project.root().file().name()
#    print "source files:", GPS.current_context().project().sources()
#    print "source dirs:", GPS.current_context().project().source_dirs()
#    print "project dir:", os.path.dirname(GPS.current_context().project().file().name())
#    print '\n\nGPS.File(GPS.current_context().file().name()).entities()', GPS.File(GPS.current_context().file().name()).entities()
#    print '\n\nGPS.current_context().file().entities()', GPS.current_context().file().entities()
#    print '\n\nGPS.File(GPS.current_context().file().name()).entities(False)', GPS.File(GPS.current_context().file().name()).entities(False)
#    print '\n\nGPS.current_context().file().entities(False)', GPS.current_context().file().entities(False)


def run_helper2():
#    gps_file = GPS.File('example.adb')
#    old_lines = GPS.Message.list(file=gps_file, category="kiasan_highlight")
#    for line in old_lines:
#        line.remove()
#    full_cover = GPS.Style("Full covered lines")
#    full_cover.set_background ("#7fff00")
#    for i in range(2,3):
#        line = GPS.Message("kiasan_highlight", gps_file, i, 1, "message text", 2)
#        line.set_style(full_cover)
    b = GPS.EditorBuffer.get(GPS.File("example.adb"))
    o = b.create_overlay("my_overlay_name")
    o.set_property("background", "#ff0000")
    b.remove_overlay(o)
    b.apply_overlay(o, GPS.EditorLocation(b, 8, 13), GPS.EditorLocation(b, 8, 17))
    
GPS.parse_xml ("""
    <action name="run Helper">
        <shell lang="python">sireum.run_helper()</shell>
    </action>
    <action name="run Helper2">
        <shell lang="python">sireum.run_helper2()</shell>
    </action>
    <submenu before="Window">
        <title>Sireum</title>
        <menu action="run Kiasan">
            <title>Run Kiasan</title>
        </menu>
        <menu action="run Helper">
            <title>Run Helper</title>
        </menu>
        <menu action="run Helper2">
            <title>Run Helper2</title>
        </menu>                
    </submenu>
""");