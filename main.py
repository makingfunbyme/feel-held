from pathlib import Path


ENTRY = (
    "The apron hangs by the kitchen door. A wooden clothespin lies sideways in "
    "the pocket. The light is low enough to show the ridge it makes in the cloth."
)

if __name__ == "__main__":
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")
