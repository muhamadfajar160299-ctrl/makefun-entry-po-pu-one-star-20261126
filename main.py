"""One Star, Five Stars for the Food: write the alien review to the output dir."""

import os

ENTRY = "One star: your gravity bruised my knees, your weather lied twice, and your leaders argue with their ovens — but the rendang was so good I have filed to extend my abduction."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
