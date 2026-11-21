"""Write recent public GitHub activity into README.md.

Reads the account's public Atom feed and keeps only events worth showing
(new repos, pull requests, issues, releases). Pushes, branch events and
anything in this profile repo (LeetHub commits) are skipped as noise.
Usage: python update_readme.py [README path] [feed URL or local file]
"""
import sys
import urllib.request
import xml.etree.ElementTree as ET

USER = "zealot-SEAlot"
FEED = f"https://github.com/{USER}.atom"
COUNT = 5
KEEP = ("created a repository", "opened a pull request", "merged a pull request",
        "opened an issue", "released", "made", "forked")
SKIP_REPO = f"github.com/{USER}/{USER}"
START, END = "<!-- ACTIVITY:START -->", "<!-- ACTIVITY:END -->"
NS = {"a": "http://www.w3.org/2005/Atom"}


def recent_activity(xml_text, count=COUNT):
    lines = []
    for entry in ET.fromstring(xml_text).iterfind("a:entry", NS):
        title = entry.findtext("a:title", "", NS).strip()
        link = entry.find("a:link", NS).get("href", "")
        if SKIP_REPO in link or not any(k in title for k in KEEP):
            continue
        action = title.removeprefix(f"{USER} ")
        date = entry.findtext("a:updated", "", NS)[:10]
        lines.append(f"- [{action}]({link}) · {date}")
        if len(lines) == count:
            break
    return lines


def replace_section(readme, lines):
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n" + "\n".join(lines) + f"\n{END}{tail}"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    src = sys.argv[2] if len(sys.argv) > 2 else FEED
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"User-Agent": "readme-activity-updater"})
        xml_text = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    else:
        xml_text = open(src, encoding="utf-8").read()
    lines = recent_activity(xml_text)
    if not lines:
        print("No matching activity; leaving README unchanged.")
        return
    with open(path, encoding="utf-8") as f:
        readme = f.read()
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(replace_section(readme, lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
