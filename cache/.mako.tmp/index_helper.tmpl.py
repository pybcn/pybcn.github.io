# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.469495
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/index_helper.tmpl'
_template_uri = u'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n')
        # SOURCE LINE 20
        if any(post.is_mathjax for post in posts):
            # SOURCE LINE 21
            __M_writer(u'        <script src="/assets/js/mathjax.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<div>\n<ul class="pager">\n')
        # SOURCE LINE 5
        if prevlink:
            # SOURCE LINE 6
            __M_writer(u'    <li class="previous">\n        <a href="')
            # SOURCE LINE 7
            __M_writer(unicode(prevlink))
            __M_writer(u'" rel="prev">&larr; ')
            __M_writer(unicode(messages("Newer posts")))
            __M_writer(u'</a>\n    </li>\n')
        # SOURCE LINE 10
        if nextlink:
            # SOURCE LINE 11
            __M_writer(u'    <li class="next">\n        <a href="')
            # SOURCE LINE 12
            __M_writer(unicode(nextlink))
            __M_writer(u'" rel="next">')
            __M_writer(unicode(messages("Older posts")))
            __M_writer(u' &rarr;</a>\n    </li>\n')
        # SOURCE LINE 15
        __M_writer(u'</ul>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


