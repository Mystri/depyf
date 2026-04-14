import torch

@torch.compile(backend='inductor') # "inductor" is the default backend for CPU
def fn(x, y):
    return x.sin().cos() + y

# result = fn(x, y) # First call triggers compilation and execution
# print(result)

# For subsequent calls, the compiled code is reused, leading to faster execution
# result = fn(x, y)      
# print(result)

def main():
    x, y = torch.randn(2,2).to('cuda'), torch.randn(2,2).to('cuda')
    
    for i in range(100):
        result = fn(x, y)
print(fn)
breakpoint()

import depyf
with depyf.prepare_debug("./dump_src_dir"):\
    main()
# with depyf.debug():
#     main()
# # After first run, get the compiled graph
# compiled_fn = fn._torchdynamo_orig_callable  # access original function
# gm = torch.fx.symbolic_trace(fn.__wrapped__)  # trace the original Python function
# print("Original FX Graph:")
# print(gm.graph)



# explanation = torch._dynamo.explain(fn, x, y)
# print("\nDynamo Explanation:")
# print(explanation)