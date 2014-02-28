# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393624836.583627
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = u'tag.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        tag = context.get('tag', UNDEFINED)
        len = context.get('len', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 11
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 32
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n        <!--Body content-->\n        <div class="postbox">\n        <h1>')
        # SOURCE LINE 16
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        # SOURCE LINE 17
        if len(translations) > 1:
            # SOURCE LINE 18
            for language in translations:
                # SOURCE LINE 19
                __M_writer(u'                <a href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">RSS (')
                __M_writer(unicode(language))
                __M_writer(u')</a>&nbsp;\n')
            # SOURCE LINE 21
        else:
            # SOURCE LINE 22
            __M_writer(u'            <a href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">RSS</a>\n')
        # SOURCE LINE 24
        __M_writer(u'        <br>\n        <ul class="unstyled">\n')
        # SOURCE LINE 26
        for post in posts:
            # SOURCE LINE 27
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">[')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'] ')
            __M_writer(unicode(post.title()))
            __M_writer(u'</a>\n')
        # SOURCE LINE 29
        __M_writer(u'        </ul>\n        </div>\n        <!--End of body content-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        kind = context.get('kind', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        if len(translations) > 1:
            # SOURCE LINE 5
            for language in translations:
                # SOURCE LINE 6
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(unicode(kind))
                __M_writer(u' ')
                __M_writer(unicode(tag))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">\n')
            # SOURCE LINE 8
        else:
            # SOURCE LINE 9
            __M_writer(u'        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(unicode(kind))
            __M_writer(u' ')
            __M_writer(unicode(tag))
            __M_writer(u'" href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


