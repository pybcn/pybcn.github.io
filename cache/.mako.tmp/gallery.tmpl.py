# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.650692
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap/templates/gallery.tmpl'
_template_uri = u'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'sourcelink', u'extra_js', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'ui', context._clean_inheritance_tokens(), templateuri=u'crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'ui')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        text = _import_ns.get('text', context.get('text', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 5
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 32
        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 44
        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        # SOURCE LINE 86
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        text = _import_ns.get('text', context.get('text', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(ui.bar(crumbs)))
        __M_writer(u'\n')
        # SOURCE LINE 9
        if text:
            # SOURCE LINE 10
            __M_writer(u'    <p>\n        ')
            # SOURCE LINE 11
            __M_writer(unicode(text))
            __M_writer(u'\n    </p>\n')
        # SOURCE LINE 14
        __M_writer(u'    <ul>\n')
        # SOURCE LINE 15
        for folder in folders:
            # SOURCE LINE 16
            __M_writer(u'        <li><a href="')
            __M_writer(unicode(folder))
            __M_writer(u'"><i class="icon-folder-open"></i>&nbsp;')
            __M_writer(unicode(folder))
            __M_writer(u'</a></li>\n')
        # SOURCE LINE 18
        __M_writer(u'    </ul>\n\n    <div id="gallery_container"></div>\n    <noscript>\n    <ul class="thumbnails">\n')
        # SOURCE LINE 23
        for image in photo_array:
            # SOURCE LINE 24
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(image['url']))
            __M_writer(u'" class="thumbnail image-reference" title="')
            __M_writer(unicode(image['title']))
            __M_writer(u'">\n                <img src="')
            # SOURCE LINE 25
            __M_writer(unicode(image['url_thumb']))
            __M_writer(u'" alt="')
            __M_writer(unicode(image['title']))
            __M_writer(u'" /></a>\n')
        # SOURCE LINE 27
        __M_writer(u'    </ul>\n    </noscript>\n')
        # SOURCE LINE 29
        if enable_comments:
            # SOURCE LINE 30
            __M_writer(u'    ')
            __M_writer(unicode(comments.comment_form(None, permalink, title)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def extra_js():
            return render_extra_js(context)
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n<script src="/assets/js/flowr.plugin.js"></script>\n<script>\njsonContent = ')
        # SOURCE LINE 50
        __M_writer(unicode(photo_array_json))
        __M_writer(u';\n$("#gallery_container").flowr({\n        data : jsonContent,\n        height : ')
        # SOURCE LINE 53
        __M_writer(unicode(thumbnail_size))
        __M_writer(u'*.6,\n        padding: 5,\n        rows: -1,\n        render : function(params) {\n            // Just return a div, string or a dom object, anything works fine\n            img = $("<img />").attr({\n                \'src\': params.itemData.url_thumb,\n                \'width\' : params.width,\n                \'height\' : params.height\n            }).css(\'max-width\', \'100%\');\n            link = $( "<a></a>").attr({\n                \'href\': params.itemData.url,\n                \'class\': \'image-reference\'\n            });\n            div = $("<div />").addClass(\'image-block\').attr({\n                \'title\': params.itemData.title,\n                \'data-toggle\': "tooltip",\n            });\n            link.append(img);\n            div.append(link);\n            div.hover(div.tooltip());\n            return div;\n        },\n        itemWidth : function(data) { return data.size.w; },\n        itemHeight : function(data) { return data.size.h; },\n        complete : function(params) {\n            if( jsonContent.length > params.renderedItems ) {\n                nextRenderList = jsonContent.slice( params.renderedItems );\n            }\n        }\n    });\n$("a.image-reference").colorbox({rel:"gal", maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n<style type="text/css">\n    .image-block {\n        display: inline-block;\n    }\n    .flowr_row {\n        width: 100%;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


