#!/usr/bin/env python
# -*- coding: utf-8 -*-
from livereload.task import Task
import json
import subprocess

def f():
    import subprocess
    subprocess.call(("nikola", "build"))

fdata = json.loads('''["conf.py", "themes", "templates", "galleries", "posts", "stories", ""]''')

for watch in fdata:
    Task.add(watch, f)
