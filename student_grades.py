class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >=90:
            return "A"
        elif body >=80:
            return "B"
        elif body >=70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, find):
        indexy = []
        for i, x in enumerate(self.scores):
            if x == find:
                indexy.append(i)
        return indexy

    def get_sorted(self):
        val2 = self.scores.copy()
        x = len(val2)
        for i in range(x):
            for j in range(0, x - 1 - i):
                if val2[j] > val2[j + 1]:
                    val2[j], val2[j + 1] = val2[j + 1], val2[j]
        return val2

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))# 91
    print(results.get_grade(2))
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny