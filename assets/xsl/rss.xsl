{{- $logo := resources.Get "images/logo.png" -}}
{{- $logo = partial "image_resize.html" (dict "img" $logo "width" 400) -}}
<?xml version="1.0" encoding="utf-8"?>
<!--
  Renders an RSS feed as a readable page when a person opens it in a browser.
  A feed reader ignores this stylesheet and reads the XML directly.
  XSLT 1.0 only: that is what browsers implement.
  Pairs with sitemap.xsl: same heading shape, same intro, same CSS, same date form.
  Serves /index.xml, the only feed of the site. A section feed, if one is ever
  built again, gets its section name in the heading.
-->
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="utf-8" indent="yes" doctype-system="about:legacy-compat"/>

  <!--
    Hugo titles a section feed "Events on PyBCN - The Barcelona Python
    Association" and the home feed "Welcome to PyBCN on PyBCN - ...". The
    heading keeps the part before " on " for a section and nothing for the
    home feed, which is the one whose link has no path after the host.
  -->
  <xsl:variable name="section" select="substring-before(rss/channel/title, ' on ')"/>
  <xsl:variable name="path" select="substring-after(substring-after(rss/channel/link, '//'), '/')"/>
  <xsl:variable name="heading">
    <xsl:text>PyBCN feed</xsl:text>
    <xsl:if test="$path != '' and $section != ''">
      <xsl:value-of select="concat(': ', $section)"/>
    </xsl:if>
  </xsl:variable>
  <xsl:variable name="count" select="count(rss/channel/item)"/>

  <!-- RFC 822, Sun, 04 Oct 2026 10:09:00 +0200, shown as 2026-10-04 10:09 +02:00. -->
  <xsl:template name="when">
    <xsl:param name="stamp"/>
    <xsl:if test="string-length($stamp) >= 31">
      <xsl:value-of select="substring($stamp, 13, 4)"/>
      <xsl:text>-</xsl:text>
      <xsl:choose>
        <xsl:when test="substring($stamp, 9, 3) = 'Jan'">01</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Feb'">02</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Mar'">03</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Apr'">04</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'May'">05</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Jun'">06</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Jul'">07</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Aug'">08</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Sep'">09</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Oct'">10</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Nov'">11</xsl:when>
        <xsl:when test="substring($stamp, 9, 3) = 'Dec'">12</xsl:when>
        <xsl:otherwise>??</xsl:otherwise>
      </xsl:choose>
      <xsl:value-of select="concat('-', substring($stamp, 6, 2), ' ', substring($stamp, 18, 5), ' ', substring($stamp, 27, 3), ':', substring($stamp, 30, 2))"/>
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
              <xsl:when test="$count = 1"> entry</xsl:when>
              <xsl:otherwise> entries</xsl:otherwise>
            </xsl:choose>, most recently changed first.
            Feed readers read the XML behind this page; a browser shows it as a table.
            The feed covers <a href="{rss/channel/link}"><xsl:value-of select="rss/channel/link"/></a>.
          </p>
          <table>
            <thead>
              <tr>
                <th class="n">#</th>
                <th>Title</th>
                <th class="when">Published</th>
              </tr>
            </thead>
            <tbody>
              <xsl:for-each select="rss/channel/item">
                <tr>
                  <td class="n"><xsl:value-of select="position()"/></td>
                  <td>
                    <!-- An item with no title shows its link, so the row has text to read and click. -->
                    <a href="{link}">
                      <xsl:choose>
                        <xsl:when test="normalize-space(title) != ''"><xsl:value-of select="title"/></xsl:when>
                        <xsl:otherwise><xsl:value-of select="link"/></xsl:otherwise>
                      </xsl:choose>
                    </a>
                  </td>
                  <td class="when">
                    <xsl:call-template name="when">
                      <xsl:with-param name="stamp" select="pubDate"/>
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
