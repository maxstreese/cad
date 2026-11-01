"""Show a part in Yet Another CAD Viewer and export it for printing.

Every part script ends with a call to `present`. It

- exports the printable part to out/<project>/<name>.{step,3mf,stl}, with the
  3MF/STL already rotated into the intended print orientation, and
- shows the part (in its use position) together with optional context
  geometry, e.g. the rail or the door, in the viewer at http://localhost:32323.

Set YACV_DISABLE_SERVER=1 to only export (the `mise run build` task does this).
"""

import os
from pathlib import Path

from build123d import Location, Mesher, Shape, export_step, export_stl

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "out"


def present(
    name: str,
    part: Shape,
    *,
    project: str,
    print_orientation: Location = Location(),
    context: dict[str, Shape] | None = None,
) -> None:
    """Export `part` and show it with its `context` in the viewer.

    `print_orientation` is applied to the 3MF/STL only; the STEP file and the
    viewer keep the part in its use position.
    """
    context = context or {}

    out = OUT_DIR / project
    out.mkdir(parents=True, exist_ok=True)

    export_step(part, out / f"{name}.step")

    printable = part.moved(print_orientation)
    bb = printable.bounding_box()
    printable = printable.moved(Location((-bb.center().X, -bb.center().Y, -bb.min.Z)))

    mesher = Mesher()
    mesher.add_shape(printable, part_number=name)
    mesher.write(str(out / f"{name}.3mf"))
    export_stl(printable, out / f"{name}.stl")

    size = part.bounding_box().size
    print(
        f"{name}: {size.X:.2f} x {size.Y:.2f} x {size.Z:.2f} mm, "
        f"volume {part.volume / 1000:.2f} cm3 -> {out.relative_to(REPO_ROOT)}/"
    )

    if os.environ.get("YACV_DISABLE_SERVER"):
        return

    from yacv_server import show

    shapes = [part, *context.values()]
    names = [name, *context.keys()]
    show(*shapes, names=names)
    print("Viewer: http://localhost:32323 (keep the tab open; re-run to update)")
