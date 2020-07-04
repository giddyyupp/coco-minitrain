# COCO minitrain

COCO minitrain dataset home page.

It is a subset of the COCO train2017 dataset, and contains 25K images (about 20% of the COCO train2017 set) and  around 184K annotations across 80 object categories. We randomly sampled these images from the full set while preserving the following three quantities as much as possible:
* proportion of object instances from each class,
* overall ratios of small, medium and large objects,
* per class ratios of small, medium and large objects.

## Download
We share **COCO** style JSON file, and **Pascal VOC** style CSV file.

[Json](https://drive.google.com/open?id=1lezhgY4M_Ag13w0dEzQ7x_zQ_w0ohjin)

[CSV](https://drive.google.com/open?id=1i12p23cXlqp1QrXjAD_vu467r4q67Mq9)

## Object Detector Performances

We trained popular object detectors on Mini COCO dataset. We present object detection results in below figures.

Object Detector performances on COCO minitrain:

![obj_det_minicoco](/figures/minicoco_det.png)


Object Detector performances COCO minitrain vs COCO train2017:

![obj_det_minicoco](/figures/minicoco_det_compare.png)

## Correlation between COCO train and COCO minitrain

Below figure compares object detection results on *COCO train2017* and *COCO minitrain*. This figure also shows the positive correlation between *COCO train2017* and *COCO minitrain* results. The Pearson correlation coefficients are **0.74** and **0.92** for COCO evaluation metrics *AP* and *AP50* respectively.

<img src="/figures/pearson.png" width="600"> 

More information on COCO minitrain statistics could be found in [STATS.md](STATS.md)


