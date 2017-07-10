def solution(N):
    '''Find longest sequence of zeros in binary representation of an integer
    (BinaryGap).

    Complexity:

            expected worst-case time complexity is O(log(N));
            expected worst-case space complexity is O(1).

    # This got perfect score, though, there are windows for improving
    # TODO: turn to divide to get Scomp O(1)
    # TODO: find a way to archive O(log(N)) instead of O(N)
    '''
    bin_presentation = bin(N)[2:]
    current_len = 0
    bingap = 0
    for c in bin_presentation:
        if c == '1':
            if current_len != 0:  # end counting
                bingap = max(bingap, current_len)
                current_len = 0
        if c == '0':
            current_len += 1

    return bingap


if __name__ == "__main__":
    cases = [(1041, 5), (1610612737, 28)]
    for c, expt in cases:
        res = solution(c)
        assert expt == res, (expt, res)
