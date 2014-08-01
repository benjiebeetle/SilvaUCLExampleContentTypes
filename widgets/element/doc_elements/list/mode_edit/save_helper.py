from Products.Silva.mangle import String

request = context.REQUEST
node = request.node
model = node.get_content()
editorsupport = context.service_editorsupport

if request['what'] != 'list':
    context.element_switch()
    return

# strip off trailing whitespace, so empty lines do not lead to empty listitems
data = request['data']
data = data.rstrip()

if not request.has_key('element_type'):
    element_type = 'disc'
else:
    element_type = request['element_type']

if element_type not in ['circle', 'square', 'disc', 
                        '1', 'A', 'a', 'I', 'i', 'none']:
    return

node.setAttribute('type', String.inputConvert(element_type))

# remove previous items, except for the title node
childNodes = [ child for child in  node.childNodes if child.nodeName=='li' ]
childNodes.reverse()
for child in childNodes:
    node.removeChild(child)

# now add new items
doc = node.ownerDocument

lines = data.split('\r\n')
lines = [ line.strip() for line in lines ]
data = '\r\n'.join(lines)
items = data.split('\r\n\r\n')
for item in items:
    item = item.strip()
    if not item:
        continue
    li = doc.createElement('li')
    node.appendChild(li)
    supp = editorsupport.getMixedContentSupport(model, li)
    supp.parse(item)
