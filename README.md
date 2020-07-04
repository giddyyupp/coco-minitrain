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

We trained popular object detectors on Mini COCO dataset. We present object detection results in below figures.

Object Detector performances on `minitrain`:

![obj_det_minicoco](/figures/minicoco_det.png)


Object Detector performances `minitrain` vs `train2017`:

![obj_det_minicoco](/figures/minicoco_det_compare.png)

## Correlation between `train2017` and `minitrain`

Below figure compares object detection results on `train2017` and `minitrain`. This figure also shows the positive correlation between `train2017` and `minitrain` results. The Pearson correlation coefficients are **0.74** and **0.92** for COCO evaluation metrics *AP* and *AP50* respectively.

<img src="/figures/pearson.png" width="500">

More information on `minitrain` statistics could be found in [STATS.md](STATS.md)


| \\multirow\{2\}\{\*\}\{Method\}       | \\multirow\{2\}\{\*\}\{Backbone\} | \\multirow\{2\}\{\*\}\{Scale\} | \\multicolumn\{3\}\{c\}\{MiniCOCO\} | \\multicolumn\{3\}\{c\}\{COCO\} |
|---------------------------------------|-----------------------------------|--------------------------------|-------------------------------------|---------------------------------|
|                                       |                                   |                                | \\textit\{AP\}                      | \\textit\{AP$\_\{50\}$\}        | \\textit\{AP$\_\{75\}$\} | \\textit\{AP\} | \\textit\{AP$\_\{50\}$\} | \\textit\{AP$\_\{75\}$\} |
| \\textit\{Two\-stage detectors:\}     |                                   |                                |                                     |                                 |                          |                |                          |                          |
| Faster R\-CNN~\\cite\{Detectron2018\} | ResNet\-50 \\textit\{w\} FPN      |
|                                       | 800                               | 27\.7                          | 48\.8                               | 28\.4                           | 36\.7                    | 58\.4          | 39\.6                    |
| Mask R\-CNN~\\cite\{Detectron2018\}   | ResNet\-50 \\textit\{w\} FPN      | 800                            | 28\.5                               | 49\.5                           | 29\.4                    | 37\.7          | 59\.2                    | 40\.9                    |
| % Mask\-R\-50\-FPN                    | ResNet\-50 w FPN                  | 800                            | Seg                                 | 26\.7                           | 46\.0                    | 27\.4          | 10\.5                    | 28\.6                    | 40\.4 |
| \\textit\{One\-stage detectors:\}     |                                   |                                |                                     |                                 |                          |                |                          |                          |
| RetinaNet~\\cite\{Detectron2018\}     | ResNet\-50 \\textit\{w\} FPN      | 800                            | 25\.7                               | 43\.1                           | 26\.8                    | 35\.7          | 54\.7                    | 38\.5                    |
| % YOLOv3                              | Darknet\-53                       | 608                            | 20\.6                               | 38\.2                           | 20\.3                    | 8\.7           | 21\.9                    | 28\.6                    |
| CornerNet~\\cite\{cornernet\}         | Hourglass\-104                    | 511                            | 28\.4                               | 41\.8                           | 29\.5                    | 38\.4          | 53\.8                    | 40\.9                    |
| ExtremeNet~\\cite\{extremenet\}       | Hourglass\-104                    | 511                            | 27\.3                               | 39\.4                           | 28\.9                    | 40\.3          | 55\.1                    | 43\.7                    |
| HoughNet \(ours\)                     | ResNet\-101                       | 512                            | 23\.4                               | 40\.1                           | 23\.6                    | 34\.3          | 53\.6                    | 36\.6                    |
| %  DCN                                | ResNet\-101 \\textit\{w\} DCN     | 512                            | 24\.7                               | 41\.3                           | 25\.5                    | 7\.6           | 26\.8                    | 38\.0                    |

