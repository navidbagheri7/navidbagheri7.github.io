# Navid Bagheri Shouraki — personal website

A static academic portfolio built with HTML, CSS, and JavaScript. Designed for GitHub Pages, with no build step, runtime dependencies, third-party scripts, analytics, or remote font requests. The published site is [navidbagheri7.github.io](https://navidbagheri7.github.io/); its source is [navidbagheri7/navidbagheri7.github.io](https://github.com/navidbagheri7/navidbagheri7.github.io).

## Preview locally

From this folder:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open **http://localhost:8765**. You can also open `index.html` directly in a browser. If working over SSH, forward port 8765 in VS Code's Ports panel, or use `ssh -L 8765:127.0.0.1:8765 your-host`.

## Edit content

- `index.html`: compact introduction, research interests, and two selected publication previews.
- `publications.html`: the complete publication list and expandable summaries.
- `academic.html`: horizontal, scrollable rows for education and research experience, a dated CV-style list of honors and awards, a compact workshops and schools list, plus academic service.
- `repositories.html`: collaborative research code and six evaluated learning labs, each with repository and interactive demo links.
- `contact.html`: a collaboration invitation, primary personal email, university email addresses, Scholar, LinkedIn, and CV links.
- `styles.css`: palette, typography, and responsive layouts. Theme colors are defined at the top.
- `script.js`: the light/dark theme and accessible academic scrolling controls. The theme preference persists between pages.
- `assets/navid-bagheri-shouraki-cv.pdf`: a copy of `RESUME/CV.pdf`. Replace it when updating the CV.
- `assets/fonts/`: locally bundled DM Sans and Instrument Serif, with their SIL Open Font License files.
- `preview/`: desktop and mobile screenshots for review; not needed for hosting.

Each navigation item opens a separate static HTML page. All pages, navigation, and expandable summaries work with JavaScript disabled. The layout uses a white background, bold sans-serif name styling, serif section headings, and a white and charcoal palette with restrained navy accents. The large animated illustration and promotional headings have been removed. The header and footer are repeated in each HTML file; keep their navigation consistent when adding pages.

## Content sources and editorial choices

The primary source is the local `RESUME/CV.tex` and `RESUME/CV.pdf`, read on 2 October 2026. Research descriptions were updated from `CSI_2026/main.pdf`, particularly pages 2, 27, 30, and 38, with summaries and expanded overviews kept distinct from formal paper abstracts. The editing-paper description follows the report’s explanation of the DING follow-up. The site includes these verified destinations:

- [UniGuide workshop paper](https://openreview.net/pdf/e98a1be6111695a53e21d1da3f85beec1dd04c27.pdf)
- [DInG paper](https://arxiv.org/abs/2512.18365) and [code](https://github.com/YazidJanati/ding)
- [Image and video editing paper](https://arxiv.org/abs/2602.14157), [code](https://github.com/ahmedgh970/ding-editor), and [project page](https://ahmedgh970.github.io/ding-editor/)

Publication status and author order follow the supplied CV. The user explicitly confirmed that UniGuide must retain Navid Bagheri Shouraki first and M. Hegazy second; both names carry a superscript asterisk with an equal-contribution note. UniGuide's extended-version review status also comes from the CV and should be refreshed when it changes.

The visual design is original, informed by the academic portfolio structure of https://darioshar.github.io/. No assets or code were copied from that site. The Repositories page credits the collaborators who maintain the two linked public codebases. The site links to the personal GitHub profile `navidbagheri7`. Phone number, GPA details beyond the education section, and the full course list are omitted from the page for focus; the linked original CV contains the full résumé.

## Publish updates

The repository uses GitHub Pages at **https://navidbagheri7.github.io/**. Push changes to `main` to run the static checks. Publish the update with **Actions → Publish personal website → Run workflow**. The Pages workflow checks local links and assets, stages only the website files, and deploys them.

Run the static checks locally with `python3 scripts/check_site.py`. HTML navigation and publication disclosures also work without JavaScript; JavaScript adds theme persistence and academic scrolling controls. The contact links open the visitor's email application.

Canonical URLs and social preview metadata point to the live site. Keep the bundled CV, publication status and contact details current when updating the content.

Supervisor Scholar links were checked against [Alain Durmus’s homepage](https://alain.perso.math.cnrs.fr/) and [Eric Moulines’s faculty page](https://mbzuai.ac.ae/academics/faculty-directory/eric-moulines). The personal email `navidbagheri7@gmail.com` is the user-provided primary contact address. Academic rows support arrow buttons, touch/trackpad scrolling, and keyboard navigation (Left/Right, Home/End), with native scrolling available without JavaScript.

The upper-left header uses the full name in black sans-serif with no tagline. Education has no subtitle. The homepage affiliation reads Sorbonne University / École Polytechnique as requested; the education details retain the CV’s institutional history. Research interests sit below the introduction. The desktop introduction includes the supplied portrait in its right column.


The homepage uses the supplied `photo_5935805993654620536_w.jpg`, copied to `assets/navid-portrait.jpg`. The portrait sits to the right of the introduction on desktop and stacks above it on narrow screens. CSS controls the visible framing without modifying the original photograph. The palette combines navy accents, light blue panels, and restrained teal details on a white background.

MBZUAI Winter School is listed under Workshops and schools, separate from honors and awards. The date remains 2026 as documented in the CV; participation is described as selection rather than assumed attendance.
