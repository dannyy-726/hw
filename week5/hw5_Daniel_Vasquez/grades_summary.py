import argparse
from tuple_and_file_utils import read_students, grade_summary, write_averages


def main():
# Set up command line argument parsing, do lab assignment to practice using argparse
    parser = argparse.ArgumentParser(description='Process student grades.')
    parser.add_argument('input_file', type=str, help='Input file containing student grades')
    parser.add_argument('output_file', type=str, help='Output file to write average grades')
    args = parser.parse_args()
# Read students from the input file
    students = read_students(args.input_file)
    summary = grade_summary(students)
    write_averages(args.output_file, summary)

if __name__ == "__main__":
    main()