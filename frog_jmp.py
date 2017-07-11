# https://codility.com/programmers/lessons/3-time_complexity/frog_jmp/
import math


def solution(X, Y, D):
    return math.ceil((Y - X) / float(D))


if __name__ == "__main__":
    assert 3 == solution(10, 85, 30)
