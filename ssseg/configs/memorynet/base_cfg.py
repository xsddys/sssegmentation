'''SEGMENTOR_CFG for MCIBI'''
SEGMENTOR_CFG = {
    'type': 'memorynet',
    'num_classes': -1,
    'benchmark': True,
    'align_corners': False,
    'backend': 'nccl',
    'work_dir': 'ckpts',
    'logfilepath': '',
    'log_interval_iterations': 50,
    'eval_interval_epochs': 10,
    'save_interval_epochs': 1,
    'resultsavepath': '',
    'norm_cfg': {'type': 'syncbatchnorm'},
    'act_cfg': {'type': 'relu', 'inplace': True},
    'backbone': {
        'type': 'resnet101', 'series': 'resnet', 'pretrained': True, 
        'outstride': 8, 'use_stem': True, 'selected_indices': (0, 1, 2, 3),
    },
    'head': {
        'downsample_backbone': {'kernel_size': 3, 'stride': 1, 'padding': 1, 'bias': False},
        'context_within_image': {'is_on': True, 'type': ['ppm', 'aspp'][1], 'cfg': {'dilations': [1, 12, 24, 36]}},
        'use_hard_aggregate': False, 'in_channels': 2048, 'feats_channels': 512, 'transform_channels': 256,
        'out_channels': 512, 'num_feats_per_cls': 1, 'use_loss': True, 'loss_cfg': {'celoss': {'scale_factor': 1.0, 'reduction': 'mean'}},
        'update_cfg': {
            'strategy': 'cosine_similarity', 'ignore_index': 255,
            'momentum_cfg': {'base_momentum': 0.9, 'base_lr': 0.01, 'adjust_by_learning_rate': True}
        },
        'dropout': 0.1,
    },
    'auxiliary': {
        'in_channels': 1024, 'out_channels': 512, 'dropout': 0.1,
    },
    'losses': {
        'loss_aux': {'celoss': {'scale_factor': 0.4, 'ignore_index': 255, 'reduction': 'mean'}},
        'loss_cls_stage1': {'celoss': {'scale_factor': 0.4, 'ignore_index': 255, 'reduction': 'mean'}},
        'loss_cls_stage2': {'celoss': {'scale_factor': 1.0, 'ignore_index': 255, 'reduction': 'mean'}},
    },
    'inference': {
        'mode': 'whole',
        'opts': {}, 
        'tricks': {
            'multiscale': [1], 'flip': False, 'use_probs_before_resize': False,
        }
    },
    'scheduler': {
        'type': 'poly', 'max_epochs': 0, 'power': 0.9,
        'optimizer': {
            'type': 'sgd', 'lr': 0.01, 'momentum': 0.9, 'weight_decay': 5e-4, 'params_rules': {},
        }
    },
    'dataset': None,
    'dataloader': None,
}