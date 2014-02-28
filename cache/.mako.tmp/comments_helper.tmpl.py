# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393624836.468293
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = u'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 7
    ns = runtime.TemplateNamespace(u'googleplus', context._clean_inheritance_tokens(), templateuri=u'googleplus_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'googleplus')] = ns

    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'livefyre', context._clean_inheritance_tokens(), templateuri=u'livefyre_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'livefyre')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'disqus', context._clean_inheritance_tokens(), templateuri=u'disqus_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'disqus')] = ns

    # SOURCE LINE 5
    ns = runtime.TemplateNamespace(u'intensedebate', context._clean_inheritance_tokens(), templateuri=u'intensedebate_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'intensedebate')] = ns

    # SOURCE LINE 6
    ns = runtime.TemplateNamespace(u'moot', context._clean_inheritance_tokens(), templateuri=u'moot_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'moot')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 21
        __M_writer(u'\n\n')
        # SOURCE LINE 35
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        moot = _mako_get_namespace(context, 'moot')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n')
        # SOURCE LINE 10
        if comment_system == 'disqus':
            # SOURCE LINE 11
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_form(url, title, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 12
        elif comment_system == 'livefyre':
            # SOURCE LINE 13
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_form(url, title, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 14
        elif comment_system == 'intensedebate':
            # SOURCE LINE 15
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_form(url, title, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 16
        elif comment_system == 'moot':
            # SOURCE LINE 17
            __M_writer(u'        ')
            __M_writer(unicode(moot.comment_form(url, title, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 18
        elif comment_system == 'googleplus':
            # SOURCE LINE 19
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        moot = _mako_get_namespace(context, 'moot')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        if comment_system == 'disqus':
            # SOURCE LINE 25
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_link(link, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 26
        elif comment_system == 'livefyre':
            # SOURCE LINE 27
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_link(link, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 28
        elif comment_system == 'intensedebate':
            # SOURCE LINE 29
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_link(link, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 30
        elif comment_system == 'moot':
            # SOURCE LINE 31
            __M_writer(u'        ')
            __M_writer(unicode(moot.comment_link(link, identifier)))
            __M_writer(u'\n')
            # SOURCE LINE 32
        elif comment_system == 'googleplus':
            # SOURCE LINE 33
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_link(link, identifier)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        moot = _mako_get_namespace(context, 'moot')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n')
        # SOURCE LINE 38
        if comment_system == 'disqus':
            # SOURCE LINE 39
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_link_script()))
            __M_writer(u'\n')
            # SOURCE LINE 40
        elif comment_system == 'livefyre':
            # SOURCE LINE 41
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_link_script()))
            __M_writer(u'\n')
            # SOURCE LINE 42
        elif comment_system == 'intensedebate':
            # SOURCE LINE 43
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_link_script()))
            __M_writer(u'\n')
            # SOURCE LINE 44
        elif comment_system == 'moot':
            # SOURCE LINE 45
            __M_writer(u'        ')
            __M_writer(unicode(moot.comment_link_script()))
            __M_writer(u'\n')
            # SOURCE LINE 46
        elif comment_system == 'googleplus':
            # SOURCE LINE 47
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_link_script()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


