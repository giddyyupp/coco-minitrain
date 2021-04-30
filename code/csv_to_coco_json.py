import argparse
import json
from dataloader import CocoDataset, CSVDataset


def main(args=None):

	parser     = argparse.ArgumentParser(description='Simple training script for training a RetinaNet network.')

	parser.add_argument('--dataset', help='Dataset type, must be one of csv or coco.', default="coco")
	parser.add_argument('--csv_train', help='Dataset type, must be one of csv or coco.', default="mscoco_sampled_0.1131.csv")
	parser.add_argument('--csv_classes', help='Dataset type, must be one of csv or coco.', default="coco_class_labels.csv")
	parser.add_argument('--coco_path', help='Path to COCO directory',
						default="/default/path/to/COCO2017/")

	parser = parser.parse_args(args)

	dataset_train = CocoDataset(parser.coco_path, set_name='train2017')
	dataset_csv= CSVDataset(train_file=parser.csv_train, class_list=parser.csv_classes)

	keys = []
	# get all keys in coco train set, total image count!
	for k,v in dataset_train.coco.imgToAnns.iteritems():
		keys.append(k)

	main_dict = {}
	annots = []
	imgs = []

	# select first N image
	for i in dataset_csv.image_names:
		im_id = int(i[:-4])
		for ann in dataset_train.coco.imgToAnns[im_id]:
			annots.append(ann)
		imgs.append(dataset_train.coco.imgs[im_id])

	main_dict['images'] = imgs
	main_dict['annotations'] = annots
	main_dict['categories'] = dataset_train.coco.dataset['categories']
	main_dict['info'] = dataset_train.coco.dataset['info']
	main_dict['licenses'] = dataset_train.coco.dataset['licenses']

	# dump to json
	with open('mini_coco_sampled.json', 'w') as fp:
		json.dump(main_dict, fp)

if __name__ == '__main__':
	main()
