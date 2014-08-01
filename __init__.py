# Copyright (c) 2014 UCL. All rights reserved.

from Products.Silva.ImporterRegistry import importer_registry
from Products.SilvaDocument import EditorSupportNested
from Products.SilvaDocument import ServiceCodeSourceCharset
import install

from Products.Silva.fssite import registerDirectory
from Products.Silva.helpers import makeContainerFilter

def initialize(context):
    
#    context.registerClass(
#        EditorSupportNested.EditorSupport,
#        constructors = (EditorSupportNested.manage_addEditorSupport, ),
#        icon = "www/editorservice.gif",
#        container_filter = makeContainerFilter()
#        )
    
#    context.registerClass(
#        ServiceCodeSourceCharset.CodeSourceCharsetService,
#        constructors = (ServiceCodeSourceCharset.manage_addCodeSourceCharsetServiceForm, 
#                        ServiceCodeSourceCharset.manage_addCodeSourceCharsetService),
#        icon = "www/editorservice.gif",
#        container_filter = makeContainerFilter()
#        )

    registerDirectory('widgets', globals())


