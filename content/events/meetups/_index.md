---
title: "Monthly meetups"
description: ""
# No menu entry, and no year. This page is the index of the section, so it
# holds no event of its own and takes no row on /events/, which is the rule
# events_index.html already applies to the other four _index.md files of the
# section. It is also kept out of the main menu on purpose: Events already
# carries Monthly Events, and two entries about the same thing is a question
# for whoever decides what that page becomes.
#
# 266 of the 268 files beside this one come from the Meetup export, through
# bin/import-meetups. The other two are the call for papers mentoring
# sessions, which that import skips with the large editions and which were
# written by hand. The export is the only record left: the Meetup REST
# API that served these events is retired and answers 404, which is why
# partials/meetup-events.html is a link to Meetup and not a list.
#
# What each file carries, and what it does not. The title, the day, the
# venue, the RSVPs, the source URL, and the group are copies of one
# field each, so they are as good as the export. The Meetup description is
# not published: it is the door policy, "only register if you can attend",
# the call for proposals, and a social media footer, and an archive records
# what happened and not how to sign up for something that is over. The talks
# that description announces are the part worth keeping, and they are
# extracted separately, read against the source by bin/check-extraction.
#
# The video of a talk does not come from the announcement, which was written
# before the day. It comes from the YouTube channel, through
# bin/import-videos, which adds a link of type video to a talk record that
# bin/import-talks already wrote. The order of the two matters: a second run
# of bin/import-talks writes the talks block again from the extraction, and
# the extraction holds no video, so the links of the videos have to be
# imported after it and not before. A recording of a whole session, a
# block of lightning talks or the introduction of the evening, is not the
# video of a talk: bin/import-videos writes it as an entry of an
# event-level session_videos block, title and url, and the page prints it
# under a Recordings heading after the talks. Not "videos": Hugo reads that
# key as the og:video URLs of the page.
#
# Every page of this section takes layouts/_default/meetup.html, which is
# what prints those fields: a file of the section carries no body, so the
# default single layout gave it a title and an empty page. The
# layout is set here and not in each file, because it is the same for all
# 268 of them and a cascade cannot drift from them the way 268 copies of
# one line can. content/events/monthly_events.md names its own layout the
# same way, in its own front matter, because it is one page.
#
# A cascade and not a layouts/events/single.html: Hugo resolves the layout
# of a page in a nested section from its top level section, which is
# events, so that file would also take the 13 larger editions off
# layouts/_default/event.html.
#
# _target keeps the cascade off this page. A cascade reaches the node that
# declares it as well as its descendants, so a bare "layout: meetup" put
# this index on the meetup layout too: the paragraph below rendered inside
# a meetup page with no date and no facts, and the list of the 268 links
# that layouts/_default/list.html draws was gone.
cascade:
  - layout: meetup
    _target:
      kind: page

# attendance is the yesCount of the Meetup RSVPs. It is who said yes, not
# who came: attendedCount is zero on almost every record. A page has to
# print it as RSVPs, the way AGENTS.md requires.
---

Every meetup the association has run, from the first one in 2007. The programme of each one was read out of the Meetup announcement that published it, so 213 of these 268 pages carry the talks of the day as well as the day, the venue, and the number of RSVPs. The other 55 pages are the days whose announcement named no session: a study group, a coding dojo, a documentation sprint, a barbecue, a social gathering, or an early meetup whose announcement said only that there would be one.
