Setting up a new homepage
============================

1. Add a ThreeD Object Index object to your publication or inside the Silva root

2. Navigate to the 'properties' tab and then 'settings' and change the skin to 'UCL Theme'

3. Inside this publication add two Silva Folders

4. The first folder must have the id 'menu' & the title 'Explore UCL'

5. The other folder must have the id 'footer', the title isn't important

6. Inside the 'menu' folder you can add a set of Silva Links, one for each of the items in the main left hand navigation. The metadata 'description' is used for the descritpive text that displays beneath each link. 
    These Silva Links must be published to disply within the template and are displayed in the order they appear in the publication

7. Inside the 'footer' folder you must now add three additional Silva Folders, one for each section of links e.g. 'facilities' (with the title 'Facilities'), 'locations' (title 'Locations') & 'connect', (title 'Connect with us').

8. Inside each of these folders you can add Silva Links for each of the footer links to be displayed. To avoid unnecessary duplication you can also add Silva Ghosts of the links contained within the 'menu' folder and these will act in exactly the same way.

9. Now you may start adding your compoenents.

-----------------------------
Creating new content types
============================

Register new component
-------------------------

Open configure.zcml and add the following

e.g:

    <silva:versionedcontent
        extension_name="SilvaUCLPetrieContentTypes"
        content=".TextComponent.TextComponent"
        version=".TextComponent.TextComponentVersion"
        icon="www/document-text.png"
    />

get icon from here http://p.yusukekamiyamane.com/ (Fugue Icons) and save to www folder.
Reference new icon in silva:content icon declaration above.

open install.py:
add the following in the appropriate positions:

    root.manage_permission('Add Text Components', roleinfo.CHIEF_ROLES)

    {'type': 'Text Component Version', 'chain': 'silva-content, silva-extra'},

    news_non_addables = ['ThreeD Object', 'Text Component']

    #register edit view:
    reg.register('edit', 'Text Component', ['edit','VersionedContent','TextComponent'])

    #Register public view
    reg.register('public', 'Text Component Version', ['public','TextComponent','view'])
    reg.register('public', 'Text Component', ['public','TextComponent','view'])

    #Register preview view
    reg.register('preview', 'Text Component Version', ['public','TextComponent','preview'])

    #register add view
    reg.register('add', 'Text Component', ['add', 'TextComponent'])

    # unregister the views:
    for meta_type in ['ThreeD Object', 'Text Component']:

Creating views
------------------

Now add all the views into the views folder by copy/pasting the following folders:

views/add/SilvaUCLComponent & renaming it to TextComponent

views/edit/VersionedContent/SilvaUCLComponent & rename to TextComponent

views/public/SilvaUCLComponent & rename to TextComponent

Create the module
-------------------

Now copy SilvaUCLComponent.py and paste it into the root and rename TextComponent.py

Now open TextComponent.py and edit the following lines:

Add the following import:

    from SilvaUCLComponent import SilvaUCLComponent, SilvaUCLComponentVersion

Delete the following lines:

    from Products.Silva.VersionedContent import CatalogedVersionedContent
    from Products.Silva.Version import CatalogedVersion

from:

    class SilvaUCLComponent(CatalogedVersionedContent):

to:

    class TextComponent(SilvaUCLComponent):

from:

    """ThreeD Object"""

to:

    """Text Component"""

from:

    __doc__ = "A ThreeD Object is a composite element of a ThreeD Object Index"""

to:

    __doc__ = "A Text Component is a composite element of a ThreeD Object Index"""

from:

    meta_type = "ThreeD Object"

to:

    meta_type = "Text Component"

from:

    security.declareProtected(SilvaPermissions.AccessContentsInformation, 'can_set_title')
    def can_set_title(self):
        """always settable"""
        # XXX: we badly need Publishable type objects to behave right.
        return 1

to:
(delete all of this content)

from:

    InitializeClass(SilvaUCLComponent)

to:

    InitializeClass(TextComponent)

from:

    class SilvaUCLComponentVersion(CatalogedVersion):
        """Base class for ThreeD Object Version"""

to:

    class TextComponentVersion(SilvaUCLComponentVersion):
        """Base class for Text Component Version"""

from:

    meta_type = "ThreeD Object Version"

to:

    meta_type = "Text Component Version"

from:

    def __init__(self, id):
        SilvaUCLComponentVersion.inheritedAttribute('__init__')(self, id)
        self._title_url = ''
        self._format = '1'

to:

    def __init__(self, id):
        TextComponentVersion.inheritedAttribute('__init__')(self, id)

and for now we can delete everything (the MANIPULATORS) from this point until we get to:

    InitializeClass(SilvaUCLComponentVersion)

which needs to be changed to:

    InitializeClass(TextComponentVersion)

Now open SilvaUCLHomepage.py and edit the following line:
from:

    _addables_allowed_in_publication = ['ThreeD Object']

to:

    _addables_allowed_in_publication = ['ThreeD Object', 'Text Component']

Modify the add view
---------------------

The next step is to modify the add form to have the submit script:

open /views/add/TextComponent/add_submit_helper.py
modify the following line from:

    model.manage_addProduct['SilvaUCLPetrieContentTypes'].manage_addSilvaUCLComponent(id, title) 

to:

    model.manage_addProduct['SilvaUCLPetrieContentTypes'].manage_addTextComponent(id, title) 

Restart Zope to test
---------------------

