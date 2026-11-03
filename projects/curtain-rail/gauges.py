"""Stepped gauges (plain stairs) that measure the rail.

Each gauge is a stair of five steps, each step GAUGE_INCREMENT bigger than
the one before. Hold it against the rail end, smallest step first, and push it
in until it stops; the last step that went in is the measurement (the true
value lies between it and the next step).

Three kinds, told apart by shape:

    gauge_width   wide flat stair   width between the channel's straight walls
    gauge_slot    narrow flat stair width of the 6 mm slot
    gauge_height  tall stair        rail underside up to the web's underside
                                    (hold its bottom flush with the rail's underside)

Each kind comes as three stairs covering 15 consecutive sizes. Gauge g has
g small dimples in its right side wall, one each on its g back (largest)
steps, so gauge 1 has one dimple and the smallest sizes. Side by side, gauge
g+1 starts where gauge g ends. Step n (counted from the front, starting at 1) of gauge g measures

    start + ((g - 1) * 5 + n - 1) * 0.2

Every gauge is MAX_PART_LENGTH long, so it fits in the gap at the rail end.
The parts are laid out in their print orientation (flat side down).
"""

from build123d import Compound, Cylinder, Part, Pos, Rot

from cadkit import present
from cadkit.features import box
from params import (
    GAUGE_COUNT,
    GAUGE_HEIGHT_START,
    GAUGE_INCREMENT,
    GAUGE_SLOT_START,
    GAUGE_STEP_DEPTH,
    GAUGE_STEPS,
    GAUGE_WIDTH_START,
)

FLAT_THICKNESS = 1.5  # width and slot stairs
HEIGHT_STAIR_WIDTH = 4.0  # narrower than the narrowest slot the slot gauge allows
GAP = 3.0  # between gauges on the print bed
DIMPLE_DIAMETER = 0.8  # fits the 1.5 mm side wall of the flat stairs
DIMPLE_DEPTH = 0.5

# Coordinates: x across, z up, y along the rail. The stair runs from y = 0
# (largest step, held in the hand) to the front (smallest step).


def _sizes(start: float, gauge: int) -> list[float]:
    """Step sizes of gauge 1..GAUGE_COUNT, back (largest) to front (smallest)."""
    first = start + (gauge - 1) * GAUGE_STEPS * GAUGE_INCREMENT
    sizes = [round(first + i * GAUGE_INCREMENT, 3) for i in range(GAUGE_STEPS)]
    return sizes[::-1]


def _stair(gauge: int, steps: list[tuple[float, float]]) -> Part:
    """Stair from (width, height) per step, back to front, each centred on x = 0.

    A side wall is only 2.6 mm long, too short for three dimples, so gauge g
    gets one dimple in the +x side wall of each of its g back steps, all at the
    flat stairs' mid-height so the three kinds look the same.
    """
    part = Part()
    for i, (w, h) in enumerate(steps):
        part += box((-w / 2, w / 2), (i * GAUGE_STEP_DEPTH, (i + 1) * GAUGE_STEP_DEPTH), (0, h))
    for i in range(gauge):
        wall_x = steps[i][0] / 2
        dimple = Rot(0, 90, 0) * Cylinder(DIMPLE_DIAMETER / 2, 2 * DIMPLE_DEPTH)  # axis along x
        part -= Pos(wall_x, (i + 0.5) * GAUGE_STEP_DEPTH, FLAT_THICKNESS / 2) * dimple
    return part


def width_gauge(gauge: int) -> Part:
    return _stair(gauge, [(w, FLAT_THICKNESS) for w in _sizes(GAUGE_WIDTH_START, gauge)])


def slot_gauge(gauge: int) -> Part:
    return _stair(gauge, [(w, FLAT_THICKNESS) for w in _sizes(GAUGE_SLOT_START, gauge)])


def height_gauge(gauge: int) -> Part:
    return _stair(gauge, [(HEIGHT_STAIR_WIDTH, h) for h in _sizes(GAUGE_HEIGHT_START, gauge)])


def layout(parts: list[Part]) -> Compound:
    """Side by side along x, all with their lowest point on z = 0."""
    placed, x = [], 0.0
    for p in parts:
        bb = p.bounding_box()
        placed.append(Pos(x - bb.min.X, 0, -bb.min.Z) * p)
        x += bb.size.X + GAP
    return Compound(placed)


GAUGES = {"gauge_width": width_gauge, "gauge_slot": slot_gauge, "gauge_height": height_gauge}

if __name__ == "__main__":
    for name, make in GAUGES.items():
        parts = [make(g) for g in range(1, GAUGE_COUNT + 1)]
        present(name, layout(parts), project="curtain-rail")
