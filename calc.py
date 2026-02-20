import csv

def load_letter_groups(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]


def count_letter_groups(letter_groups, csv_filename, weighted=True):
    counts = {group: 0 for group in letter_groups}

    with open(csv_filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            word = row['word'].lower()
            frequency = int(row['frequency'])

            for group in letter_groups:
                occurrences = word.count(group)

                if occurrences > 0:
                    if weighted:
                        counts[group] += occurrences * frequency
                    else:
                        counts[group] += occurrences

    return counts


def save_results(counts, output_filename):
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    with open(output_filename, 'w', encoding='utf-8') as f:
        for group, count in sorted_counts:
            f.write(f"{group},{count}\n")


if __name__ == "__main__":
    letter_groups_file = "letter_groups.txt"
    word_frequency_file = "word_frequencies.csv"
    output_file = "letter_group_counts.csv"

    letter_groups = load_letter_groups(letter_groups_file)
    counts = count_letter_groups(letter_groups, word_frequency_file, weighted=True)
    save_results(counts, output_file)

    print("Done! Results saved to", output_file)