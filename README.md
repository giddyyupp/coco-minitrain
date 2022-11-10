# COCO `minitrain`

COCO `minitrain` is a curated mini training set (25K images ≈ 20% of `train2017`) for COCO. It is useful for hyperparameter tuning and reducing the cost of ablation experiments. `minitrain`'s object instance statistics match those of `train2017` (see the [stats page](STATS.md)).  `val2017` performance of a model trained on  `minitrain` is strongly positively correlated with the performance of the same model trained on the full set, `train2017` (see the [Performance Correlation](https://github.com/giddyyupp/coco-minitrain#performance-correlation-of-train2017-and-minitrain) section below).

## Reference
We introduced COCO `minitrain` in our ECCV'2020 paper. Please cite it, if you use COCO `minitrain` in your work: 

N. Samet, S. Hicsonmez, E. Akbas, "HoughNet: Integrating near and long-range evidence for bottom-up object detection", ECCV 2020. [arXiv 2007.02355](https://arxiv.org/abs/2007.02355). 

### Bibtex entry
```
@inproceedings{HoughNet, 
  author = {Nermin Samet and Samet Hicsonmez and Emre Akbas},
  title = {HoughNet: Integrating near and long-range evidence for bottom-up object detection},   
  booktitle = {European Conference on Computer Vision (ECCV)}, 
  year = {2020}, 
}
```

## More information

COCO `minitrain` is a subset of the COCO `train2017` dataset, and contains 25K images (about 20% of the `train2017` set) and  around 184K annotations across 80 object categories. We randomly sampled these images from the full set while preserving the following three quantities as much as possible:
* proportion of object instances from each class,
* overall ratios of small, medium and large objects,
* per class ratios of small, medium and large objects.

More information on `minitrain` statistics could be found in [STATS.md](STATS.md).

## Download
We share **COCO** style JSON file, and **Pascal VOC** style CSV file.

[Json](https://drive.google.com/open?id=1lezhgY4M_Ag13w0dEzQ7x_zQ_w0ohjin)

[CSV](https://drive.google.com/open?id=1i12p23cXlqp1QrXjAD_vu467r4q67Mq9) 

[Class Labels](https://drive.google.com/file/d/1xmjxfdnFxZnD1IFpkpj2Yub9Wvv97-Kd/view?usp=sharing) 

Download the whole 25k dataset:

[coco_minitrain_25k.zip](https://drive.google.com/file/d/1t_l9uyBPfxSEzcajTk4a1TaQXzeRm9hw/view?usp=sharing)


## Usage
If you want to sample according to your own needs (e.g. different number of images), run `src/sample_coco.py` with updated parameters.

Below script runs minicoco sampling to curated 25000 images and saves annotations (both **bbox** and **segmentation**) to `instances_train2017_minicoco.json` file.

```bash
cd src
python sample_coco.py --coco_path "path_to_your_coco_dataset" --save_file_name "instances_train2017_minicoco" --save_format "json" --sample_image_count 25000 --debug
```

## Performance correlation of `train2017` and `minitrain`

Object Detector performances. Models are trained on `minitrain` and evaluated on `val2017`:

| Method        | Backbone         | Scale | AP    | AP\_50 | AP\_75 | AP\_S | AP\_M | AP\_L |
|---------------|------------------|-------|-------|--------|--------|-------|-------|-------|
| Faster R\-CNN | ResNet\-50 w FPN | 800   | 27\.7 | 48\.8  | 28\.4  | 14\.7 | 29\.8 | 36\.4 |
| Mask R\-CNN   | ResNet\-50 w FPN | 800   | 28\.5 | 49\.5  | 29\.4  | 14\.7 | 30\.7 | 37\.6 |
| RetinaNet     | ResNet\-50 w FPN | 800   | 25\.7 | 43\.1  | 26\.8  | 12\.1 | 28\.6 | 34\.2 |
| CornerNet     | Hourglass\-104   | 511   | 28\.4 | 41\.8  | 29\.5  | 11\.3 | 29\.6 | 39\.2 |
| ExtremeNet    | Hourglass\-104   | 511   | 27\.3 | 39\.4  | 28\.9  | 12\.5 | 29\.6 | 38\.0 |



Object Detector performances trained on `minitrain` vs `train2017`. Models are evaluated on `val2017`.

| Method        | Backbone         | Scale | minitrain AP    | minitrain AP\_50 | minitrain AP\_75 | train2017 AP | train2017 AP\_50 | train2017 AP\_75 |
|---------------|------------------|-------|-------|--------|--------|-------|-------|-------|
| Faster R\-CNN | ResNet\-50 w FPN | 800   | 27\.7 | 48\.8  | 28\.4  | 36\.7 | 58\.4 | 39\.6 |
| Mask R\-CNN   | ResNet\-50 w FPN | 800   | 28\.5 | 49\.5  | 29\.4  | 37\.7 | 59\.2 | 40\.9 |
| RetinaNet     | ResNet\-50 w FPN | 800   | 25\.7 | 43\.1  | 26\.8  | 35\.7 | 54\.7 | 38\.5 |
| CornerNet     | Hourglass\-104   | 511   | 28\.4 | 41\.8  | 29\.5  | 38\.4 | 53\.8 | 40\.9 |
| ExtremeNet    | Hourglass\-104   | 511   | 27\.3 | 39\.4  | 28\.9  | 40\.3 | 55\.1 | 43\.7 |
| HoughNet      | ResNet\-101      | 512   | 23\.4 | 40\.1  | 23\.6  | 34\.3 | 53\.6 | 36\.6 |


Below figure compares object detection results on `train2017` and `minitrain`. This figure also shows the positive correlation between `train2017` and `minitrain` results. The Pearson correlation coefficients are **0.74** and **0.92** for COCO evaluation metrics *AP* and *AP50* respectively. This figure is based on the table above. *BaseModel* corresponds HoughNet model with ResNet-101 backbone.

<img src="/figures/pearson.png" width="500">
