import csv

def validate_annotations(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['label'] or not row['confidence']:
                print("Invalid annotation found:", row)

validate_annotations('image_annotation/annotations.csv')
