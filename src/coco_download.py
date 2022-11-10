import os
from pycocotools.coco import COCO
import wget
import concurrent.futures
import argparse
import pathlib

parser = argparse.ArgumentParser(description="Download COCO images")
parser.add_argument(
    "--annotation",
    type=str,
    default="instances_minitrain2017.json",
    help="Json file containing annotations",
)
parser.add_argument(
    "--output_dir", type=str, default="", help="Output file to save images to"
)

args = parser.parse_args()
annotation = args.annotation
root = pathlib.Path().absolute()
ann_file = root / annotation
# assert pathlib.Path(args.output_dir).is_dir(), "not valid dir"
out_p = pathlib.Path(args.output_dir)
out_p.mkdir(parents=True, exist_ok=True)

if not os.fsdecode(ann_file).endswith(".json"):
    assert "Only support COCO style JSON file"

try:
    coco = COCO(os.fsdecode(ann_file))
    img_ids = list(coco.imgs.keys())

except FileNotFoundError:
    raise


def download_images(id):
    try:
        start_url = "http://images.cocodataset.org/train2017"
        filename = "{0:0>12d}".format(id)
        filename = filename + ".jpg"
        full_url = f"{start_url}/{filename}"
        wget.download(full_url, out=args.output_dir)
    except Exception as e:
        print(f"The download exception is {e}", flush=True)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_images, img_ids)
