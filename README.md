# COCO `minitrain`

COCO `minitrain` dataset home page.

It is a subset of the COCO `train2017` dataset, and contains 25K images (about 20% of the `train2017` set) and  around 184K annotations across 80 object categories. We randomly sampled these images from the full set while preserving the following three quantities as much as possible:
* proportion of object instances from each class,
* overall ratios of small, medium and large objects,
* per class ratios of small, medium and large objects.

## Download
We share **COCO** style JSON file, and **Pascal VOC** style CSV file.

[Json](https://drive.google.com/open?id=1lezhgY4M_Ag13w0dEzQ7x_zQ_w0ohjin)

[CSV](https://drive.google.com/open?id=1i12p23cXlqp1QrXjAD_vu467r4q67Mq9) [Class Labels](https://drive.google.com/file/d/1xmjxfdnFxZnD1IFpkpj2Yub9Wvv97-Kd/view?usp=sharing) 

## Object Detector Performances

We trained popular object detectors with `minitrain` dataset. We present the results in below figures.

Object Detector performances. Models are trained on `minitrain` and evaluated on `val2017`:

<img src="/figures/minicoco_det.png" width="500">


Object Detector performances trained `minitrain` vs `train2017`. Models are evaluated on `val2017`.

<img src="/figures/minicoco_det_compare.png" width="500">


## Correlation between `train2017` and `minitrain`

Below figure compares object detection results on `train2017` and `minitrain`. This figure also shows the positive correlation between `train2017` and `minitrain` results. The Pearson correlation coefficients are **0.74** and **0.92** for COCO evaluation metrics *AP* and *AP50* respectively. This figure is based on the table above. *BaseModel* corresponds HoughNet model with ResNet-101 backbone.

<img src="/figures/pearson.png" width="500">

More information on `minitrain` statistics could be found in [STATS.md](STATS.md)

## Citation

If you use COCO `minitrain` in your research, please cite as following:
