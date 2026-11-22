from pathlib import Path


ENTRY = (
    "The apron hangs by the kitchen door. In its pocket is a wooden clothespin, "
    "left there when the washing came in. All evening the cloth keeps that small shape."
)

if __name__ == "__main__":
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")
