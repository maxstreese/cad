"""Stopper for the curtain rail's lower (glider) channel, entirely inside the rail.

The body follows the channel's cross-section, including its rounded bottom,
shrunk by the fit clearance all around. A short stem fills the 6 mm slot up
to the rail's underside. An M3x5 set screw (flat point) threads straight
into a 2.5 mm hole in the plastic and is reached from below through the slot
with a 1.5 mm hex key. Tightening it presses the tip against the underside
of the web; the reaction pushes the body down into the rounded bottom of the
channel, which centres it and clamps it along the whole curve. Since nothing
sticks out, it can be clamped anywhere along the rail.

Coordinates match context.rail(): x across, z up from the rail bottom,
the stopper is pushed in along +y (the +y end is the tapered nose).
"""

from build123d import Location, Part, offset

from cadkit import present
from cadkit.features import box, loft_profiles, vertical_hole
from context import channel_cavity, rail, screw
from params import (
    FIT_SLIDE,
    FIT_SLOT,
    M3_TAP_DRILL,
    RAIL_SLOT,
    RAIL_WEB_BOTTOM,
    SET_SCREW_LENGTH,
    STOPPER_LENGTH,
    STOPPER_NOSE_CHAMFER,
)


def build(length: float = STOPPER_LENGTH, slide: float = FIT_SLIDE, slot: float = FIT_SLOT) -> Part:
    """The stopper; `length` and the clearances can be overridden."""
    # Body = channel cross-section shrunk by the clearance all around, with a
    # 45 degree lead-in taper on the nose so it pushes into the rail easily.
    profile = offset(channel_cavity(), -slide)
    nose_profile = offset(channel_cavity(), -slide - STOPPER_NOSE_CHAMFER)
    nose_start = length - STOPPER_NOSE_CHAMFER
    body = loft_profiles([(0, profile), (nose_start, profile), (length, nose_profile)])

    # Stem in the slot. Its bottom sits `slide` above the rail's underside, so it
    # ends up flush once the screw has pushed the body down into its seat. It
    # stops where the nose taper starts, so it never pokes out through the taper.
    stem_half = RAIL_SLOT / 2 - slot
    stem = box((-stem_half, stem_half), (0, nose_start), (slide, 2.0))

    part = body + stem
    part -= vertical_hole(0, length / 2, (0, RAIL_WEB_BOTTOM), M3_TAP_DRILL)
    return part


if __name__ == "__main__":
    stopper = build()
    inset = 5.0  # how far the stopper sits inside the rail in the preview
    present(
        "stopper",
        stopper,
        project="curtain-rail",
        # Upside down: the flat top on the bed, the rounded bottom facing up
        # (no overhangs), and the screw hole printed vertically for good threads.
        print_orientation=Location((0, 0, 0), (180, 0, 0)),
        context={
            "rail": rail(60).moved(Location((0, -inset, 0))),
            "set_screw_m3x5": screw(
                0, STOPPER_LENGTH / 2, (RAIL_WEB_BOTTOM - SET_SCREW_LENGTH, RAIL_WEB_BOTTOM), 3.0
            ),
        },
    )
