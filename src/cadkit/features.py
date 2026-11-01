"""Small geometry helpers shared across projects."""

from build123d import (
    Align,
    Box,
    Cylinder,
    Face,
    Location,
    Part,
    Pos,
    RegularPolygon,
    Rot,
    Sketch,
    extrude,
    loft,
)

# Cross-section profiles are drawn in the XY plane and read as (x, z), as seen
# looking along -y (from the +y end back). The helpers below run them along +y.


def extrude_profile(profile: Face | Sketch, y: tuple[float, float]) -> Part:
    """Extrude a cross-section profile along +y from y[0] to y[1]."""
    return _along_y(extrude(profile, y[1] - y[0]), y[0])


def loft_profiles(sections: list[tuple[float, Face | Sketch]]) -> Part:
    """Ruled loft through cross-section profiles placed at increasing y values.

    E.g. [(0, p), (9.4, p), (10, p_shrunk)] gives a straight body with a lead-in
    taper on its +y end, as one solid. Building it in one piece instead of
    unioning an extrusion and a taper avoids invalid seams on curved profiles.
    """
    y0 = sections[0][0]
    faces = [Pos(0, 0, y - y0) * profile.faces()[0] for y, profile in sections]
    return _along_y(loft(faces, ruled=True), y0)


def _along_y(solid: Part, y0: float) -> Part:
    """Map a solid built along +Z from z=0 onto world +y from y0 (drawing y -> world z)."""
    # Rot X +90: (x, y, z) -> (x, -z, y); then Rot Z 180: -> (-x, z, y).
    return Pos(0, y0, 0) * Rot(0, 0, 180) * Rot(90, 0, 0) * solid


def box(x: tuple[float, float], y: tuple[float, float], z: tuple[float, float]) -> Part:
    """Axis-aligned box given by its (min, max) extent on each axis."""
    return Pos(sum(x) / 2, sum(y) / 2, sum(z) / 2) * Box(x[1] - x[0], y[1] - y[0], z[1] - z[0])


def vertical_hole(x: float, y: float, z: tuple[float, float], diameter: float) -> Part:
    """Cylinder along Z from z[0] to z[1], to be subtracted from a part."""
    return Pos(x, y, z[0]) * Cylinder(
        diameter / 2, z[1] - z[0], align=(Align.CENTER, Align.CENTER, Align.MIN)
    )


def hex_nut_slot(
    x: float, y: float, z: tuple[float, float], across_flats: float, open_to_x: float
) -> Part:
    """Hex pocket (axis along Z, flats facing +/-Y) with a slot running in +X up to `open_to_x`.

    The nut is pushed in sideways from the +X face and is then captive along Z.
    """
    height = z[1] - z[0]
    hexagon = Pos(x, y, z[0]) * extrude(
        RegularPolygon(across_flats / 2, 6, major_radius=False), height
    )
    slot = box((x, open_to_x), (y - across_flats / 2, y + across_flats / 2), z)
    return hexagon + slot
