#!/usr/bin/env python
import os
from functions import *

header = """
<!doctype html>\n
<html>\n
<head>\n
<meta charset="utf-8">\n
<meta name="viewport" content="width=device-width, initial-scale=1.0">\n
<link rel="stylesheet" type="text/css" href="style.css">\n
<title>EGA</title>\n
</head>\n
"""

script_conf = """
<script type="text/x-mathjax-config">\n
  MathJax.Hub.Config({\n
    tex2jax: {\n
      inlineMath: [['$','$']],\n
      displayMath: [["\\\\[","\\\\]"],['$$','$$']],\n
      processEscapes: true,\n
    }\n
  });\n
</script>\n\n
<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>\n
"""

path = get_path()
for _, _, files in os.walk(path):
  for fname in files:
    if '.tag' in fname or fname == 'index':
      with open(path + fname, 'r') as rf:
        with open(path + fname + '.html', 'w+') as wf:
          wf.write(header)
          wf.write(script_conf)
          wf.write('<body>\n')
          for line in rf:
            if '<span data-tag="">None</span>' in line:
              line = line.replace('<span data-tag="">None</span>', '')
            if '/tag/' in line:
              line = line.replace('/tag/', '')
            wf.write(line)
          wf.write('</body>\n</html>')
#      os.remove(path + fname)



