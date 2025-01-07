#!/usr/bin/env python3

import subprocess as sp
import os
import time

dirs = list(e.name for e in os.scandir() if e.is_dir() and e.name.startswith("day"))
for d in sorted(dirs):
    try:
        ts = time.perf_counter_ns()
        sp.run(
            ["python3", f"{d}/{d}.py", f"{d}/input"],
            stdout=sp.PIPE,
            stderr=sp.PIPE,
            timeout=60,
        )
        t = int((time.perf_counter_ns() - ts) // 1e6)
        print(f"{d}: {t:,}ms", flush=True)
    except sp.TimeoutExpired:
        print(f"{d}: Timed out")
