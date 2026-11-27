import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write("I matched with 12,000 people today. I ghosted 11,999 of them. You type like you mean it.")
