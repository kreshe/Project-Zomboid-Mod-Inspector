import urllib.request
import json
import re


APP_VERSION = "1.0.1"

GITHUB_API = (
    "https://api.github.com/repos/"
    "kreshe/Project-Zomboid-Mod-Inspector/releases/latest"
)


def normalize_version(version):
    version = str(version).strip().lower()

    if version.startswith("v"):
        version = version[1:]

    match = re.match(
        r"(\d+)\.(\d+)\.(\d+)",
        version
    )

    if not match:
        return (0, 0, 0)

    return tuple(
        int(x)
        for x in match.groups()
    )


def get_latest_release():

    request = urllib.request.Request(
        GITHUB_API,
        headers={
            "User-Agent": "Project-Zomboid-Mod-Inspector"
        }
    )

    try:

        with urllib.request.urlopen(
            request,
            timeout=5
        ) as response:

            data = json.loads(
                response.read().decode("utf-8")
            )

        assets = data.get(
            "assets",
            []
        )

        zip_url = None

        for asset in assets:

            name = asset.get(
                "name",
                ""
            )

            if name.lower().endswith(".zip"):

                zip_url = asset.get(
                    "browser_download_url"
                )

                break

        return {
            "version": data.get(
                "tag_name",
                ""
            ),
            "name": data.get(
                "name",
                ""
            ),
            "url": data.get(
                "html_url",
                ""
            ),
            "zip": zip_url
        }

    except Exception as e:

        print(
            f"Ошибка проверки обновлений: {e}"
        )

        return None


def check_for_update():

    release = get_latest_release()

    if not release:
        return None

    current = normalize_version(
        APP_VERSION
    )

    latest = normalize_version(
        release["version"]
    )

    if latest > current:
        return release

    return None