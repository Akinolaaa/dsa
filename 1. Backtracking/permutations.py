#  leetcode 46
# Generating permutations of an array of number. No dupicates allowed

def permutations(nums: list[int]) -> list[list[int]]:
  res = []

  if (len(nums) == 1):
    return [nums[:]];

  for i in range(len(nums)):
    removed = nums.pop(0);
    otherRes = permutations(nums);

    for r in otherRes:
      r.append(removed);
    res.extend(otherRes)
    nums.append(removed);

  return res

print(permutations([1,2,3]))




