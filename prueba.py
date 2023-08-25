def indices(nums, target):
    num_indices = {}

    for i, numero in enumerate(nums):
        resultado =target-numero
        if resultado in num_indices:
            return (num_indices[resultado], i)
        num_indices[numero] = i


