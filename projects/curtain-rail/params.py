"""Shared numbers for the curtain-rail project (all in mm).

Values marked ESTIMATE are read off the manufacturer's drawing by pixel
measurement and should be checked with calipers; the gauges measure them.
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

# --- Fits (FIT: tune after printing the first stopper) ----------------------
FIT_SLIDE = 0.3  # clearance all around between slider and channel (normal to the surface)
FIT_SLOT = 0.4  # clearance per side between stem and the 6 mm slot; keep > FIT_SLIDE so the
#   stem meets the slider's flat bottom, not its curve (the slider does the locating)

# --- Hardware --------------------------------------------------------------
M3_TAP_DRILL = 2.5  # hole the M3 set screw cuts its own thread into

# --- Space at the rail end ------------------------------------------------
# The gap between the rail's end and the wall is about 15 mm. Every part goes
# in from that end, so none may be longer than this (includes ~2 mm margin).
MAX_PART_LENGTH = 13.0

# --- Stopper ---------------------------------------------------------------
STOPPER_LENGTH = MAX_PART_LENGTH
STOPPER_NOSE_CHAMFER = 0.6
SET_SCREW_LENGTH = 5.0  # M3x5 flat point (DIN 913 / ISO 4026)

# --- Measuring gauges --------------------------------------------------------
# Plain stairs, pushed into the rail end smallest step first. Three gauges per
# dimension cover 15 consecutive sizes in GAUGE_INCREMENT steps, centred on
# the current values above.
GAUGE_INCREMENT = 0.2
GAUGE_STEPS = 5  # steps per gauge
GAUGE_COUNT = 3  # gauges per dimension
GAUGE_STEP_DEPTH = MAX_PART_LENGTH / GAUGE_STEPS  # 2.6
GAUGE_WIDTH_START = 9.2  # wall-to-wall width, 9.2..12.0 (current 2 x 5.3 = 10.6)
GAUGE_SLOT_START = 4.6  # slot width, 4.6..7.4 (nominal 6.0)
GAUGE_HEIGHT_START = 3.6  # rail underside to web underside, 3.6..6.4 (current 4.9;
#   even tenths so every step lands on a 0.2 mm layer line)
