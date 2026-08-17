# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the source for the **Disciplinas UVV** website (https://disciplinas.uvv.br), a Jekyll
static site where professors at Universidade Vila Velha (UVV) publish course content, schedules,
announcements, and resources for students. Built with Jekyll + the `just-the-docs` theme.

## Common commands

Install/update dependencies:
```
bundle install
bundle update --all
bundle update --bundler
```

Run the site locally with livereload:
```
bundle exec jekyll serve --livereload
```

Build for production:
```
JEKYLL_ENV=production bundle exec jekyll build
```

There are no automated tests, linters, or CI configured in this repo — verification is done by
building the site and checking the output in `_site/`.

## Architecture

### Content model: courses (`disciplinas`) contain sections (`turmas`)

Each course ("disciplina") lives in `disciplinas/<nome_dir_disciplina>/` (e.g.
`disciplinas/ed2/`) and has these top-level pages: `index.md`, `syllabus.md`, `leituras.md`,
`recursos.md`, `pessoal.md`.

Inside a course directory, each class section ("turma") for a given year/semester lives in its
own subdirectory named `<ano><semestre>_<turma>` (e.g. `disciplinas/ed2/20251_cc6m/`), containing
`index.md`, `avisos.md`, `calendario.md`, `horario.md`.

New courses/sections are scaffolded from templates in `modelos/` (see `modelos/index.md`,
`modelos/turmas/*.md`) using placeholder tokens `NOME-DA-DISCIPLINA`, `NOME-DA-TURMA`,
`ANOSEMESTRE`, `TURMA` that get substituted via `sed`. `cod/cria_estrutura.sh` is a reference
script (hand-edit its variables at the top before running) that shows the expected scaffolding
steps for a new course + sections — treat it as a template to adapt, not a script to run as-is.

### Data collections drive announcements and schedules

Two custom Jekyll collections hold structured data that pages query via Liquid, rather than
authoring HTML/tables directly on each turma page:

- **`_avisos/<disciplina>/<anosemestre>/<turma>/semana-NN.md`** — weekly announcements. Front
  matter: `title`, `semana`, `disciplina`, `semestre`, `turma`, `date`. Rendered on a turma's
  `avisos.md`/`index.md` page via `site.avisos | where: "disciplina", ... | where: "semestre", ...
  | where: "turma", ...`.
- **`_horarios/<disciplina>/<anosemestre>/<turma>/horario.md`** — weekly schedule grid. Front
  matter: `disciplina`, `semestre`, `turma`, `timeline` (time slots), `schedule` (day-by-day
  events with `name`/`start`/`end`/`location`). Queried the same way via `site.horarios`.

Both collections are declared in `_config.yml` under `collections:`, with `defaults:` there
assigning layouts by collection type (`staffer` for `_pessoal`, `module` for `_monitorias`,
`schedule` for `_horarios`, `announcement` for `_avisos`).

`calendario.md` files are NOT a collection — they're static HTML tables (see
`modelos/turmas/calendario.md`) hand-edited per turma, `include_relative`d into that turma's
`index.md`.

Other collections: `_pessoal/` (staff bios, one file per person, shared across courses),
`_monitorias/<disciplina>/<anosemestre>/` (tutoring session notes).

### Front matter conventions

Most content pages use `just-the-docs` navigation front matter: `layout`, `title`, `parent`,
`grand_parent`, `nav_order`, `nav_exclude`, `has_children`, `has_toc`, `last_modified_date`. When
adding a page under a course/turma, set `parent`/`grand_parent` to match the exact `title` string
of the enclosing pages so it nests correctly in the site nav — this is a common source of broken
navigation if titles drift out of sync.

### Layouts and includes

Custom layouts live in `_layouts/`: `announcement.html`, `schedule.html`, `staffer.html`,
`module.html`, `post.html` (these extend `just-the-docs`/`just-the-class` theme layouts pulled in
via the gem, not vendored in this repo). Shared partials live in `_includes/components/`
(`sidebar.html`, `footer.html`) and `_includes/` (`minutes.liquid`, `head_custom.html`,
`search_placeholder_custom.html`).

### Assets

Course-specific static assets go in `assets/disciplinas/<nome_dir_disciplina_abreviado>/`. Other
asset trees exist for specific hardware/robotics courses (`assets/arduino/`, `assets/raspberry/`,
`assets/robo_sumo/`, `assets/maqvirt/`) and general site assets (`assets/images/`, `assets/js/`,
`assets/docs/`).

### Build exclusions

`_config.yml`'s `exclude:` list keeps non-site files out of the Jekyll build: `cod/`, `Gemfile`,
`Gemfile.lock`, `LICENSE`, `_config.yml`, `README.md`, `INSTRUCOES`, `modelos/`, `mapa.emmx`,
`remove_polyfill.sh`, `roteiros/`. When adding new top-level non-content directories/files,
add them here too.

### Language

All site content and commit-adjacent documentation (`INSTRUCOES`, `README.md`) is in Brazilian
Portuguese (`lang: pt-br` in `_config.yml`); match that when writing or editing content.
