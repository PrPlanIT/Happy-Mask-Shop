"""Copy Mealie's frontend to a writable folder and link the SysEggplant stylesheet into every page.

Run with Mealie's own image, so the copied frontend always matches the Mealie that serves it:

    python3 link-theme.py <theme-files> <out>

<theme-files> holds syseggplant.css and monof_tt.txt; Mealie then serves <out> with STATIC_FILES=<out>.
"""
import glob
import importlib.util
import os
import shutil
import sys

files, out = sys.argv[1], sys.argv[2]
src = os.path.join(importlib.util.find_spec("mealie").submodule_search_locations[0], "frontend")
shutil.copytree(src, out, dirs_exist_ok=True)
for f in ("syseggplant.css", "monof_tt.txt"):
    shutil.copy(os.path.join(files, f), os.path.join(out, f))

tag = '<link rel="stylesheet" href="/syseggplant.css">'
pages = 0
for page in glob.glob(out + "/**/*.html", recursive=True):
    html = open(page, encoding="utf-8").read()
    if tag not in html and "</head>" in html:
        open(page, "w", encoding="utf-8").write(html.replace("</head>", tag + "</head>", 1))
        pages += 1
assert pages, "no pages found to link the theme into"
print(f"theme linked into {pages} pages")
