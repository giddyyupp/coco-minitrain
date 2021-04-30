import time
import os
import copy
import argparse
import pdb
import collections
import sys
import numpy as np

from dataloader import CocoDataset

import matplotlib.pyplot as plt
from random import shuffle

MAX_IMG_COUNT = 25000
RUN_COUNT = 10000000

areaRng = [32 ** 2, 96 ** 2, 1e5 ** 2]


def main(args=None):

	parser     = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')

	parser.add_argument('--dataset', help='Dataset type, must be one of csv or coco.', default="coco")
	parser.add_argument('--coco_path', help='Path to COCO directory', default="/default/path/to/COCO2017/")

	parser = parser.parse_args(args)

	dataset_train = CocoDataset(parser.coco_path, set_name='train2017')

	annot_dict = {}

	for k, v in dataset_train.coco.catToImgs.iteritems():
		# aa = Counter(v)
		annot_dict[k] = len(v)

	print annot_dict

	# fig = plt.figure()
	# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # left, bottom, width, height (range 0 to 1)
	# axes.plot(np.arange(0,80,1), np.divide(annot_dict.values(), float(len(dataset_train.image_ids)) ), 'r')
	# axes.plot(np.arange(0,80,1), np.divide(annot_dict.values(), float(len(dataset_train.image_ids)) ), 'r')
	# axes.set_xlabel('Class Id')
	# axes.set_ylabel('Annot Count')
	# axes.set_title('MiniCoco vs Coco 2017 train set')
	# fig.show()
	# fig.savefig("minicoco_vs_coco_train2017_annot.png")

	# here extract object sizes.
	size_dict = {}

	for k, v in dataset_train.coco.anns.iteritems():
		# aa = Counter(v)
		area = v['bbox'][2] * v['bbox'][3]
		cat = v['category_id']
		if area < areaRng[0]:
			kk = str(cat) + "_S"
		elif area < areaRng[1]:
			kk = str(cat) + "_M"
		else:
			kk = str(cat) + "_L"

		# update counts
		if size_dict.has_key(kk):
			size_dict[kk] += 1
		else:
			size_dict[kk] = 1

	print size_dict

	# now sample!!
	imgs_list = []
	ratio_list = []
	best_run_index = 0
	best_diff = 10000
	keys = []
	# get all keys in coco train set, total image count!
	for k,v in dataset_train.coco.imgToAnns.iteritems():
		keys.append(k)

	for rr in range(RUN_COUNT):
		imgs = {}

		# shuffle keys
		shuffle(keys)

		# select first N image
		for i in keys[:MAX_IMG_COUNT]:
			imgs[i] = dataset_train.coco.imgToAnns[i]

		imgs_list.append(imgs)

		# now check for category based annotations
		# annot_sampled = np.zeros(90, int)
		annot_sampled = {}
		for k,v in imgs.iteritems():
			for it in v:
				area = it['bbox'][2] * it['bbox'][3]
				cat = it['category_id']
				if area < areaRng[0]:
					kk = str(cat) + "_S"
				elif area < areaRng[1]:
					kk = str(cat) + "_M"
				else:
					kk = str(cat) + "_L"

				if annot_sampled.has_key(kk):
					annot_sampled[kk] += 1
				else:
					annot_sampled[kk] = 1

		print annot_sampled

		# calculate ratios
		ratios_obj_count = {}
		ratios_obj_size = {}

		failed_run = False
		for k,v in size_dict.iteritems():
			if not annot_sampled.has_key(k):
				failed_run = True
				break

			ratios_obj_count[k] = annot_sampled[k] / float(v)
		if failed_run:
			continue

		ratio_list.append(ratios_obj_count)

		min_ratio = min(ratios_obj_count.itervalues())
		max_ratio = max(ratios_obj_count.itervalues())

		diff = max_ratio - min_ratio

		if diff < best_diff:
			best_diff = diff
			best_run_index = rr

		print best_diff, best_run_index

	# print imgs_list[best_run_index]

	# now write to csv file
	csv_file = open("mscoco_sampled.csv", 'w')
	write_str = ""

	for k,v in imgs_list[best_run_index].iteritems():
		f_name = dataset_train.coco.imgs[k]['file_name']
		for ann in v:
			bbox = ann['bbox']
			class_id = ann['category_id']
			write_str = f_name+','+str(bbox[0])+','+str(bbox[1])+','+str(bbox[2])+','+str(bbox[3])+','+ \
						str(dataset_train.labels[dataset_train.coco_labels_inverse[class_id]]) + ',' + '0' + '\n'

			csv_file.write(write_str)

	csv_file.close()

	# # max annotations
	# s = 0
	# for key, val in dataset_train.coco.catToImgs.iteritems():
	# 	s += len(val)
	# print s # 604907

	# maxx = 0
	# for key, val in dataset_train.coco.catToImgs.iteritems():
	# 	m = max(val)
	# 	if m > maxx:
	# 		maxx = m
	# print maxx  # 581921


if __name__ == '__main__':
	main()
