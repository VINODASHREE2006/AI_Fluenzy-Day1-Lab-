def estimate_memory(params_b, bytes_per_param, context_k):
    weights = params_b * bytes_per_param
    kv_cache = context_k * params_b * 0.000002
    total = weights + kv_cache + 1

    return {
        "weights": round(weights, 2),
        "kv_cache": round(kv_cache, 2),
        "total": round(total, 2)
    }

if __name__ == "__main__":
    print(estimate_memory(7, 0.5, 4))