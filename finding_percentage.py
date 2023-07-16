if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    na = student_marks[query_name]
    avg = sum(na)/len(na)
    print("%.2f" % avg)
