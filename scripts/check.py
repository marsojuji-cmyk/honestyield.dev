"""CI for honestyield.dev: every internal link resolves, required files exist,
the Rule text is intact, and no placeholder copy ships."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = []

def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)

# 1. required files
for f in ["index.html", "styles.css", "ledger/index.html", "lab/index.html",
          "about/index.html", "README.md", "LICENSE"]:
    if not os.path.exists(os.path.join(ROOT, f)):
        fail("missing required file: " + f)

# 2. every internal link resolves
for dirpath, _, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in files:
        if not fn.endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        html = open(p).read()
        for m in re.finditer(r'href="([^"#:]+)"', html):
            h = m.group(1)
            if h.startswith(("http", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(dirpath, h))
            if not os.path.exists(target):
                fail(os.path.relpath(p, ROOT) + " -> broken link " + h)

# 3. the Rule's six clauses ship verbatim
rule = open(os.path.join(ROOT, "index.html")).read()
for clause in ["A yield claim is a measured claim",
               "A run pair is a before-and-after measurement",
               "the savings number is null",
               "Negative results are admitted",
               "The ledger is append-only",
               "Authority only narrows"]:
    if clause not in rule:
        fail("rule clause missing from index.html: " + repr(clause))

# 4. no placeholder copy
for dirpath, _, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in files:
        if not fn.endswith((".html", ".css", ".md")):
            continue
        text = open(os.path.join(dirpath, fn)).read().lower()
        if "lorem ipsum" in text:
            fail("lorem ipsum in " + fn)

if failures:
    print(str(len(failures)) + " check(s) failed")
    sys.exit(1)
print("all checks passed")
