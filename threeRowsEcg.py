import csv
import random
import datetime

# Generate sample data
def generate_sample_data(num_samples):
    data = []
    current_time = datetime.datetime.now()
    for _ in range(num_samples):
        ecg_1 = random.uniform(-100,100)  # Simulated ECG value
        ecg_2 = random.uniform(-100,100)  # Simulated ECG value
        ecg_3 = random.uniform(-100,100)  # Simulated ECG value
        data.append([current_time.strftime('%Y-%m-%d %H:%M:%S.%f'), ecg_1, ecg_2, ecg_3])
        current_time += datetime.timedelta(milliseconds=100)  # Increment time by 1 second
    return data

# Write data to CSV file
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['time', 'ecg_1', 'ecg_2', 'ecg_3'])  # Write header
        csvwriter.writerows(data)  # Write data rows

if __name__ == "__main__":
    num_samples = 200  # Change this to the desired number of samples
    sample_data = generate_sample_data(num_samples)
    csv_filename = 'sample_ecg_data_3_rows.csv'
    write_to_csv(csv_filename, sample_data)
    print(f'Sample CSV file "{csv_filename}" generated with {num_samples} samples.')
