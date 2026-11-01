"""Fit test to print before the real parts.

- Rail slugs: short pieces of the stopper's T profile, each with a different
  side clearance (engraved on top). Try them in the rail and pick the one that
  slides in snugly without play; that value becomes FIT_SLIDE in params.py.
- Drill gauge: guide holes from DRILL + 0.0 to DRILL + 0.4 mm. Pick the one
  your drill bit turns freely in without wobble; the extra becomes
  DRILL_CLEARANCE.

The parts are modelled directly in their print orientation.
"""

from build123d import Align, Compound, Location, Part, Pos, Rot, Text, extrude

from cadkit import present
from cadkit.features import box, vertical_hole
from end_stopper import t_body
from params import DRILL, FIT_SLOT, FIT_SLIDE

SLUG_LENGTH = 10.0
SLIDE_STEPS = [0.15, 0.25, 0.35, 0.45]
DRILL_STEPS = [0.0, 0.1, 0.2, 0.3, 0.4]
ENGRAVE = 0.4


def engrave_top(part: Part, label: str, x: float, y: float, size: float = 3.0) -> Part:
    top = part.bounding_box().max.Z
    text = extrude(Text(label, size, align=(Align.CENTER, Align.CENTER)), ENGRAVE)
    return part - Pos(x, y, top - ENGRAVE) * text


def slug(slide: float) -> Part:
    # Keep the stem's slot clearance at the same offset from the slide clearance as in params.
    s = t_body(SLUG_LENGTH, slide=slide, slot=slide + (FIT_SLOT - FIT_SLIDE))
    s = s.moved(Location((0, 0, 0), (90, 0, 0)))  # stand on end, nose up
    return engrave_top(s, f"{slide:.2f}".lstrip("0"), 0, 4.0, size=2.6)


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
    slugs = [Pos(i * 14.0, 0, 0) * slug(c) for i, c in enumerate(SLIDE_STEPS)]
    gauge = Pos(-7, 12, 0) * drill_gauge()
    return Compound([*slugs, gauge])


if __name__ == "__main__":
    present("fit_test", build(), project="door-handles")
