"""Non-printed geometry shown next to the parts: the rail, a door, screws."""

from build123d import Color, Part

from cadkit.features import box, vertical_hole
from params import (
    DOOR_THICKNESS,
    RAIL_CHANNEL_HEIGHT,
    RAIL_HEIGHT_LEFT,
    RAIL_HEIGHT_RIGHT,
    RAIL_LIP,
    RAIL_SLOT,
    RAIL_WALL,
    RAIL_WEB,
    RAIL_WIDTH,
)

ALUMINIUM = Color(0.75, 0.77, 0.80, 0.45)
WOOD = Color(0.80, 0.66, 0.47, 0.6)
STEEL = Color(0.25, 0.25, 0.28)


def rail(length: float) -> Part:
    """Simplified rail profile, running along +y from y=0. Upper channel is approximate."""
    half = RAIL_WIDTH / 2
    y = (0, length)
    web_z = RAIL_LIP + RAIL_CHANNEL_HEIGHT
    r = (
        box((-half, -half + RAIL_WALL), y, (0, RAIL_HEIGHT_LEFT))  # left wall
        + box((half - RAIL_WALL, half), y, (0, RAIL_HEIGHT_RIGHT))  # right wall
        + box((-half, -RAIL_SLOT / 2), y, (0, RAIL_LIP))  # bottom lips
        + box((RAIL_SLOT / 2, half), y, (0, RAIL_LIP))
        + box((-half, half), y, (web_z, web_z + RAIL_WEB))  # web
        + box((-half + RAIL_WALL, -half + 2.2), y, (8.3, 9.3))  # upper left hook
        + box((half - 3.0, half - RAIL_WALL), y, (RAIL_HEIGHT_RIGHT - 1, RAIL_HEIGHT_RIGHT))
    )
    r.color = ALUMINIUM
    return r


def door_corner(width: float, height: float) -> Part:
    """Top right corner of a door: right edge at x=0, top edge at y=0, face at z=0."""
    d = box((-width, 0), (-height, 0), (-DOOR_THICKNESS, 0))
    d.color = WOOD
    return d


def screw(x: float, y: float, z: tuple[float, float], diameter: float) -> Part:
    s = vertical_hole(x, y, z, diameter)
    s.color = STEEL
    return s
