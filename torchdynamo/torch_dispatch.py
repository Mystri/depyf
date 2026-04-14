import torch

# Get the operator object
op = torch.ops.aten.abs

# List all registered kernels and their dispatch keys
print(op._get_dispatch_table())
# Or inspect the schema and fallbacks
print(op._schema)