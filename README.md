# COCO `minitrain`

COCO `minitrain` is a mini training set (25K images ≈ 20% of `train2017`) for COCO. It is useful for hyperparameter tuning and reducing the cost of ablation experiments. `minitrain`s object instance statistics match those of `train2017` (see the [stats page](STATS.md)).  \texttt{val2017} performance of a model trained on  \texttt{minitrain} is strongly positively correlated with the performance of the same model trained on the full set, \texttt{train2017} (see the Performance Correlation section below).

We introduced COCO `minitrain` in our HoughNet paper in ECCV'2020. Please cite our paper, if you use COCO `minitrain` in your work. 

N. Samet, S. Hicsonmez, E. Akbas, "HoughNet: Integrating near and long-range evidence for bottom-up object detection", ECCV 2020. [arXiV pre-print](buraya arxiv linki). 

```
@inproceedings{HoughNet, 
  authors = {Nermin Samet and Samet Hicsonmez and Emre Akbas},
  title = {HoughNet: Integrating near and long-range evidence for bottom-up object detection}, 
  date = 2020, 
  booktitle = {European Conference on Computer Vision (ECCV)}
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

[CSV](https://drive.google.com/open?id=1i12p23cXlqp1QrXjAD_vu467r4q67Mq9) [Class Labels](https://drive.google.com/file/d/1xmjxfdnFxZnD1IFpkpj2Yub9Wvv97-Kd/view?usp=sharing) 

## Object Detector Performances

We trained popular object detectors on `minitrain`. We present the results in below.

Object Detector performances. Models are trained on `minitrain` and evaluated on `val2017`:

<img src="/figures/minicoco_det.png" width="500">


Object Detector performances trained on `minitrain` vs `train2017`. Models are evaluated on `val2017`.

<img src="/figures/minicoco_det_compare.png" width="500">


## Performance correlation of `train2017` and `minitrain`

Below figure compares object detection results on `train2017` and `minitrain`. This figure also shows the positive correlation between `train2017` and `minitrain` results. The Pearson correlation coefficients are **0.74** and **0.92** for COCO evaluation metrics *AP* and *AP50* respectively. This figure is based on the table above. *BaseModel* corresponds HoughNet model with ResNet-101 backbone.

<img src="/figures/pearson.png" width="500">
