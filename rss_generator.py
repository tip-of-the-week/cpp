#!/usr/bin/env python3
# coding: utf-8

import re
import sys
import glob
import pathlib
import datetime
import markdown


def gen_feed(tips, url):
    date = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    title_re = r"\* +(\*\*)?(?P<title>(?(1).+(?<!\*\*)|.+))(?(1)\*\*$|$)"

    xml = ""
    for tip in tips:
        title = re.search(title_re, tip["content"], re.RegexFlag.MULTILINE).group("title").replace("<", "&lt;").replace(">", "&gt;")

        link = tip["short_path"]
        md = markdown.markdown(f"<div markdown=1>{tip['content']}</div>", extensions=["extra", "codehilite"], output_format="xhtml")
        md = md.replace("<details open>", "<details open=true>").replace("<", "&lt;").replace(">", "&gt;")

        xml += f"""<item>
            <title>{title}</title>
            <link>{url}{link}</link>
            <guid>{url}{link}</guid>
            <pubDate>{date}</pubDate>
            <description>{md}</description>
        </item>\n"""
    return xml


def main():
    tips = []

    for file in glob.glob("tips/*.md"):
        path = pathlib.Path(file)
        tips.append({
            "content": path.read_text(encoding="utf-8"),
            "short_path": path.name,
        })

    xml = gen_feed(tips, "https://github.com/tip-of-the-week/cpp/blob/master/tips/")
    template = pathlib.Path("feed.template.xml")
    new_content = template.read_text().replace("<!-- START FEED -->", xml)
    pathlib.Path("feed.xml").write_text(new_content)

    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

