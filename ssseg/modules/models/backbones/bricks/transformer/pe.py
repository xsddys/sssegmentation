'''
Function:
    Implementation of PositionEmbedding Methods
Author:
    Zhenchao Jin
'''
import math
import torch
import torch.nn as nn


'''PositionEmbeddingSine'''
class PositionEmbeddingSine(nn.Module):
    def __init__(self, num_pos_feats=64, temperature=10000, apply_normalize=False, scale=None, eps=1e-6):
        super(PositionEmbeddingSine, self).__init__()
        assert not ((scale is not None) and (not apply_normalize))
        self.eps = eps
        self.temperature = temperature
        self.num_pos_feats = num_pos_feats
        self.apply_normalize = apply_normalize
        if scale is None: scale = 2 * math.pi
        self.scale = scale
    '''forward'''
    def forward(self, x, mask=None):
        if mask is None: mask = torch.zeros((x.size(0), x.size(2), x.size(3)), device=x.device, dtype=torch.bool)
        not_mask = ~mask
        y_embed = not_mask.cumsum(1, dtype=torch.float32)
        x_embed = not_mask.cumsum(2, dtype=torch.float32)
        if self.apply_normalize:
            y_embed = y_embed / (y_embed[:, -1:, :] + self.eps) * self.scale
            x_embed = x_embed / (x_embed[:, :, -1:] + self.eps) * self.scale
        dim_t = torch.arange(self.num_pos_feats, dtype=torch.float32, device=x.device)
        dim_t = self.temperature ** (2 * (dim_t // 2) / self.num_pos_feats)
        pos_x = x_embed[:, :, :, None] / dim_t
        pos_y = y_embed[:, :, :, None] / dim_t
        pos_x = torch.stack(
            (pos_x[:, :, :, 0::2].sin(), pos_x[:, :, :, 1::2].cos()), dim=4
        ).flatten(3)
        pos_y = torch.stack(
            (pos_y[:, :, :, 0::2].sin(), pos_y[:, :, :, 1::2].cos()), dim=4
        ).flatten(3)
        pos = torch.cat((pos_y, pos_x), dim=3).permute(0, 3, 1, 2)
        return pos