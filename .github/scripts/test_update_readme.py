from update_readme import END, START, recent_activity, replace_section

FEED = """<feed xmlns="http://www.w3.org/2005/Atom">
<entry><title type="html">zealot-SEAlot pushed gym</title>
  <link href="https://github.com/zealot-SEAlot/gym/compare/a...b"/><updated>2026-11-20 05:00:00 UTC</updated></entry>
<entry><title type="html">zealot-SEAlot opened a pull request in zealot-SEAlot</title>
  <link href="https://github.com/zealot-SEAlot/zealot-SEAlot/pull/1"/><updated>2026-11-19 05:00:00 UTC</updated></entry>
<entry><title type="html">zealot-SEAlot opened a pull request in gym</title>
  <link href="https://github.com/zealot-SEAlot/gym/pull/7"/><updated>2026-11-18 05:00:00 UTC</updated></entry>
</feed>"""


def test_keeps_real_events_and_replaces_section():
    lines = recent_activity(FEED)
    assert lines == ["- [opened a pull request in gym](https://github.com/zealot-SEAlot/gym/pull/7) · 2026-11-18"]
    out = replace_section(f"top\n{START}\nold\n{END}\nbottom", lines)
    assert out == f"top\n{START}\n{lines[0]}\n{END}\nbottom"


if __name__ == "__main__":
    test_keeps_real_events_and_replaces_section()
    print("ok")
