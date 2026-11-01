"""Fit test to print before the real parts.

- Rail stoppers: four complete mini stoppers, each with a different clearance
  between body and channel. They're too small to engrave, so the clearance is
  coded in the length:

      8 mm -> 0.15    10 mm -> 0.25    12 mm -> 0.35    14 mm -> 0.45

  Try them in the rail and pick the one that slides in snugly without play;
  that value becomes FIT_SLIDE in params.py. Each also has the M3 tap hole,
  so you can check that the set screw cuts a thread that holds.
- Drill gauge: guide holes from DRILL + 0.0 to DRILL + 0.4 mm. Pick the one
  your drill bit turns freely in without wobble; the extra becomes
  DRILL_CLEARANCE.

The parts are placed in their print orientation.
"""

from build123d import Align, Compound, Location, Part, Pos, Text, extrude

from cadkit import present
from cadkit.features import box, vertical_hole
from end_stopper import build as stopper
from params import DRILL, FIT_SLIDE, FIT_SLOT

SLIDE_STEPS = {0.15: 8.0, 0.25: 10.0, 0.35: 12.0, 0.45: 14.0}  # clearance -> length
DRILL_STEPS = [0.0, 0.1, 0.2, 0.3, 0.4]
ENGRAVE = 0.4


def engrave_top(part: Part, label: str, x: float, y: float, size: float = 3.0) -> Part:
    top = part.bounding_box().max.Z
    text = extrude(Text(label, size, align=(Align.CENTER, Align.CENTER)), ENGRAVE)
    return part - Pos(x, y, top - ENGRAVE) * text


def mini_stopper(slide: float, length: float) -> Part:
    # Keep the stem's slot clearance at the same offset from the slide clearance as in params.
    s = stopper(length, slide=slide, slot=slide + (FIT_SLOT - FIT_SLIDE))
    s = s.moved(Location((0, 0, 0), (180, 0, 0)))  # same orientation as the real stopper
    bb = s.bounding_box()
    return s.moved(Location((-bb.center().X, -bb.min.Y, -bb.min.Z)))


def drill_gauge() -> Part:
    pitch = 12.0
    width = pitch * len(DRILL_STEPS)
    plate = box((0, width), (0, 16), (0, 5))
    for i, extra in enumerate(DRILL_STEPS):
        x = pitch * (i + 0.5)
        plate -= vertical_hole(x, 5, (-1, 6), DRILL + extra)
        plate = engrave_top(plate, f"+{extra:.1f}", x, 12.5, size=3)
    return plate


def build() -> Compound:
    stoppers = [
        Pos(i * 14.0, 0, 0) * mini_stopper(slide, length)
        for i, (slide, length) in enumerate(SLIDE_STEPS.items())
    ]
    gauge = Pos(-7, 18, 0) * drill_gauge()
    return Compound([*stoppers, gauge])


if __name__ == "__main__":
    present("fit_test", build(), project="door-handles")
