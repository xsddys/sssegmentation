'''upernet_convnextbase_ade20k'''
import copy
from .base_cfg import SEGMENTOR_CFG
from .._base_ import DATASET_CFG_ADE20k_512x512, DATALOADER_CFG_BS16


# deepcopy
SEGMENTOR_CFG = copy.deepcopy(SEGMENTOR_CFG)
# modify dataset config
SEGMENTOR_CFG['dataset'] = DATASET_CFG_ADE20k_512x512.copy()
# modify dataloader config
SEGMENTOR_CFG['dataloader'] = DATALOADER_CFG_BS16.copy()
# modify scheduler config
SEGMENTOR_CFG['scheduler']['max_epochs'] = 130
SEGMENTOR_CFG['scheduler']['min_lr'] = 0.0
SEGMENTOR_CFG['scheduler']['power'] = 1.0
SEGMENTOR_CFG['scheduler']['warmup_cfg'] = {'type': 'linear', 'ratio': 1e-6, 'iters': 1500}
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 150
SEGMENTOR_CFG['backbone'] = {
    'type': 'convnext_base', 'series': 'convnext', 'arch': 'base', 'pretrained': True, 'drop_path_rate': 0.4,
    'layer_scale_init_value': 1.0, 'gap_before_final_norm': False, 'selected_indices': (0, 1, 2, 3), 'norm_cfg': {'type': 'layernorm2d', 'eps': 1e-6},
}
SEGMENTOR_CFG['work_dir'] = 'upernet_convnextbase_ade20k'
SEGMENTOR_CFG['logfilepath'] = 'upernet_convnextbase_ade20k/upernet_convnextbase_ade20k.log'
SEGMENTOR_CFG['resultsavepath'] = 'upernet_convnextbase_ade20k/upernet_convnextbase_ade20k_results.pkl'