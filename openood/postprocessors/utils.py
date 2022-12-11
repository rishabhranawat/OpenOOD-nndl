from openood.utils import Config

from .base_postprocessor import BasePostprocessor
from .odin_postprocessor import ODINPostprocessor


def get_postprocessor(config: Config):
    postprocessors = {
        'msp': BasePostprocessor,
        'odin': ODINPostprocessor}

    return postprocessors[config.postprocessor.name](config)