We can probably do a restart of zope here just to check it all installs correctly, the views are registered and metadata sets propoery configured.

Navigate to service_extensions in the ZMI and refresh your the Silva UCL Petrie Content Types extension.

Now navigate to the service_view_registry and check the views are all registered for the new component.

Now navigate to the service_metadata and check the metadata is registered for the new component version (only).

Now open the SMI and see if you can add a Text Component into a ThreeD Object Index if you can we're good to go and we can concentrate on the edit and public views:

Modify the edit view
---------------------

open views/edit/VersionedContent/TextComponent/form.form

you will see a <fields> containing three <field> tags (object_title, title_url & format) We're now going to add some additional fields to supplement these.

To do this go into your ZMI, anywhere. And add a 'Formulator Form', give it a title and id...not important.
Into this you can add fields, there a bunch of different types.
For the TextComponent it appears we need two paragraphs of text and a link. So I'll add two TextAreaFields and a StringField (for the url)

Id, Title
* 'p1', '1st Paragraph'
* 'p2', '2nd Paragraph'
* 'link_url', 'Link' *
(* not required.)

When adding the link_url, since it's not required, click 'add and edit' and uncheck the box next to where it says 'Required'

Now you've made your fields, we have to add them into form.form. Go to the XML tab in the Formulator Form you've just made and copy everything from between the <fields></fields> tag and paste it into the form.form file, below the last <field> (format).

You can now delete your Formulator Form in the ZMI if you want.

Try restarting Zope and adding a Text Component via the SMI, you should see your new form.

If you want to add some descriptions to your fields you can do so in form.form by adding them to the <description> tag for each field.

Getter and Setters
-------------------

Now we need to add a setter/getter for each of these new fields...if you look at the original ones, particularly the label_url you'll see theres an additional section like so:

    <tales>
        <default>python:request.model.get_editable().get_label_url()</default>
    </tales>
    
we need to add something like this for each field:
eg:

    <tales>
        <default>python:request.model.get_editable().get_p1()</default>
    </tales>

or:

    <tales>
        <default>python:request.model.get_editable().get_link_url()</default>
    </tales>

so add it in.

You can restart zope now and have a look what this does by editing an existsing Text Component.

Yes, thats right, yoiu've got an AttributeError, something like Error Value:get_p1....Why?

Because you need to add the MANIPULATORS to your TextComponent class. These allow the values of p1,p2, and link_url to be set as attributes on the Text Component object.

So now open up TextComponent.py:

First you must add default values, if there are any, to the attributes when the object is initialised. To do this add the following lines to the __init__ method e.g:

    def __init__(self, id):
        TextComponentVersion.inheritedAttribute('__init__')(self, id)
        self.label = 'My Label' # if you want to set a default label value do so here
        self._p1 = ''
        self._p2 = ''
        self._link_url = ''

This just sets all of the values to be empty strings to begin with.

Next you must add a getter and a setter of each of the attributes eg.:

    security.declareProtected(SilvaPermissions.AccessContentsInformation,
                                   'get_link_url')
    def get_link_url(self):
       """Get the link_url of the component."""
       if not hasattr(self, '_link_url'):
            self._link_url = ''
       else:
            return self._link_url

    security.declareProtected(SilvaPermissions.ChangeSilvaContent,
                                    'set_link_url')
    def set_link_url(self, link_url):
        """Sets the link_url of the component."""
        self._link_url = link_url

Ok, you can restart zope now and have a look what this does by editing an existsing Text Component.

Ok edit form appears to work now, we can view it at least. But wait!! What happens when we try to enter some text in one of the new fields and save it? Uh ohhh nothing...Component Changed, but refresh the page and the values disappear!!!

So why's this?

It's because the values from the form aren't passed to the object when we click save. To rectify this we need to now open views\edit\VersionedContent\TextComponent\submit.py

If you look at this script, we're only setting the title, the title_url and the format values our new fields aren't being saved. So we need to add some calls to the set_<whatever> MANIPULATOR methods we just added to TextComponent.py eg:

    p1 = result['p1']
    editable.set_p1(p1)

    p2 = result['p2']
    editable.set_p2(p2)

    link_url = result['link_url']
    editable.set_link_url(link_url)

Ok, now lets try saving some values in the edit view...Restart zope again! Woo Hoo!! Now we have a new object onto which we can save a bunch of attributes.

Modify a public view
---------------------

Next, the public views:
Open the file views\public\TextComponent\render_helper.pt

And modify accordingly using basic tal and tales for ZPT:

e.g:

    <tal:comp
        xmlns:metal="http://xml.zope.org/namespaces/metal"
        xmlns:tal="http://xml.zope.org/namespaces/tal"
        xmlns:i18n="http://xml.zope.org/namespaces/i18n"
        i18n:domain="silva_news"
        tal:define="
        global model request/model; 
        global view here; 
        global version options/version;">
        <p class="meta top">
            <a tal:attributes="href python:version.get_title_url()" tal:content="structure python:version.get_title()" class="flag">Title</a>
        </p>
        <p>format: <tal:format replace="python:version.get_format()" /></p>
        <p tal:define="p1 python:version.get_p1()" tal:condition="p1" tal:content="p1">p1</p>
        <p tal:define="p2 python:version.get_p2()" tal:condition="p2" tal:content="p2">p2</p>
        <a tal:define="link python:version.get_link_url()" tal:condition="link" tal:attributes="href link">Link URL</a>
    </tal:comp>

