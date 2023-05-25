'''emanet_resnet101os8_ade20k'''
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
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 150
SEGMENTOR_CFG['work_dir'] = 'emanet_resnet101os8_ade20k'
SEGMENTOR_CFG['logfilepath'] = 'emanet_resnet101os8_ade20k/emanet_resnet101os8_ade20k.log'
SEGMENTOR_CFG['resultsavepath'] = 'emanet_resnet101os8_ade20k/emanet_resnet101os8_ade20k_results.pkl'