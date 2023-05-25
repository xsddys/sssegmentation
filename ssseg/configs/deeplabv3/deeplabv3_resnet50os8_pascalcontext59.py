'''deeplabv3_resnet50os8_pascalcontext59'''
import copy
from .base_cfg import SEGMENTOR_CFG
from .._base_ import DATASET_CFG_PASCALCONTEXT59_480x480, DATALOADER_CFG_BS16


# deepcopy
SEGMENTOR_CFG = copy.deepcopy(SEGMENTOR_CFG)
# modify dataset config
SEGMENTOR_CFG['dataset'] = DATASET_CFG_PASCALCONTEXT59_480x480.copy()
# modify dataloader config
SEGMENTOR_CFG['dataloader'] = DATALOADER_CFG_BS16.copy()
# modify scheduler config
SEGMENTOR_CFG['scheduler']['max_epochs'] = 260
SEGMENTOR_CFG['scheduler']['optimizer'] = {
    'type': 'sgd', 'lr': 0.004, 'momentum': 0.9, 'weight_decay': 1e-4, 'params_rules': {},
}
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 59
SEGMENTOR_CFG['backbone'] = {
    'type': 'resnet50', 'series': 'resnet', 'pretrained': True,
    'outstride': 8, 'use_stem': True, 'selected_indices': (2, 3),
}
SEGMENTOR_CFG['head'] = {
    'in_channels': 2048, 'feats_channels': 512, 'dilations': [1, 12, 24, 36], 'dropout': 0.1,
}
SEGMENTOR_CFG['inference'] = {
    'mode': 'slide',
    'opts': {'cropsize': (480, 480), 'stride': (320, 320)}, 
    'tricks': {
        'multiscale': [1], 'flip': False, 'use_probs_before_resize': True,
    }
}
SEGMENTOR_CFG['work_dir'] = 'deeplabv3_resnet50os8_pascalcontext59'
SEGMENTOR_CFG['logfilepath'] = 'deeplabv3_resnet50os8_pascalcontext59/deeplabv3_resnet50os8_pascalcontext59.log'
SEGMENTOR_CFG['resultsavepath'] = 'deeplabv3_resnet50os8_pascalcontext59/deeplabv3_resnet50os8_pascalcontext59_results.pkl'