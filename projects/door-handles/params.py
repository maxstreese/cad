"""Shared numbers for the door-handles project (all in mm).

Values marked ESTIMATE are read off the manufacturer's drawing by pixel
measurement and must be checked with calipers. Values marked PLACEHOLDER
are guesses until we know the real handles and doors. FIT values get tuned
from the fit test.
"""

# --- Curtain rail (Gardinia profile 4460) ----------------------------------
# Coordinates: x across the rail, z up from the rail's bottom face, rail runs along y.
# The lower (glider) channel has no flat floor: its side walls curve inward into
# the lips that form the 6 mm slot. All inner values are ESTIMATE, traced from
# the manufacturer's drawing at about 17.5 px/mm.
RAIL_WIDTH = 13.0
RAIL_HEIGHT_LEFT = 10.0
RAIL_HEIGHT_RIGHT = 8.8
RAIL_SLOT = 6.0  # opening of the lower (glider) channel
RAIL_INNER_HALF_WIDTH = 5.3  # ESTIMATE centre to the inside of the side walls
RAIL_WEB_BOTTOM = 4.9  # ESTIMATE underside of the web (top of the glider channel)
RAIL_WEB_TOP = 5.9  # ESTIMATE
# ESTIMATE inside of the channel's left half, from the straight wall down
# along the curve to the edge of the slot, as (x, z) points.
RAIL_CHANNEL_CURVE = [(-5.3, 1.9), (-5.0, 1.65), (-4.7, 1.4), (-4.2, 1.2), (-3.4, 0.95), (-3.0, 0.7)]
# ESTIMATE outside of the left lower corner, as (x, z) points (preview only).
RAIL_OUTER_CURVE = [(-6.5, 1.9), (-6.35, 1.4), (-6.1, 0.94), (-5.8, 0.7), (-5.5, 0.47), (-5.1, 0.24), (-4.6, 0.0)]

# --- Fits (FIT: tune with fit_test) ----------------------------------------
FIT_SLIDE = 0.3  # clearance all around between slider and channel (normal to the surface)
FIT_SLOT = 0.4  # clearance per side between stem and the 6 mm slot; keep > FIT_SLIDE so the
#   stem meets the slider's flat bottom, not its curve (the slider does the locating)
DRILL_CLEARANCE = 0.2  # added to the drill diameter for the guide holes

# --- Hardware --------------------------------------------------------------
M3_TAP_DRILL = 2.5  # hole the M3 set screw cuts its own thread into

# --- End stopper -----------------------------------------------------------
STOPPER_LENGTH = 16.0
STOPPER_NOSE_CHAMFER = 0.6
SET_SCREW_LENGTH = 5.0  # M3x5 flat point (DIN 913 / ISO 4026)

# --- Doors and handles -----------------------------------------------------
DOOR_THICKNESS = 19.0  # PLACEHOLDER
HANDLE_SPACING = 96.0  # screw centre distance
HANDLE_EDGE_OFFSET = 28.0  # right edge of door to screw centre line
HANDLE_TOP_OFFSET = 28.0  # top edge of door to the upper screw
DRILL = 5.0  # drill bit for the handle screws

# --- Drill template --------------------------------------------------------
TEMPLATE_PLATE = 4.0  # plate thickness = guide length for the drill
TEMPLATE_FENCE = 4.0  # fence wall thickness
TEMPLATE_FENCE_DEPTH = 15.0  # how far the fences reach down the door edges
TEMPLATE_FENCE_CORNER_GAP = 15.0  # fences end this far before the door corner
TEMPLATE_MARGIN = 15.0  # plate material beyond the outer holes
TEMPLATE_CORNER_RELIEF = 1.5  # groove in the inside corners for rounded door edges
