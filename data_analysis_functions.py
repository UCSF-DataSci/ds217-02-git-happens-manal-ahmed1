# data_analysis_functions.py (advanced analysis script)


# make grade distribution with percentages
def analyze_grade_distribution(grades, total):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        if g >= 90:
            dist["A"] += 1
        elif g >= 80:
            dist["B"] += 1
        elif g >= 70:
            dist["C"] += 1
        elif g >= 60:
            dist["D"] += 1
        else:
            dist["F"] += 1

    return {
        grade: f"{count} ({(count / total) * 100:.1f}%)"
        for grade, count in dist.items()
    }


# save advanced report to output file
def save_results(results, filename="output/analysis_report.txt"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Analysis Report (Advanced)\n")

        f.write(f"Total Students: {results['total']}\n")
        f.write(f"Average Grade: {results['average']:.1f}\n")
        f.write(f"Highest Grade: {results['highest']}\n")
        f.write(f"Lowest Grade: {results['lowest']}\n\n")

        f.write("Students by Subject:\n")
        for subject, count in results["subjects"].items():
            f.write(f"- {subject}: {count}\n")

        f.write("\nGrade Distribution:\n")
        for grade, value in results["distribution"].items():
            f.write(f"- {grade}: {value}\n")

    print(f"report saved to {filename}")


# main workflow
def main():
    students = load_data()
    results = analyze_data(students)
    save_results(results)


if __name__ == "__main__":
    main()
