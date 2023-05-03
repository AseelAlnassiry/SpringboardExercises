def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    hsh = {}
    mx = nums[0]
    for n in nums: hsh[n] = 1 + hsh.get(n, 0)
    for n in hsh:
        if hsh[n] > hsh[mx]: mx = n
    return mx

