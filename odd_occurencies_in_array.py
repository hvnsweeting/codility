# https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
def solution(A):
    return reduce(lambda x, y: x ^ y, A)


if __name__ == "__main__":
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
