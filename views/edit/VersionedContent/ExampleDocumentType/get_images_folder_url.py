## Script (Python) "get_images_folder_url"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##


# This script is called (if required) by views > edit > VersionedContent > ExampleDocumentType > kupusilvatools.js.dtml line 3070
# I can't work out how to get from the service_views object to the actual content object via the dtml call
# in kupusilvatools.js.dtml. I've tried content_url() and get_content(), but neither works so
# just return the url of the silva root for now

return context.get_root_url()

# Below is a quick fix to work for Petrie. It needs to be made generic
# I'll do that at some point, but can't at the moment, cos I'm not clever enough
catalog = context.service_catalog
publications = catalog.searchResults({'meta_type':'Silva Publication','id':'3dpetriemuseum'})
myroot = publications and publications[0].getObject() or None
if myroot:
    items = myroot.get_container_tree(1)
    for item in items:
        thing = item[1]
        if thing.meta_type == 'ThreeD Object Index':
            subitems = thing.get_container_tree(1)
            for sitem in subitems:
                sthing = sitem[1]
                if sthing.meta_type == 'Silva Folder' and  sthing.getId() == 'images':
                    return sthing.absolute_url()
            return thing.absolute_url()
else:
    threedindexes = catalog.searchResults({'meta_type':'ThreeD Object Index'})
    if threedindexes:
        tdi = threedindexes[0].getObject()
        subitems = tdi.get_container_tree(1)
        for sitem in subitems:
            sthing = sitem[1]
            if sthing.meta_type == 'Silva Folder' and  sthing.getId() == 'images':
                return sthing.absolute_url()
        return tdi.absolute_url()
return context.get_root().absolute_url()