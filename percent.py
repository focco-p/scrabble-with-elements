def load_counts(filename):
    counts = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                group, count = line.strip().split(',')
                counts[group] = int(count)
    return counts


def convert_to_percentages(counts):
    total = sum(counts.values())

    if total == 0:
        raise ValueError("Total count is zero — cannot compute percentages.")

    percentages = {
        group: (count / total) * 100
        for group, count in counts.items()
    }

    return percentages


def save_percentages(percentages, output_filename):
    sorted_percentages = sorted(percentages.items(), key=lambda x: x[1], reverse=True)

    with open(output_filename, 'w', encoding='utf-8') as f:
        for group, percentage in sorted_percentages:
            f.write(f"{group},{percentage:.6f}%\n")


if __name__ == "__main__":
    input_file = "letter_group_counts.csv"
    output_file = "letter_group_percentages.csv"

    counts = load_counts(input_file)
    percentages = convert_to_percentages(counts)
    save_percentages(percentages, output_file)

    print("Done! Percentages saved to", output_file)