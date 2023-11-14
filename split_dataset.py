import shutil
from pathlib import Path

input_dir = Path("images")
output_train_dir = Path("training")
output_valid_dir = Path("validation")

output_train_dir.mkdir(parents=True, exist_ok=True)
output_valid_dir.mkdir(parents=True, exist_ok=True)

for subdir in input_dir.iterdir():
    if subdir.is_dir():
        train_subdir = output_train_dir / subdir.name
        valid_subdir = output_valid_dir / subdir.name

        train_subdir.mkdir(parents=True, exist_ok=True)
        valid_subdir.mkdir(parents=True, exist_ok=True)

        images = sorted(
            subdir.glob("image (*).JPG"),
            key=lambda x: int(x.stem.split(" ")[1].strip("()")),
        )
        validation_images = images[:25]
        training_images = images[25:]

        for img in training_images:
            shutil.copy(str(img), str(train_subdir / img.name))
        for img in validation_images:
            shutil.copy(str(img), str(valid_subdir / img.name))
