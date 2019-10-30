import os

os.system('conda install pytorch torchvision')
os.system('conda install pip pyyaml sympy h5py cython numpy scipy pandas matplotlib')
os.system('conda install -c menpo opencv3')
os.system('pip install --upgrade pip')
os.system('pip install easydict')

os.system('wget -O yolov3/yolov3.weights https://pjreddie.com/media/files/yolov3.weights')
os.system('wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar')
os.system('wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar')
os.system('wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCdevkit_08-Jun-2007.tar')

os.system('tar xvf VOCtrainval_06-Nov-2007.tar')
os.system('tar xvf VOCtest_06-Nov-2007.tar')
os.system('tar xvf VOCdevkit_08-Jun-2007.tar')

os.system('mv VOCdevkit ssd/VOCdevkit')

os.system('conda install -c conda-forge graphviz')
os.system('conda install -c conda-forge python-graphviz')
os.chdir('ssd')
os.system('python3 create_data_lists.py')
os.chdir('..')
