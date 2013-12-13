# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386959225.577548
_enable_loop = True
_template_filename = u'/home/areski/.virtualenvs/pybcn/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/bootstrap_helper.tmpl'
_template_uri = u'bootstrap_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['html_navigation_links', 'html_head', 'late_load_js']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 74
        __M_writer(u'\n\n\n')
        # SOURCE LINE 98
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n')
        # SOURCE LINE 78
        for url, text in navigation_links[lang]:
            # SOURCE LINE 79
            if isinstance(url, tuple):
                # SOURCE LINE 80
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">')
                __M_writer(unicode(text))
                __M_writer(u'<b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                # SOURCE LINE 82
                for suburl, text in url:
                    # SOURCE LINE 83
                    if rel_link(permalink, suburl) == "#":
                        # SOURCE LINE 84
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                        # SOURCE LINE 85
                    else:
                        # SOURCE LINE 86
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                # SOURCE LINE 89
                __M_writer(u'            </ul>\n')
                # SOURCE LINE 90
            else:
                # SOURCE LINE 91
                if rel_link(permalink, url) == "#":
                    # SOURCE LINE 92
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 93
                else:
                    # SOURCE LINE 94
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        blog_author = context.get('blog_author', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        # SOURCE LINE 7
        if description:
            # SOURCE LINE 8
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        # SOURCE LINE 10
        __M_writer(u'    <meta name="author" content="')
        __M_writer(unicode(blog_author))
        __M_writer(u'">\n    <title>')
        # SOURCE LINE 11
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 12
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        # SOURCE LINE 13
        if use_bundles:
            # SOURCE LINE 14
            if use_cdn:
                # SOURCE LINE 15
                __M_writer(u'            <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
                # SOURCE LINE 17
            else:
                # SOURCE LINE 18
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 20
        else:
            # SOURCE LINE 21
            if use_cdn:
                # SOURCE LINE 22
                __M_writer(u'            <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">\n')
                # SOURCE LINE 23
            else:
                # SOURCE LINE 24
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 26
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css"/>\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css"/>\n')
            # SOURCE LINE 30
            if has_custom_css:
                # SOURCE LINE 31
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        # SOURCE LINE 34
        __M_writer(u'    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>\n    <![endif]-->\n')
        # SOURCE LINE 37
        if rss_link:
            # SOURCE LINE 38
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            if len(translations) > 1:
                # SOURCE LINE 41
                for language in translations:
                    # SOURCE LINE 42
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
                # SOURCE LINE 44
            else:
                # SOURCE LINE 45
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        # SOURCE LINE 48
        if favicons:
            # SOURCE LINE 49
            for name, file, size in favicons:
                # SOURCE LINE 50
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 56
        if use_bundles:
            # SOURCE LINE 57
            if use_cdn:
                # SOURCE LINE 58
                __M_writer(u'            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>\n            <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js" type="text/javascript"></script>\n')
                # SOURCE LINE 61
            else:
                # SOURCE LINE 62
                __M_writer(u'            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
            # SOURCE LINE 64
        else:
            # SOURCE LINE 65
            if use_cdn:
                # SOURCE LINE 66
                __M_writer(u'            <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>\n            <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>\n')
                # SOURCE LINE 68
            else:
                # SOURCE LINE 69
                __M_writer(u'            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/bootstrap.min.js" type="text/javascript"></script>\n')
            # SOURCE LINE 72
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


