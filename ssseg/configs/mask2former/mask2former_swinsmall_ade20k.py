'''mask2former_swinsmall_ade20k'''
import copy
from .base_cfg import SEGMENTOR_CFG
from .._base_ import DATASET_CFG_ADE20k_512x512, DATALOADER_CFG_BS16


# deepcopy
SEGMENTOR_CFG = copy.deepcopy(SEGMENTOR_CFG)
# modify dataset config
SEGMENTOR_CFG['dataset'] = DATASET_CFG_ADE20k_512x512.copy()
SEGMENTOR_CFG['dataset']['train']['data_pipelines'][0] = (
    'RandomChoiceResize', {
        'scales': [int(512 * x * 0.1) for x in range(5, 21)], 
        'resize_type': 'ResizeShortestEdge', 
        'max_size': 2048,
    }
)
# modify dataloader config
SEGMENTOR_CFG['dataloader'] = DATALOADER_CFG_BS16.copy()
# modify scheduler config
SEGMENTOR_CFG['scheduler']['max_epochs'] = 130
SEGMENTOR_CFG['scheduler']['min_lr'] = 0.0
SEGMENTOR_CFG['scheduler']['clipgrad_cfg'] = {'max_norm': 0.01, 'norm_type': 2}
# modify other segmentor configs
SEGMENTOR_CFG['num_classes'] = 150
SEGMENTOR_CFG['backbone'] = {
    'type': 'SwinTransformer', 'structure_type': 'swin_small_patch4_window7_224', 'pretrained': True, 
    'selected_indices': (0, 1, 2, 3), 'norm_cfg': {'type': 'LayerNorm'},
    'pretrain_img_size': 224, 'in_channels': 3, 'embed_dims': 96, 'patch_size': 4, 'window_size': 7, 'mlp_ratio': 4,
    'depths': [2, 2, 18, 2], 'num_heads': [3, 6, 12, 24], 'qkv_bias': True, 'qk_scale': None, 'patch_norm': True,
    'drop_rate': 0., 'attn_drop_rate': 0., 'drop_path_rate': 0.3, 'use_abs_pos_embed': False,
}
SEGMENTOR_CFG['head']['pixel_decoder']['input_shape']['in_channels'] = [96, 192, 384, 768]
SEGMENTOR_CFG['work_dir'] = 'mask2former_swinsmall_ade20k'
SEGMENTOR_CFG['logfilepath'] = 'mask2former_swinsmall_ade20k/mask2former_swinsmall_ade20k.log'
SEGMENTOR_CFG['resultsavepath'] = 'mask2former_swinsmall_ade20k/mask2former_swinsmall_ade20k_results.pkl'