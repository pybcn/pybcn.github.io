# PyBCN site

This repository contains the Python Barcelona Association page
deployed using [Hugo](https://gohugo.io).

## Usage for content publishing

## Prerequisites
- `curl`, `tar`, and `sha256sum`. The `bin/install` script needs them to download and verify the Hugo binary.

### Setup on your computer

Clone this repository and run the `bin/install` script. It downloads the pinned
Hugo extended binary into `bin/hugo`, checks its SHA256 against the checksums
published with the release, and does nothing if the right version is already
there.

You need `curl`, `tar`, and `sha256sum` (or `shasum`, which macOS ships). You
do not need Python, Go, or npm.

The version lives in `.hugo-version`, which is the single source of truth.
To move to a new Hugo release, edit that file and run `bin/install` again.


### Running local server

You can bring a hugo hot reload server using the `bin/serve` script. This will bring a local hot reloading server on `http://localhost:1313`.


### Publishing process

During current implementation phase, the way to publish is to push new commits to the `edition` branch. However this will change in the future, to provide some review step in the publishing process.


### How to add a new sponsor

To create a new sponsor data file, run `hugo new sponsors/my-new-sponsor.md`. This will create a pre-filled MarkDown file under `content/sponsors` with that same name.

The MarkDown file for the sponsor will have a FrontMatter section with the following fields:
- `id`: Unique identifier of this sponsor. Should be a string without spaces, preferrably kebab-case.
- `name`: Sponsor's name to be shown in all renderings.
- `logo_image`: File name for the sponsor logo, which must be under `themes/pybcn_theme/assets/images/sponsors/`. An external URL is not accepted: copy the file into the repository. The template loads it with `resources.Get`, so a file under `static/` is not found, and `bin/check-content` reports it as an error.
- `url`: URL for the sponsor web page.
- `twitter`: URL for the sponsor's twitter account.

After this FrontMatter section, any valid MarkDown will be considered generic content to be shown in detail view.

Finally, add this sponsor to the sponsors list in the corresponding level of the desired sponsors page, like `content/sponsors/_index.md`, for the main sponsors page; `content/pyladies_bcn/sponsors.md`, for the PyLadies BCN Sponsors' page; or the specific event, if appropriate.

Note that the logo images are limited to 90% of width and 150px height.


### Offering different options

Some of the pages in the sites offer different options to the visitor, like the Sponsor Us page. These pages show blocks of different lists of options with different blocks of descriptions, like what they can get, what they need to do, etc...

These pages can be created easily using the `options` layout. This layout requires an options list containing different areas, which contain blocks. Each block will have an id, an optional name to be shown, and the descriptions list. The descriptions contain name, id, and the content, which must be MarkDown content.

Probably the best example is the `sponsor-us.md`, but basically, the following might be a example:
```
layout: options

option:
- name: Area
  blocks:
  - name: First block
    id: first-block
    descriptions:
    - name: First question
      id: first-question
      content: First response
```

### Archiving external or old sites

To archive external or old sites we need to keep as they are, the `bin/archive` script can be used. It requires you to have `wget` installed, available in your `$PATH`, and working. It will need you to provide the desired URL, and will grab all the pages in the site, storing a browsable static version of them under `static/archives/your-site`, and published, on merge, under `archives/your-site`.

When doing this, please, take care to review the links are working and taking the visitor to expected URLs, since this has not been tested thoroughly and could be tricky.

Once the site was archived, you can create a new link in the navigational menu using the `url` attribute of the menu entries, like we did for old PyDays, PyData, or HacktoberFest Barcelona.


## Information for developers

### Content safety check

`bin/check-html-safety` scans `content/` and fails if it finds raw HTML that
turns a content change into script execution, a redirect, a credential prompt
or a page overlay: `<script`, `<style`, `<iframe`, a `srcdoc=` attribute,
`<object`, `<embed`, `<form`, `<meta`, `<link`, `<base`, an `on...=` event
handler, a `style=` attribute (unless its value is only sizes and margins), and
a `javascript:`, `vbscript:` or `data:` URL.

It reads every file under `content/` that Hugo renders, not only markdown:
`.org`, `.adoc`, `.rst` and `.pandoc` content can carry raw HTML too. Images and
PDFs are skipped. A file with any other extension fails the check until the
script lists it as text or as a binary asset. In each text file it reads the
YAML front matter at any depth, both as raw text and after YAML decodes it, and
the body.

```
pip install pyyaml
./bin/check-html-safety
```

The `pr-checks` workflow (`.github/workflows/pr.yml`) runs it on every pull
request.

The `ALLOWLIST` at the top of the script is empty. The Google Form and Google
Calendar embeds of the site go through the `google-embed` shortcode in
`layouts/shortcodes/`, which checks the host and which an organizer reviews. To
accept new third party markup, put it in a shortcode under `layouts/`. If an
entry is unavoidable, it is keyed by file path, pattern and the prefix of the
URL the element loads, so it permits one known embed and not any later one in
the same file, and the file that carries it needs a rule in
`.github/CODEOWNERS`, or any contributor can edit the allowed snippet.


This is a work in progress. All the design and implementation decisions are detailed in [Proposta d'estructura](https://docs.google.com/document/d/10YxQeCuGQXUjnN3o9e1oH2HJkrhxJsr31qnxO_aiCNM/edit?usp=sharing) (currently written in catalan). All the tasks are managed through our [private Trello board](https://trello.com/b/cFE8KRTS).

For now, we are not looking for contributors yet.


### Using JS code

There are, at least, three ways of embedding JS code in a page, depending on when this needs to be processed:
* **Using the extraJS block**
* **Using the requiredJS block**
* **Using the script tag wherever needed**

Remember the blocks only work in templates, but not in partials.
Also consider whether using `defer` attribute is interesting or not, which should be preferred.


### Sponsors pages implementation details

Currently, there are two sponsor pages implemented: The PyBCN sponsors and the PyLadies BCN. Both pages use the same template, in `themes/pybcn_theme/layouts/_default/sponsors.html`.

The template collects all the pages under sponsors content and iterates over the levels defined in the corresponding sponsors page, rendering the level name, if any, and then all the summaries for each sponsor defined in the level's sponsors list.

The sponsor summary is defined in a separate partial `themes/pybcn_theme/layouts/partials/sponsor_summary.html`. This partial receives the sponsor page to render the summary from.

About the creation of new sponsors, the `themes/pybcn_theme/archetypes/sponsors.md` file contains the template Hugo will use when the editor runs the command `hugo new sponsors/my-new-sponsor.md`.


### People pages implementation details: organizers, speakers...

There are three pages displaying people: PyBCN Organizers, PyLadiesBCN Organizers and PyLadiesBCN speakers. More can be added to display, for example, collaborators of other events, etc.

All pages rely on the same template: `themes/pybcn_theme/layouts/_default/people.html`. The individual person summary is defined in a separate partial template: `themes/pybcn_theme/layouts/partials/people_summary.html`, and the style are defined in `themes/pybcn_theme/assets/scss/people.scss`.

The template iterates over the defined levels, and for each level:
- displays the level name, if 'name' is provided
- displays a summary of all the people listed, limiting the number of people per line to the provided number 'people_per_line' (which must be in [12, 6, 4, 3, 4, 1])  

To add new people to the site, there is a Hugo archetype defined in `themes/pybcn_theme/archetypes/people.md` that can be used by running the command: `hugo new people/my-new-person.md`.


### Monthly event page implementation details

The monthly event page uses the meetup component to show PyBCN and PyLadies BCN meetup events lists. The template embeds the `meetup.js` code without `defer` using the `requiredJS` block. Then, it invokes the `meetup-events` partial which processes the list of meetup events.

The requests to Meetup's API are done asynchronously and should replace the spinner item with the correct list of events.


### Pages with carousel

It is possible to add a carousel of photos in any regular page by changing the layout to 'carousel'. 
This layout requires us to define the number of columns [1-12] and a list of the images and (optional) captions to display:
```
layout: carousel
carousel_columns: 6
carousel_photos:
    - photo: folder/img1.jpg
      caption: "A nice and descriptive caption"
    - photo: folder/img2.jpg
      caption: "Another nice and descriptive caption"
    - photo: folder/img3.jpg
      caption: "Yet another nice and descriptive caption"
```


### Event page

This page is designed for events like PyDay or DjangoGirls, and allows to display the description of the event as well as a carousel with images, its sponsors, organizers, speakers, previous editions and the agenda. It also offers the possibility to add as many free text elements as desired.

It allows for different sections to be added, that are displayed in a floating menu:
- Content: textual content
- carousel_photos: list of photos to appear in a carousel next to (if content_columns and carousel_columns are indicated) or below the main content.
- free_text_sections: list of sections (title, id, content) containing textual content
- events (special component, see description below)
- sponsor_levels 
- people_sections (special component, see description below)  
- previous_editions 

The **agenda** is based on the code in [https://www.liquidlight.co.uk/blog/create-an-event-schedule-with-html-table/](https://www.liquidlight.co.uk/blog/create-an-event-schedule-with-html-table/) and requires to define the duration of the time spans in which we want to divide the slots (e.g. 30 minutes slots), how many parallel tracks does the event have, a list of the time slots and a list of the events.

Each event in the list must indicate:
- the starting and ending time slots (may be the same if the event only spans for one time slot)
- the track lenght (e.g. 4 if the event has 4 tracks and the element should span across all of them, like the welcome session)-
- the title of the event

Each event in the list can indicate:
- the color of the event in the calendar: red, orange, yellow, green, blue, purple (defaults to orange)
- the location where the event will take place (a room, or a url)
- the topic of the event (e.g. Data Science, Security...)
- the type of the event: talk, workshop, coffee, lunch, photo, group, qa, lightning
- `language`: the language the talk is given in, shown as text (e.g. `Spanish`)
- `title_lang`: set it only when the title itself is not in English, with
  `Spanish`, `Castellano`, `Catalan`, `Català` or a BCP 47 code such as `es`.
  It puts a `lang` attribute on the title, so a screen reader reads it with
  the right voice. `language` never sets it: many talks given in Spanish have
  an English title
- `python_level` and `topic_level`: the experience the attendee needs. Use one
  of `beginner`, `intermediate` or `advanced`

#### Experience levels

`python_level` and `topic_level` take a token, never markup. The site renders
each token as a badge with a coloured dot and the matching text label, so the
level does not depend on colour alone:

| Token | Label | Dot |
|---|---|---|
| `beginner` | Beginner | green |
| `intermediate` | Intermediate | amber |
| `advanced` | Advanced | red |

An unknown token prints as plain text and logs a build warning. The tokens and
the labels live in `themes/pybcn_theme/layouts/partials/level_badge.html`.

#### Agenda legend

`legend` is a list of items, not an HTML string. Each item is one of:

```
legend:
  - type: workshop        # any event type, plus "sponsor" for the gold star
    label: Hands-on       # optional, overrides the default label
  - type: talk
  - separator: true       # a visual group break
  - level: beginner
  - level: intermediate
  - level: advanced
```

The icons and the default labels come from
`themes/pybcn_theme/layouts/partials/event_types.html`.

```
spansDuration: 20
numTracks: 4
eventTimes: [8:00, 8:20, 8:40, 9:00, 9:20, 9:40, 10:00, 10:20, 10:40, 11:00, 11:20, 11:40, 12:00, 12:20, 12:40, 13:00]
events:
    - start_time_slot: 8:00
      end_time_slot: 8:40
      track_length: 4
      color: green
      title: Arrival and registration
      location: Registration Area
      type: coffee
    - start_time_slot: 9:00
      end_time_slot: 9:20
      track_length: 4
      color: blue
      title: Welcome Talk
      location: Main Stage
      type: group
    - start_time_slot: 9:40
      end_time_slot: 10:00
      track_length: 3
      color: yellow
      title: An interesting talk with a big audience
      location: http://www.youtube.com
      level: advanced
      topic: Data Science
      type: talk
    - start_time_slot: 9:40
      end_time_slot: 10:20
      track_length: 1
      color: red
      title: Some long talk
      location:  http://www.youtube.com
      level: advanced
      topic: Data Science
      type: workshop
    - ...
```


The **people_sections** option allows to add a list of sections displaying people, such as organizers, speakers and mentors. 
Each section can have subsections (e.g. in organizers, we could have 'main organizers' and 'volunteers').
Example:

```
people_sections:
    - title: Organizers
      id: organizers
      levels:
        - people_per_line: 4
          people:
              - elisabeth-ortega-carrasco
              - lpmayos
              - natalia
              - nuria
    - title: Mentors, speakers & volunteers
      id: main_organizers
      levels:
        - name: Mentors
          people_per_line: 4
          people:
              - esperanza
              - eli
              - sandra
              - alex
        - name: Speakers
          people_per_line: 4
          people:
              - alberto
              - cristina
              - magda
              - cris-lopez
              - maria
              - martina
              - violeta
        - name: Volunteers
          people_per_line: 4
          people:
              - mireia
              - josep
```