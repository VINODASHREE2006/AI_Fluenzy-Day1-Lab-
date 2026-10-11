from estimator import estimate_memory

print("=== Context Variation ===")
for ctx in [2, 4, 8, 16]:
    print(ctx, estimate_memory(7, 0.5, ctx))

print("\n=== Quantization Variation ===")
for bpp in [2, 1, 0.5, 0.25]:
    print(bpp, estimate_memory(7, bpp, 4))