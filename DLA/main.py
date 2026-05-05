#!/usr/bin/env -S uv run --script
import random

from image import Image, rgba


# 1. create sim and set random seeds
#
class DLA:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.sim_data = Image(self.width, self.height, (255, 255, 255, 255))
        self.output_image = Image(self.width, self.height, (128, 128, 128, 255))

    def save(self, filename: str) -> None:
        self.output_image.save(filename)

    def _get_random_position(self):
        x = random.randint(1, self.width - 1)
        y = random.randint(1, self.height - 1)
        return x, y

    def _get_random_colour(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def place_random_seed(self):
        x, y = self._get_random_position()
        r, g, b = self._get_random_colour()
        self.sim_data.set_pixel(x, y, (r, g, b, 0))
        self.output_image.set_pixel(x, y, (r, g, b, 255))

    def place_seed(self, x, y):
        r, g, b = self._get_random_colour()
        self.sim_data.set_pixel(x, y, (r, g, b, 0))
        self.output_image.set_pixel(x, y, (r, g, b, 255))

    def walk(self) -> bool:
        walking = True
        found = False
        # loop until we hit the wall or find a seed
        x, y = self._get_random_position()
        while walking:
            move = [-1, 0, 1]
            x += random.choice(move)
            y += random.choice(move)
            # check to see if we hit bounds
            if x < 1 or x >= self.width - 1 or y < 1 or y >= self.height - 1:
                print("hit edge")
                walking = False
                found = False
                break
            else:
                for x_offset in move:
                    for y_offset in move:
                        r, g, b, a = self.sim_data.get_pixel(x + x_offset, y + y_offset)
                        if a == 0:
                            print("found seed")
                            self.sim_data.set_pixel(x, y, (r, g, b, 0))
                            self.output_image.set_pixel(x, y, (r, g, b, 255))
                            found = True
                            walking = False
                            break
                    if found:
                        break

        return found


def main():
    sim = DLA(300, 300)
    for x in range(300):
        sim.place_seed(x, 150)
    frame = 0
    count = 0
    for _ in range(5000):
        if sim.walk():
            count += 1
            if count % 10 == 0:
                sim.save(f"sim.{frame:04}.png")
                frame += 1
    sim.save("test.png")


if __name__ == "__main__":
    main()
