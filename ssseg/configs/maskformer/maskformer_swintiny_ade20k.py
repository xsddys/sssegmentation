'''maskformer_swintiny_ade20k'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'ade20k',
    'rootdir': os.path.join(os.getcwd(), 'ADE20k'),
})
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update({
    'type': 'adamw',
    'lr': 0.00006,
    'betas': (0.9, 0.999),
    'weight_decay': 0.01,
    'params_rules': {'backbone_net_zerowd': (1.0, 0.0), 'others': (1.0, 1.0)},
})
# modify scheduler config
SCHEDULER_CFG = SCHEDULER_CFG.copy()
SCHEDULER_CFG.update({
    'max_epochs': 130,
    'min_lr': 0.0,
    'power': 1.0,
    'warmup_cfg': {'type': 'linear', 'ratio': 1e-6, 'iters': 1500},
})
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify segmentor config
SEGMENTOR_CFG = SEGMENTOR_CFG.copy()
SEGMENTOR_CFG.update({
    'num_classes': 150,
    'backbone': {
        'type': 'swin_tiny_patch4_window7_224',
        'series': 'swin',
        'pretrained': True,
        'selected_indices': (0, 1, 2, 3),
        'norm_cfg': {'type': 'layernorm'},
    },
    'ppm': {
        'in_channels': 768,
        'out_channels': 512,
        'pool_scales': [1, 2, 3, 6],
    },
    'lateral': {
        'in_channels_list': [96, 192, 384],
        'out_channels': 512,
    },
    'fpn': {
        'in_channels_list': [512, 512, 512],
        'out_channels': 512,
    },
})
SEGMENTOR_CFG['decoder']['predictor']['in_channels'] = 768
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['work_dir'] = 'maskformer_swintiny_ade20k'
COMMON_CFG['logfilepath'] = 'maskformer_swintiny_ade20k/maskformer_swintiny_ade20k.log'
COMMON_CFG['resultsavepath'] = 'maskformer_swintiny_ade20k/maskformer_swintiny_ade20k_results.pkl'