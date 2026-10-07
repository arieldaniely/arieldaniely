from pathlib import Path
import re
import xml.etree.ElementTree as ET

START = "<!-- PROFILE-STATS:START -->"
END = "<!-- PROFILE-STATS:END -->"

def update_readme(root: Path):
    for name in ("stats-light.svg", "stats-dark.svg"):
        path = root / "profile" / name
        svg = ET.parse(path).getroot()
        if svg.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError("Invalid stats SVG")
        if "Something went wrong" in path.read_text(encoding="utf-8"):
            raise ValueError("Refusing to publish an error card")

    path = root / "README.md"
    text = path.read_text(encoding="utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("README must contain exactly one stats marker pair")
    card = '''<!-- PROFILE-STATS:START -->
<p dir="ltr" align="right">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="profile/stats-dark.svg" />
    <img alt="הפעילות והדירוג ב־GitHub, כולל מאגרים פרטיים הזמינים להרשאה" src="profile/stats-light.svg" />
  </picture>
</p>

<sub>החישוב כולל מאגרים ציבוריים ופרטיים הזמינים להרשאה. מוצגים נתונים מצטברים בלבד.</sub>
<!-- PROFILE-STATS:END -->'''
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: card, text, flags=re.S)
    path.write_text(updated, encoding="utf-8")

if __name__ == "__main__":
    update_readme(Path.cwd())
