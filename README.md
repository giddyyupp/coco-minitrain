# COCO minitrain

COCO minitrain dataset home page.

It is a subset of the COCO train2017 351 dataset, contains 25K images (about 20% of the COCO train2017 set) and  around 184K ob jects across 80 ob ject categories. We randomly sampled these images from the full set while preserving the following three quantities as much as possible: 
* proportion of object instances from each class, 
* overall ratios  of small, medium and large objects, 
* per class ratios of small, medium and large objects.

## Download
We share COCO style json file, and Pascal style csv file.

[Json](https://drive.google.com/open?id=1lezhgY4M_Ag13w0dEzQ7x_zQ_w0ohjin)

[CSV](https://drive.google.com/open?id=1i12p23cXlqp1QrXjAD_vu467r4q67Mq9)

## Object Detector Performances
We trained popular object detectors on Mini COCO dataset. Below we display results.

Object Detector performances on Mini COCO:

![obj_det_minicoco](/figures/minicoco_det.png)


Object Detector performances Mini COCO vs COCO:

![obj_det_minicoco](/figures/minicoco_det_compare.png)


