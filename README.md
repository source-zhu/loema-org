# loema.org

The public trust layer of Loema. Static, zero external requests, no cookies,
no analytics, no forms.

Everything under `site/` is generated — edit `build.py` at the repo root and
run `python3 build.py` to regenerate. Deploy: Cloudflare Pages, no build
command, build output directory `site` (the `_headers` file there serves
`/constitution/schema` as JSON Schema — one address for the format, no
version number).

Held back deliberately (reserved, unbuilt): /essays/, /clarity-analytics/.

Legal pages are accurate statements of actual practice (governing law:
Virginia), to be hardened in the attorney pass. The format's open license is
being settled with counsel; the format page says so until it is named.
