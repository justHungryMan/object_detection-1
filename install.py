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
<<<<<<< HEAD

=======
>>>>>>> c813f732acb682fd35bfcac54d4dbfccdaf8b8d9
os.chdir('ssd')
os.system('python3 create_data_lists.py')
os.chdir('..')
'''

os.system('conda install -c conda-forge pyyaml sympy h5py cython numpy scipy pandas matplotlib tqdm tensorboardX menpo opencv3 easydict graphviz python-graphviz python3-dev')
os.system('pip install --upgrade pip')
os.system('conda install -c dgursoy gcc-5')
# os.system('wget -O yolov3/yolov3.weights https://pjreddie.com/media/files/yolov3.weights')

# If collect2 error occurs,
# os.system('conda remove mkl mkl-include')
# os.system('conda install numpy pyyaml mkl=2019.3 mkl-include setuptools cmake cffi typing')

os.chdir('faster-rcnn')
os.system('python support/setup.py develop')
# If "nvcc fatal unsupported gpu arch 'compute_75'" error occurs,
# os.system("export TORCH_CUDA_ARCH_LIST='7.0'")
