#!/usr/bin/env -S uv run --script
#
from image import Image, rgba


def main():
    width = 400
    height = 400
    img = Image(width, height, rgba(255, 255, 255))
    for frame in range(0, width):
        for y in range((height // 2) - 2, (height // 2) + 2):
            for x in range(0, frame):
                img.set_pixel(x, y, (255, 0, 0))
        img.save(f"seq.{frame:04d}.png")


if __name__ == "__main__":
    main()
