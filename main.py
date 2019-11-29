# import yolov3.detect as yolov3_demo
import os
import argparse
def main():
    model_list = ['faster-rcnn', 'faster-rcnn', 'faster-rcnn', 'faster-rcnn', 'ssd', 'ssd', 'ssd', 'ssd', 'yolo']
    backbone_list = ['inception_resnet_v2', 'resnet101', 'inception_resnet_v2+atrous', 'resnext', 'vggnet16', 'resnet101', 'inception-v2', 'mobilenet', 'darknet53']
    backbone_list2 = ['inception_resnet_v2', 'resnet101', 'inception_resnet_v2', 'resnext', 'vggnet', 'resnet', 'googlenet', 'mobilenet', 'darknet']
    parser = argparse.ArgumentParser()
    # parser.add_argument('-model', default='ssd', help='Detection Model, ssd/yolov3/all')
    # parser.add_argument('-backbone', default='resnet', help='Detection Model, ssd/yolov3/all')
    parser.add_argument('-mode', default='demo', help='Mode, train/demo')
    parser.add_argument('-image', default='imgs/messi.jpg', help='input image name')
    parser.add_argument('-save', default='save_dir', help='save dir')

    parse = parser.parse_args()
    for i in range(len(model_list)):
        print(" - {} [detector] {} [backbone] {} ".format(i, model_list[i], backbone_list[i]))
    print("select number : ")
    num = int(input())
    parse.model = model_list[num]
    parse.backbone = backbone_list2[num]
    print("[Info] -detector: {} -backbone: {} ".format(parse.model, parse.backbone))
    parse.mode = parse.mode.lower()

    if parse.model == 'ssd':
        os.chdir('ssd')
        if parse.mode == 'demo':
            os.system('python -W ignore::UserWarning  detect.py --images ../{} --det ../{} --backbone {}'.format(parse.image, parse.save, parse.backbone))
        elif parse.mode == 'train':
            os.system('python -W ignore::UserWarning train.py --backbone {}'.format(parse.backbone))
        os.chdir('..')
    elif parse.model == 'faster-rcnn':
        os.chdir('easy-faster-rcnn.pytorch')
        if parse.mode == 'demo':
            os.system('python -W ignore::UserWarning infer.py --backbone {} ../{} ../{} '.format(parse.backbone, parse.image, parse.save))
        elif parse.mode == 'train':
            os.system('python -W ignore::UserWarning train.py --backbone {}'.format(parse.backbone))
        os.chdir('..')

    elif parse.model == 'yolov3':
        os.chdir('yolov3')
        if parse.mode == 'demo':
            os.system('python -W ignore::UserWarning  detect.py --images ../{} --det ../{}'.format(parse.image, parse.save))
        os.chdir('..')

if __name__ == '__main__':
    main()
