# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1393624836.439821
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/annotation_helper.tmpl'
_template_uri = u'annotation_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['code', 'css']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_code(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    <script src="http://code.jquery.com/jquery-migrate-1.2.1.js"></script>\n    <script src="http://assets.annotateit.org/annotator/v1.2.7/annotator-full.js"></script>\n    <script>\n    jQuery(function ($) {\n        $(\'body\').annotator().annotator(\'setupPlugins\', {}, {\n            // Disable filter bar\n            Filter: false\n        });\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <link rel="stylesheet" href="http://assets.annotateit.org/annotator/v1.2.5/annotator.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


