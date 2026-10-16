from built_in_os import demo_os
from built_in_sys import demo_sys
from built_in_shutil import demo_shutil
from built_in_math import demo_math
from built_in_json import demo_json

from ext_pyfiglet import demo_pyfiglet
from ext_qrcode import demo_qrcode
from ext_faker import demo_faker
from ext_emoji import demo_emoji
from ext_humanize import demo_humanize
from ext_pytz import demo_pytz
from ext_slugify import demo_slugify
from ext_tabulate import demo_tabulate
from ext_babel import demo_babel
from ext_wikipedia import demo_wikipedia


def main():
    print("=== LABORATORY WORK 4 ===\n")

    demo_os()
    demo_sys()
    demo_shutil()
    demo_math()
    demo_json()

    demo_pyfiglet()
    demo_qrcode()
    demo_faker()
    demo_emoji()
    demo_humanize()
    demo_pytz()
    demo_slugify()
    demo_tabulate()
    demo_babel()
    demo_wikipedia()

    print("\n=== ALL MODULES COMPLETED ===")


if __name__ == "__main__":
    main()