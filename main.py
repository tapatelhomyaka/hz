from collections import defaultdict


def parse_kiosk_file(filename):
    # Create a dictionary to store total spending per place
    spending_per_place = defaultdict(int)

    # Open and read the file
    with open(filename, 'r', encoding='utf-16') as file:
        # Skip the header line
        file.readline()

        # Process each line in the file
        for line in file:
            # Split the line into words and clean it
            parts = line.strip().split('\t')

            if len(parts) >= 6:
                # Get the spending amount (second to last item)
                spending = int(parts[-2])

                # Get the place (last item)
                place = parts[-1]

                # Add the spending to the corresponding place
                spending_per_place[place] += spending

    # Sort places by total spending in descending order and get the top 3
    sorted_places = sorted(spending_per_place.items(), key=lambda x: x[1], reverse=True)[:3]

    return sorted_places


def main():
    # Specify the filename
    filename = 'kiosk2.txt'

    # Get the top 3 places with highest spending
    top_places = parse_kiosk_file(filename)

    # Display the result
    print("Top 3 places with highest total spending:")
    for place, total_spending in top_places:
        print(f"{place}: {total_spending} UAH")


if __name__ == "__main__":
    main()
