# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.521044
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/googleplus_helper.tmpl'
_template_uri = u'googleplus_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n\n')
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<script src="https://apis.google.com/js/plusone.js"></script>\n<div class="g-comments"\n    data-href="')
        # SOURCE LINE 5
        __M_writer(unicode(url))
        __M_writer(u'"\n    data-first_party_property="BLOGGER"\n    data-view_type="FILTERED_POSTMOD">\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n<div class="g-commentcount" data-href="')
        # SOURCE LINE 12
        __M_writer(unicode(link))
        __M_writer(u'"></div>\n<script src="https://apis.google.com/js/plusone.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


