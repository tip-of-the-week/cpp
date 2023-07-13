#!/usr/bin/env python3
# coding: utf-8

import re
import sys
import glob
import pathlib
from datetime import datetime
import markdown


def sanitize(text: str) -> str:
    return text.replace("<", "&lt;").replace(">", "&gt;")


def gen_feed(tips, url):
    title_re = r"\* +(\*\*)?(?P<title>(?(1).+(?<!\*\*)|.+))(?(1)\*\*$|$)"
    link_re = r"(?P<link>(?<!\[|\()https?://[\w\./\?&=\-\+#:,;%]+)"

    xml = ""
    for tip in tips:
        link = tip["short_path"]
        tip_num = link.replace(".md", "")

        date = datetime.fromtimestamp(tip["pub_date"]).strftime("%a, %d %b %Y %H:%M:%S GMT")

        title = re.search(title_re, tip["content"], re.RegexFlag.MULTILINE).group("title")
        title = sanitize(title)

        content = tip["content"]
        updated = content
        for match in re.finditer(link_re, content):
            naked_link = match.group("link")
            updated = updated.replace(naked_link, f"[{naked_link}]({naked_link})")

        # TODO: find a way to colorize the code, the documentation advise to have custom css
        # The classes should already have been applied to the code thanks to extension 'codehilite'
        md = markdown.markdown(
                f"<div markdown=1>{updated}</div>",
                extensions=["extra", "codehilite", "nl2br"],
                output_format="xhtml"
        )
        md = md.replace("<p></p>", "")
        md = md.replace("<details open>", "<details open=true>")
        md = "<![CDATA[ %s]]>" % md

        xml += f"""<item>
            <title>{tip_num} - {title}</title>
            <link>{url}{link}</link>
            <guid>{url}{link}</guid>
            <pubDate>{date}</pubDate>
            <description>{md}</description>
        </item>\n"""
    return xml


def main():
    tips = []
    files = sorted(glob.glob("tips/*.md"), reverse=True)

    for file in files:
        path = pathlib.Path(file)
        tips.append({
            "content": path.read_text(encoding="utf-8"),
            "short_path": path.name,
            "pub_date": path.lstat().st_ctime,
        })

    xml = gen_feed(tips, "https://github.com/tip-of-the-week/cpp/blob/master/tips/")
    template = pathlib.Path("feed.template.xml")
    new_content = template.read_text().replace("<!-- START FEED -->", xml)
    pathlib.Path("feed.xml").write_text(new_content)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

