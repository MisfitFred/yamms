#!/usr/bin/env python3
import re
from pathlib import Path

root = Path("docs/source")
files = list(root.rglob("*.rst"))
changed_files = []
for p in files:
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    i = 0
    changed = False
    while i < len(lines):
        out.append(lines[i])
        # Only adjust adornment lines when both title and adornment are not indented
        if i + 1 < len(lines):
            title_line = lines[i]
            nxt = lines[i + 1]
            # skip if title or adornment are indented (likely code/literal blocks)
            if title_line.lstrip() != title_line or nxt.lstrip() != nxt:
                i += 1
                continue
            # match adornment lines that consist of 2+ non-word, non-space characters
            m = re.fullmatch(r"([^\w\s]{2,})", nxt.strip())
            if m:
                ch = m.group(1)[0]
                title = title_line.rstrip("\n")
                new_line = ch * len(title)
                # preserve original trailing spaces
                if new_line != nxt:
                    out.append(new_line)
                    changed = True
                    i += 2
                    continue
        i += 1
    if changed:
        p.write_text("\n".join(out) + "\n", encoding="utf-8")
        changed_files.append(str(p))

if changed_files:
    print("Fixed title underlines in:")
    for f in changed_files:
        print(" -", f)
else:
    print("No changes needed")
