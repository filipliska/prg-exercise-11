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


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))# 91
    print(results.get_grade(2))
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))