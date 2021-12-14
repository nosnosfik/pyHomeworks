def get_top_performers(file_path, number_of_top_students=5):
    students_dict = {}

    with open(file_path, 'r') as inp_file:
        for line in inp_file.readlines():
            line = line.strip().split(',')
            if line[-1].replace('.', '', 1).isdigit():
                students_dict[line[0]] = float(line[-1])

    return sorted(students_dict.keys(), key=lambda x: students_dict[x], reverse=True)[:number_of_top_students]


def write_students_age_desc(file_path, output_file):
    lines = []

    with open(file_path, 'r') as inp_file:
        for line in inp_file.readlines():
            lines.append(line.strip())

    lines.sort(key=lambda x: float(y) if (y := x.split(',')[1]).isdecimal() else float('inf'), reverse=True)

    with open(output_file, 'w') as out_file:
        for line in lines:
            if line != lines[-1]:
                line += '\n'

            out_file.write(line)