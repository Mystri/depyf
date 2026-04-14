from __future__ import annotations
import torch
from torch import device
class GraphModule(torch.nn.Module):
    def forward(self, L_x_: "f32[2, 2]", L_y_: "f32[2, 2]"):
        l_x_ = L_x_
        l_y_ = L_y_
        
         # File: /root/autodl-tmp/hanboyou/torch_compile.py:5 in fn, code: return x.sin().cos() + y
        sin: "f32[2, 2]" = l_x_.sin();  l_x_ = None
        cos: "f32[2, 2]" = sin.cos();  sin = None
        add: "f32[2, 2]" = cos + l_y_;  cos = l_y_ = None
        return (add,)
        