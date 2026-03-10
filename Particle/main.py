from Emitter import Emitter
from Vec3 import Vec3


def main():
    e = Emitter(Vec3(0, 1, 0), 10)
    e.render()


if __name__ == "__main__":
    main()
