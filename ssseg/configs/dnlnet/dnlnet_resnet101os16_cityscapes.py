'''dnlnet_resnet101os16_cityscapes'''
import copy
from .base_cfg import SEGMENTOR_CFG
from .._base_ import DATASET_CFG_CITYSCAPES_512x1024, DATALOADER_CFG_BS8


# deepcopy
SEGMENTOR_CFG = copy.deepcopy(SEGMENTOR_CFG)
# modify dataset config
SEGMENTOR_CFG['dataset'] = DATASET_CFG_CITYSCAPES_512x1024.copy()
# modify dataloader config
SEGMENTOR_CFG['dataloader'] = DATALOADER_CFG_BS8.copy()
# modify scheduler config
SEGMENTOR_CFG['scheduler']['max_epochs'] = 220
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 19
SEGMENTOR_CFG['backbone'] = {
    'type': 'resnet101', 'series': 'resnet', 'pretrained': True,
    'outstride': 16, 'use_stem': True, 'selected_indices': (2, 3),
}
SEGMENTOR_CFG['work_dir'] = 'dnlnet_resnet101os16_cityscapes'
SEGMENTOR_CFG['logfilepath'] = 'dnlnet_resnet101os16_cityscapes/dnlnet_resnet101os16_cityscapes.log'
SEGMENTOR_CFG['resultsavepath'] = 'dnlnet_resnet101os16_cityscapes/dnlnet_resnet101os16_cityscapes_results.pkl'