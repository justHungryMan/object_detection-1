from typing import Tuple

import torchvision
from torch import nn

from backbone.inceptionresnetv2 import inceptionresnetv2

import backbone.base


class Inception_Resnet_V2(backbone.base.Base):

    def __init__(self, pretrained: bool):
        super().__init__(pretrained)

    def features(self) -> Tuple[nn.Module, nn.Module, int, int]:
        model = inceptionresnetv2(pretrained=self._pretrained)

        children = list(model.children())
        features = children[:-2]
        num_features_out = 1536

        hidden = children[-2]
        num_hidden_out = 1536

        for parameters in [feature.parameters() for i, feature in enumerate(features) if i <= 4]:
            for parameter in parameters:
                parameter.requires_grad = False

        features = nn.Sequential(*features)

        return features, hidden, num_features_out, num_hidden_out
