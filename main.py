# import yolov3.detect as yolov3_demo
import os
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', required=True, help='Detection Model, ssd/yolov3')
    parser.add_argument('-mode', required=True, help='Mode, train/demo')
    parser.add_argument('-image', default='imgs/messi.jpg', help='input image name')
    parser.add_argument('-save', default='save_dir', help='save dir')

    parse = parser.parse_args()
    parse.model = parse.model.lower()
    parse.mode = parse.mode.lower()

    if parse.model == 'ssd':
        os.chdir('ssd')
        if parse.mode == 'demo':
            os.system('python detect.py --images ../{} --det ../{}'.format(parse.image, parse.save))
        elif parse.mode == 'train':
            os.system('python train.py')
        os.chdir('..')
    elif parse.model == 'yolov3':
        os.chdir('yolov3')
        if parse.mode == 'demo':
            # os.system('cd yolov3')vi
            os.system('python detect.py --images ../{} --det ../{}'.format(parse.image, parse.save))
        os.chdir('..')

if __name__ == '__main__':
    main()
