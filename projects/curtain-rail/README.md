# curtain-rail

Stopper for a curtain rail (Gardinia profile 4460). It sits entirely inside the
lower (glider) channel and is clamped anywhere along the rail with a set screw.

| Part | What it does |
|---|---|
| `stopper` | The stopper: follows the channel's rounded bottom, clamped by an M3 set screw pressing against the web |
| `fit_test` | Four mini stoppers with different clearances, coded by length: 8 mm = 0.15, 10 mm = 0.25, 12 mm = 0.35, 14 mm = 0.45. Print first and pick the one that slides in snugly |

Status: **draft**. The channel's inner shape is traced from the manufacturer's
drawing (see `params.py`), so print the fit test first.

## Hardware

- 1x M3x5 set screw, flat point (DIN 913 / ISO 4026), per stopper. It cuts its
  own thread into the plastic: screw it fully in and out once on the bench
  before inserting the stopper into the rail. Tighten with a 1.5 mm hex key
  through the slot, snug only.

## Print sheet (suggestion)

Print each part in the orientation it comes in the 3MF (flat top on the bed);
no supports needed.

| | |
|---|---|
| Material | PETG (or PLA) |
| Layer height | 0.2 mm or finer |
| Walls | 4 |
| Infill | 100 % (the parts are tiny; solid gives the screw thread the most grip) |
| Supports | none |
