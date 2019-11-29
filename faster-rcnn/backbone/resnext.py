from typing import Tuple

import torchvision
from torch import nn

#from backbone.resnext101 import resnext101_32x4d, resnext101_64x4d
import pretrainedmodels

import backbone.base


class ResNext(backbone.base.Base):

    def __init__(self, pretrained: bool):
        super().__init__(pretrained)

    def features(self) -> Tuple[nn.Module, nn.Module, int, int]:

        # Choose one  [ResNeXt101_32x4d, ResNeXt101_64x4d]
        _pretrained = None

        if self._pretrained is True:
            _pretrained = "imagenet"

        resnext101 = pretrainedmodels.resnext101_64x4d(pretrained=_pretrained)


        children = list(resnext101.children())
        features = children[:-2]
        num_features_out = 2048

        hidden = children[-2]
        num_hidden_out = 2048

        for parameters in [feature.parameters() for i, feature in enumerate(features) if i <= 4]:
            for parameter in parameters:
                parameter.requires_grad = False

        features = nn.Sequential(*features)

        return features, hidden, num_features_out, num_hidden_out
