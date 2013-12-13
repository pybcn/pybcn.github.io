# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.611298
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 10
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 28
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        # SOURCE LINE 36
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n    <div class="postbox">\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(helper.html_title()))
        __M_writer(u'\n    <hr>\n    <small>\n        ')
        # SOURCE LINE 16
        __M_writer(unicode(messages("Posted")))
        __M_writer(u': <time class="published" datetime="')
        __M_writer(unicode(post.date.isoformat()))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time>\n        ')
        # SOURCE LINE 17
        __M_writer(unicode(helper.html_translations(post)))
        __M_writer(u'\n        ')
        # SOURCE LINE 18
        __M_writer(unicode(helper.html_tags(post)))
        __M_writer(u'\n    </small>\n    <hr>\n    ')
        # SOURCE LINE 21
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    ')
        # SOURCE LINE 22
        __M_writer(unicode(helper.html_pager(post)))
        __M_writer(u'\n')
        # SOURCE LINE 23
        if not post.meta('nocomments'):
            # SOURCE LINE 24
            __M_writer(u'        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'    ')
        __M_writer(unicode(helper.mathjax_script(post)))
        __M_writer(u'\n    </div>\n')
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
        # SOURCE LINE 7
        if post.meta('keywords'):
            # SOURCE LINE 8
            __M_writer(u'    <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 31
        if not post.meta('password'):
            # SOURCE LINE 32
            __M_writer(u'    <li>\n    <a href="')
            # SOURCE LINE 33
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


