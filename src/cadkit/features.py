"""Small geometry helpers shared across projects."""

from build123d import Align, Box, Cylinder, Part, Pos, RegularPolygon, extrude


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
