from Products.Silva.mangle import String

if not context.check_editable():
    return context.redirect()

node = context.REQUEST.node
doc = node.ownerDocument
for row in node.childNodes:
    if row.nodeName != 'row':
        continue
    # add field
    field = doc.createElement('field')
    p = doc.createElement('p')
    p.appendChild(doc.createTextNode(''))
    field.appendChild(p)

    row.appendChild(field)

node.setAttribute(
    'columns', 
    String.inputConvert(str(int(node.getAttribute('columns')) + 1)) )

if node.hasAttribute('column_info'):
    node.setAttribute('column_info', node.getAttribute('column_info') + u' L:1')

# invalidate cache
#for mode in ['mode_normal', 'mode_edit', 'mode_insert', 'mode_done']:
#    context.service_editor.invalidateCache(node,
#       ('service_document_editor_widgets', 'element', 'table', mode))

return context.redirect()
