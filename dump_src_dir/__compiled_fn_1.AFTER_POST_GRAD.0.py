from __future__ import annotations
import torch
from torch import device
class GraphModule(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 2]", arg1_1: "f32[2, 2]"):
         # File: /root/autodl-tmp/hanboyou/torch_compile.py:5 in fn, code: return x.sin().cos() + y
        sin: "f32[2, 2]" = torch.ops.aten.sin.default(arg0_1);  arg0_1 = None
        cos: "f32[2, 2]" = torch.ops.aten.cos.default(sin);  sin = None
        add: "f32[2, 2]" = torch.ops.aten.add.Tensor(cos, arg1_1);  cos = arg1_1 = None
        return (add,)
        