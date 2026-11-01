"""Fit test to print before the real stoppers.

Four complete mini stoppers, each with a different clearance between body
and channel. They're too small to engrave, so the clearance is coded in the
length:

    8 mm -> 0.15    10 mm -> 0.25    12 mm -> 0.35    14 mm -> 0.45

Try them in the rail and pick the one that slides in snugly without play;
that value becomes FIT_SLIDE in params.py. Each also has the M3 tap hole, so
you can check that the set screw cuts a thread that holds. The best one can
stay in the rail as a working stopper.

The parts are placed in their print orientation.
"""

from build123d import Compound, Location, Part, Pos

from cadkit import present
from params import FIT_SLIDE, FIT_SLOT
from stopper import build as stopper

SLIDE_STEPS = {0.15: 8.0, 0.25: 10.0, 0.35: 12.0, 0.45: 14.0}  # clearance -> length


def mini_stopper(slide: float, length: float) -> Part:
    # Keep the stem's slot clearance at the same offset from the slide clearance as in params.
    s = stopper(length, slide=slide, slot=slide + (FIT_SLOT - FIT_SLIDE))
    s = s.moved(Location((0, 0, 0), (180, 0, 0)))  # same orientation as the real stopper
    bb = s.bounding_box()
    return s.moved(Location((-bb.center().X, -bb.min.Y, -bb.min.Z)))


def build() -> Compound:
    stoppers = [
        Pos(i * 14.0, 0, 0) * mini_stopper(slide, length)
        for i, (slide, length) in enumerate(SLIDE_STEPS.items())
    ]
    return Compound(stoppers)


if __name__ == "__main__":
    present("fit_test", build(), project="curtain-rail")
