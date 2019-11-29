from typing import Tuple, Type

from torch import nn


class Base(object):

    OPTIONS = ['resnet18', 'resnet50', 'resnet101', 'inception_resnet_v2', 'resnext']

    @staticmethod
    def from_name(name: str) -> Type['Base']:
        if name == 'resnet18':
            from backbone.resnet18 import ResNet18
            return ResNet18
        elif name == 'resnet50':
            from backbone.resnet50 import ResNet50
            return ResNet50
        elif name == 'resnet101':
            from backbone.resnet101 import ResNet101
            return ResNet101
        elif name == 'inception_resnet_v2':
            from backbone.inception_resnet_v2 import Inception_Resnet_V2
            return Inception_Resnet_V2
        elif name == 'nasnet':
            from backbone.nasnet import NASnet
            return NASnet
        elif name == 'resnext':
            from backbone.resnext import ResNext
            return ResNext
        else:
            raise ValueError

    def __init__(self, pretrained: bool):
        super().__init__()
        self._pretrained = pretrained

    def features(self) -> Tuple[nn.Module, nn.Module, int, int]:
        raise NotImplementedError
