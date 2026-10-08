{{- $logo := resources.Get "images/logo.png" -}}
{{- $logo = partial "image_resize.html" (dict "img" $logo "width" 400) -}}
<?xml version="1.0" encoding="utf-8"?>
<!--
  Renders /sitemap.xml as a readable page when a person opens it in a browser.
  Search engines ignore this stylesheet and read the XML directly.
  XSLT 1.0 only: that is what browsers implement.
  Pairs with rss.xsl: same heading shape, same intro, same CSS, same date form.
-->
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9"
  exclude-result-prefixes="s">

  <xsl:output method="html" encoding="utf-8" indent="yes" doctype-system="about:legacy-compat"/>

  <xsl:variable name="heading">PyBCN sitemap</xsl:variable>
  <xsl:variable name="count" select="count(s:urlset/s:url)"/>

  <!-- W3C datetime, 2026-10-05T18:27:40+02:00, shown as 2026-10-05 18:27 +02:00. -->
  <xsl:template name="when">
    <xsl:param name="stamp"/>
    <xsl:if test="string-length($stamp) >= 25">
      <xsl:value-of select="concat(substring($stamp, 1, 10), ' ', substring($stamp, 12, 5), ' ', substring($stamp, 20, 6))"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta name="robots" content="noindex"/>
        <title><xsl:value-of select="$heading"/></title>
        <link rel="icon" href="/favicon.ico" sizes="any"/>
        <style>
          body { margin: 0; color: #343a40; background: #fff;
                 font-family: Helvetica, Roboto, "Segoe UI", Calibri, sans-serif; }
          h1 { margin: 0; padding: 0; font-weight: normal; font-size: 2rem; }
          header { padding: 28px 0 24px; text-align: center; background: #fff;
                   border-bottom: 1px solid #dee2e6; margin-bottom: 1.5rem; }
          header a { display: inline-block; color: #006c9b; text-decoration: none; }
          header img { display: block; height: 58px; width: auto; margin: 0 auto 14px; }
          header a:hover h1, header a:focus h1 { text-decoration: underline; }
          main { max-width: 72rem; margin: 0 auto; padding: 0 1rem 2rem; }
          p { margin: 0 0 1rem; }
          a { color: #006c9b; }
          table { width: 100%; border-collapse: collapse; font-size: 0.95rem; }
          th, td { padding: 0.4rem 0.6rem; text-align: left; vertical-align: top;
                   border-bottom: 1px solid #dee2e6; }
          th { background: #f1f5f8; font-weight: 600; }
          .n { width: 2.5rem; color: #6c757d; text-align: right; white-space: nowrap; }
          .when { width: 12rem; white-space: nowrap; font-variant-numeric: tabular-nums; }
          td.loc { word-break: break-all; }
          tbody tr:hover { background: #f1f5f8; }
        </style>
      </head>
      <body>
        <header>
          <a href="{{ site.Home.Permalink }}">
            <img src="{{ $logo.RelPermalink }}" width="{{ $logo.Width }}" height="{{ $logo.Height }}" alt="Python Barcelona"/>
            <h1><xsl:value-of select="$heading"/></h1>
          </a>
        </header>
        <main>
          <p>
            <xsl:value-of select="$count"/>
            <xsl:choose>
              <xsl:when test="$count = 1"> URL</xsl:when>
              <xsl:otherwise> URLs</xsl:otherwise>
            </xsl:choose>, most recently changed first.
            Search engines read the XML behind this page; a browser shows it as a table.
          </p>
          <table>
            <thead>
              <tr>
                <th class="n">#</th>
                <th>URL</th>
                <th class="when">Last modified</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="s:urlset/s:url">
                <xsl:sort select="s:lastmod" order="descending"/>
                <tr>
                  <td class="n"><xsl:value-of select="position()"/></td>
                  <td class="loc">
                    <a href="{s:loc}"><xsl:value-of select="s:loc"/></a>
                  </td>
                  <td class="when">
                    <xsl:call-template name="when">
                      <xsl:with-param name="stamp" select="s:lastmod"/>
                    </xsl:call-template>
                  </td>
                </tr>
              </xsl:for-each>
            </tbody>
          </table>
        </main>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
