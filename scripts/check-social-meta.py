from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
files = [root / "index.html", root / "waitlist.html", root / "founders.html"]

required = {
    "og:image": r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
    "og:image:width": r'<meta[^>]+property=["\']og:image:width["\'][^>]+content=["\']([^"\']+)["\']',
    "og:image:height": r'<meta[^>]+property=["\']og:image:height["\'][^>]+content=["\']([^"\']+)["\']',
    "og:site_name": r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\']([^"\']+)["\']',
    "twitter:card": r'<meta[^>]+name=["\']twitter:card["\'][^>]+content=["\']([^"\']+)["\']',
}

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    print(f"\nChecking {file_path.name}")
    for key, pattern in required.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            print(f"  ✓ {key}: {match.group(1)}")
        else:
            print(f"  ✗ Missing {key}")

    og_desc = re.search(r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']+)["\']', text, re.IGNORECASE)
    if og_desc:
        length = len(og_desc.group(1))
        print(f"  ✓ og:description length: {length}")
        if length > 200:
            print("    ⚠ Description is longer than 200 chars and may be truncated")
    else:
        print("  ✗ Missing og:description")
