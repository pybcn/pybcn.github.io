# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.602229
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/story.tmpl'
_template_uri = u'story.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 4
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        title = context.get('title', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 7
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 16
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 9
        if title and not post.meta('hidetitle'):
            # SOURCE LINE 10
            __M_writer(u'    <h1>')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        # SOURCE LINE 12
        __M_writer(u'    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n')
        # SOURCE LINE 13
        if enable_comments and not post.meta('nocomments'):
            # SOURCE LINE 14
            __M_writer(u'    ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


