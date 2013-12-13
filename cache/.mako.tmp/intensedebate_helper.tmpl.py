# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.511523
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/intensedebate_helper.tmpl'
_template_uri = u'intensedebate_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u"\n<script>\nvar idcomments_acct = '")
        # SOURCE LINE 4
        __M_writer(unicode(comment_system_id))
        __M_writer(u'\';\nvar idcomments_post_id = "')
        # SOURCE LINE 5
        __M_writer(unicode(identifier))
        __M_writer(u'";\nvar idcomments_post_url = "')
        # SOURCE LINE 6
        __M_writer(unicode(url))
        __M_writer(u'";\n</script>\n<span id="IDCommentsPostTitle" style="display:none"></span>\n<script type=\'text/javascript\' src=\'http://www.intensedebate.com/js/genericCommentWrapperV2.js\'></script>\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n<a href="{link}" onclick="this.href=\'')
        # SOURCE LINE 14
        __M_writer(unicode(link))
        __M_writer(u'\'; this.target=\'_self\';"><span class=\'IDCommentsReplace\' style=\'display:none\'>')
        __M_writer(unicode(identifier))
        __M_writer(u"</span>\n<script>\nvar idcomments_acct = '")
        # SOURCE LINE 16
        __M_writer(unicode(comment_system_id))
        __M_writer(u'\';\nvar idcomments_post_id = "')
        # SOURCE LINE 17
        __M_writer(unicode(identifier))
        __M_writer(u'";\nvar idcomments_post_url = "')
        # SOURCE LINE 18
        __M_writer(unicode(link))
        __M_writer(u'";\n</script>\n<script type="text/javascript" src="http://www.intensedebate.com/js/genericLinkWrapperV2.js"></script>\n</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


