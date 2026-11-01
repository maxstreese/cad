"""Shared numbers for the door-handles project (all in mm).

Values marked ESTIMATE are read off the manufacturer's drawing by pixel
measurement and must be checked with calipers. Values marked PLACEHOLDER
are guesses until we know the real handles and doors. FIT values get tuned
from the fit test.
"""

# --- Curtain rail (Gardinia profile 4460) ----------------------------------
# Coordinates: x across the rail, z up from the rail's bottom face, rail runs along y.
RAIL_WIDTH = 13.0
RAIL_HEIGHT_LEFT = 10.0
RAIL_HEIGHT_RIGHT = 8.8
RAIL_SLOT = 6.0  # opening of the lower (glider) channel
RAIL_WALL = 1.0  # ESTIMATE side wall thickness
RAIL_LIP = 1.0  # ESTIMATE bottom lip thickness
RAIL_CHANNEL_HEIGHT = 3.3  # ESTIMATE lip top to underside of the web
RAIL_WEB = 0.8  # ESTIMATE

# --- Fits (FIT: tune with fit_test) ----------------------------------------
FIT_SLIDE = 0.3  # clearance per side between slider and rail side walls
FIT_HEIGHT = 0.4  # total vertical clearance of the slider in the channel
FIT_SLOT = 0.25  # clearance per side between stem and the 6 mm slot
DRILL_CLEARANCE = 0.2  # added to the drill diameter for the guide holes

# --- Hardware --------------------------------------------------------------
M3_CLEARANCE = 3.4
M3_NUT_AF = 5.5 + 0.3  # across flats plus printing allowance
M3_NUT_HEIGHT = 2.4 + 0.3

# --- End stopper -----------------------------------------------------------
STOPPER_LENGTH = 16.0
STOPPER_BUMPER_WIDTH = 10.0
STOPPER_BUMPER_HEIGHT = 7.0
STOPPER_BUMPER_GAP = 0.5  # gap between bumper top and rail bottom
STOPPER_NOSE_CHAMFER = 0.6

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
