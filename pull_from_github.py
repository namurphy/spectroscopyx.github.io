#!/usr/bin/env python
import requests as re

OUTPUT_DIR = "web/pages/"
BASE_URL = "https://raw.githubusercontent.com/PlasmaPy/SpectroscoPyx/master/"
WEB_BASE_URL = "https://raw.githubusercontent.com/PlasmaPy/spectroscopyx.github.io/src/"
PAGES = [
    {
        "filename": f'{OUTPUT_DIR}conduct.md',
        "url": f'{BASE_URL}CODE_OF_CONDUCT.md',
        "metadata": {"title": "Code of conduct", "slug": "conduct"},
    },
    {
        "filename": f'{OUTPUT_DIR}contribute.md',
        "url": f'{BASE_URL}CONTRIBUTING.md',
        "metadata": {"title": "Contribute to PlasmaPy", "slug": "contribute"},
    },
    {
        "filename": f'{OUTPUT_DIR}license.md',
        "url": f'{WEB_BASE_URL}LICENSE.md',
        "metadata": {"title": "License", "slug": "license"},
    },
    {
        "filename": f'{OUTPUT_DIR}vision.md',
        "url": f'{BASE_URL}vision_statement.md',
        "metadata": {"title": "Vision statement", "slug": "vision"},
    },
]



for page in PAGES:
    content = "".join(
        "{}: {}\n".format(field, tag)
        for field, tag in page["metadata"].items()
    )

    content += "\n"
    content += re.get(page["url"]).content.decode("utf-8")
    with open(page["filename"], "w+") as f:
        f.write(content)
