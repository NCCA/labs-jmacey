from Emitter import Emitter
from Vec3 import Vec3
from pathlib import Path

OUTPUT_DIR = "/transfer/Particles"
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def main():
    e = Emitter(Vec3(0, 0, 0), 50000)
    for i in range(200):
        e.write_geo(f"{OUTPUT_DIR}/Particle.{i:04}.geo")
        e.update(0.01)


if __name__ == "__main__":
    main()
