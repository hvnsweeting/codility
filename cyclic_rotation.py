# https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/
def solution(A, K):
    ''' Rotate an array A to the right by a given number of steps K.
    '''
    N = len(A)

    if N == 0:
        return A

    # After K rotations, the -Kth element becomes first element of list
    return A[-K:] + A[:N-K]


if __name__ == "__main__":
    cases = [(([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8]),
             (([], 0), []),
             (([5, -1000], 1), [-1000, 5])
             ]
    for case, expt in cases:
        res = solution(*case)
        assert expt == res, (expt, res)
