#!/usr/bin/env python3

from array import array
import os
import re
import sys

"""
This script generates unfilled icons based on 22px icons
"""

OUTPUT_DIR: str = "./dist"
INPUT_DIR: str = "../breeze-icons/icons"
COLOR_EXP: str = "#[0-9a-zA-Z]{6}"

ICON_PATHS: array = ['actions', 'places', 'mimetypes', 'devices', 'applets']

def optimize_svg(input_file, output_file):
    os.system(
        f"scour -i '{input_file}' -o '{output_file}' --enable-comment-stripping --strip-xml-space --remove-metadata --renderer-workaround --remove-descriptions --enable-id-stripping --shorten-ids --set-precision=5 --set-c-precision=5 --create-groups --remove-descriptive-elements --remove-titles  --enable-viewboxing > /dev/null")


def main():
    for dirpath, _dirnames, filenames in os.walk(INPUT_DIR):
        for c_file in filenames:
            filepath = os.path.join(dirpath, c_file)
            current_resource_icons = filepath.split('/')[3]

            if current_resource_icons not in ICON_PATHS:
                continue

            # Filter out files
            if not (c_file.endswith('.svg') and '/22' in filepath):
                continue

            # skip symlinks or edit SVGs
            if os.path.islink(filepath):
                continue
            else:
                with open(filepath, "r") as svg_file:
                    data_file = svg_file.read().replace("\n", "")

                # skip icons with gradient
                if 'stop-color' in data_file or 'transform' in data_file:
                    continue

                # sanitize output name
                output_file = c_file.replace("application-", "")
                output_file = re.sub(
                    "vnd.ms|vnd.oasis|vnd|x-", "", output_file)
                output_file = re.sub("\/-|\/\s|\/\.", "/", output_file)
                output_file = output_file.replace("+", "-")
                output_file = output_file.replace("_", "-")
                output_file = output_file.replace(".", "-")
                output_file = output_file.replace("-svg", ".svg")
                output_file = re.sub(r"^-", "", output_file)
                output_file = os.path.join(OUTPUT_DIR, output_file)

                optimize_svg(filepath, output_file)

                # with open(output_file, "r") as svg_file:
                #     re_fill = svg_file.read().replace("\n", "")

                # re_fill = re.sub(r"#[f|F]{3,6}", 'white-hex', re_fill)
                # re_fill = re.sub(r"#[0-9a-zA-Z]{3,6}", '#000000', re_fill)

                # re_fill = re_fill.replace("currentColor", "#000000")
                # re_fill = re_fill.replace("white-hex", "#FFFFFF")

                # new_svg_file = open(output_file, "w")
                # new_svg_file.write(re_fill)
                # new_svg_file.close()
            

# I've structured the program like this in case I want to do multiprocessing later
if __name__ == '__main__':
    sys.exit(main())
