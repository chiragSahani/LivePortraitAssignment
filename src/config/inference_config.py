flag_use_half_precision: bool = True  # Use FP16 for faster inference (set False if you see black boxes)
flag_do_torch_compile: bool = True  # Use torch.compile for faster inference (requires PyTorch 2.0+)
input_shape: Tuple[int, int] = (256, 256)  # input shape (set to e.g. (128,128) for fast mode) 