"""End stopper for the curtain rail's lower (glider) channel.

T-shaped slider: a flat body sits inside the channel, a stem passes down
through the 6 mm slot and ends in a bumper below the rail. An M3 set screw
(DIN 913, M3x10) runs up through a captive nut in the bumper. Tightening it
presses the tip against the underside of the web, which pulls the slider
down onto the bottom lips and clamps it in place.

Coordinates match context.rail(): x across, z up from the rail bottom,
the stopper is pushed in along +y (the +y end is the chamfered nose).
"""

from build123d import Axis, Location, Part, chamfer, fillet

from cadkit import present
from cadkit.features import box, hex_nut_slot, vertical_hole
from context import rail, screw
from params import (
    FIT_HEIGHT,
    FIT_SLIDE,
    FIT_SLOT,
    M3_CLEARANCE,
    M3_NUT_AF,
    M3_NUT_HEIGHT,
    RAIL_CHANNEL_HEIGHT,
    RAIL_LIP,
    RAIL_SLOT,
    RAIL_WALL,
    RAIL_WIDTH,
    STOPPER_BUMPER_GAP,
    STOPPER_BUMPER_HEIGHT,
    STOPPER_BUMPER_WIDTH,
    STOPPER_LENGTH,
    STOPPER_NOSE_CHAMFER,
)

BUMPER_TOP = -STOPPER_BUMPER_GAP
BUMPER_BOTTOM = BUMPER_TOP - STOPPER_BUMPER_HEIGHT
SLIDER_TOP = RAIL_LIP + RAIL_CHANNEL_HEIGHT - FIT_HEIGHT
NUT_Z = BUMPER_BOTTOM + 1.6  # bottom of the nut pocket


def t_body(length: float, slide: float = FIT_SLIDE, slot: float = FIT_SLOT) -> Part:
    """Slider + stem + bumper, without screw features. Also used by the fit test."""
    y = (0, length)
    slider_half = RAIL_WIDTH / 2 - RAIL_WALL - slide
    stem_half = RAIL_SLOT / 2 - slot

    slider = box((-slider_half, slider_half), y, (RAIL_LIP, SLIDER_TOP))
    # Lead-in chamfer on the nose so it pushes into the rail easily.
    nose = slider.faces().sort_by(Axis.Y)[-1]
    slider = chamfer(nose.edges(), STOPPER_NOSE_CHAMFER)

    stem = box((-stem_half, stem_half), y, (BUMPER_TOP, RAIL_LIP))

    bumper_half = STOPPER_BUMPER_WIDTH / 2
    bumper = box((-bumper_half, bumper_half), y, (BUMPER_BOTTOM, BUMPER_TOP))
    bumper = fillet(bumper.edges().filter_by(Axis.Y).group_by(Axis.Z)[0], 1.5)

    return slider + stem + bumper


def build() -> Part:
    yc = STOPPER_LENGTH / 2
    part = t_body(STOPPER_LENGTH)
    part -= vertical_hole(0, yc, (BUMPER_BOTTOM - 1, SLIDER_TOP + 1), M3_CLEARANCE)
    part -= hex_nut_slot(
        0, yc, (NUT_Z, NUT_Z + M3_NUT_HEIGHT), M3_NUT_AF, STOPPER_BUMPER_WIDTH
    )
    return part


if __name__ == "__main__":
    stopper = build()

    inset = 5.0  # how far the stopper sits inside the rail end in the preview
    web_z = RAIL_LIP + RAIL_CHANNEL_HEIGHT
    present(
        "end_stopper",
        stopper,
        project="door-handles",
        # Stand it on its back end: the T profile lies flat on the bed, no supports.
        print_orientation=Location((0, 0, 0), (90, 0, 0)),
        context={
            "rail": rail(60).moved(Location((0, -inset, 0))),
            "set_screw_m3x10": screw(0, STOPPER_LENGTH / 2, (web_z - 10, web_z), 3.0),
        },
    )
