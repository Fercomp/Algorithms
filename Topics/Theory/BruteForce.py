# When we want to compare each element of an array with all others,
# a brute–force approach uses two nested loops:
nums = [2, 5, 12, 9, 10]

for i in range(len(nums)):
    for j in range(len(nums)):
        # Compare nums[i] with nums[j]
        continue

# However, this repeats comparisons. For example, after comparing
# nums[0] with nums[1], we later compare nums[1] with nums[0] again.
# We also compare each element with itself, which is often unnecessary.

# To avoid redundant checks, we can start the inner loop from i + 1.
# This way, each pair is compared only once, and we skip self-comparisons.
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        # Compare nums[i] with nums[j]
        continue

# This pattern extends naturally to more nested loops.
# Always advance the starting index of the next loop.
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            # Compare nums[i], nums[j], and nums[k]
            continue