import random
import time

# OO to 00 mapping
rev_mapping = {'00': 'OO', '01': 'OA', '02': 'OF', '03': 'OB', '04': 'OD', '05': 'OV', '06': 'OS', '07': 'OL', '08': 'OM', '09': 'OH',
               '10': 'AO', '11': 'AA', '12': 'AF', '13': 'AB', '14': 'AD', '15': 'AV', '16': 'AS', '17': 'AL', '18': 'AM', '19': 'AH',
               '20': 'FO', '21': 'FA', '22': 'FF', '23': 'FB', '24': 'FD', '25': 'FV', '26': 'FS', '27': 'FL', '28': 'FM', '29': 'FH',
               '30': 'BO', '31': 'BA', '32': 'BF', '33': 'BB', '34': 'BD', '35': 'BV', '36': 'BS', '37': 'BL', '38': 'BM', '39': 'BH',
               '40': 'DO', '41': 'DA', '42': 'DF', '43': 'DB', '44': 'DD', '45': 'DV', '46': 'DS', '47': 'DL', '48': 'DM', '49': 'DH',
               '50': 'VO', '51': 'VA', '52': 'VF', '53': 'VB', '54': 'VD', '55': 'VV', '56': 'VS', '57': 'VL', '58': 'VM', '59': 'VH',
               '60': 'SO', '61': 'SA', '62': 'SF', '63': 'SB', '64': 'SD', '65': 'SV', '66': 'SS', '67': 'SL', '68': 'SM', '69': 'SH',
               '70': 'LO', '71': 'LA', '72': 'LF', '73': 'LB', '74': 'LD', '75': 'LV', '76': 'LS', '77': 'LL', '78': 'LM', '79': 'LH',
               '80': 'MO', '81': 'MA', '82': 'MF', '83': 'MB', '84': 'MD', '85': 'MV', '86': 'MS', '87': 'ML', '88': 'MM', '89': 'MH',
               '90': 'HO', '91': 'HA', '92': 'HF', '93': 'HB', '94': 'HD', '95': 'HV', '96': 'HS', '97': 'HL', '98': 'HM', '99': 'HH'}

# 00 to OO mapping
mapping = {v: k for k, v in rev_mapping.items()}


def test_mapping(count):
    correct_count = 0
    total_time = 0
    times = []

    oo_times = []
    oo_correct_count = 0

    for i in range(count):
        # Generate a random mapping
        oo = random.choice(list(mapping.keys()))

        # Prompt user to recall the mapping
        start_time = time.time()
        guess = int(input(f"{i}/{count}：What is the number for {oo}? "))
        end_time = time.time()

        # Calculate the time taken to guess and record it
        time_taken = int((end_time - start_time) * 1000)
        times.append(time_taken)
        total_time += time_taken

        # Check if the guess is correct and record it
        if guess == int(mapping[oo]):
            print("You are right!")
            correct_count += 1
            oo_correct_count += 1
        else:
            print("You are wrong! correct is：{}".format(mapping[oo]))

        oo_times.append(time_taken)

    # Calculate and print the statistics
    accuracy = correct_count / count
    avg_time = total_time / count

    oo_accuracy = oo_correct_count / count
    oo_avg_time = sum(oo_times) / count

    print(f"\nResults after {count} rounds:")
    print(f"Total time: {total_time} ms")
    print(f"Average time: {avg_time:.2f} ms")
    print(f"Accuracy: {accuracy * 100:.2f}%\n")

    print("OO to 00 mapping:")
    print(f"Average time: {oo_avg_time:.2f} ms")
    print(f"Accuracy: {oo_accuracy * 100:.2f}%")

    sorted_times = sorted(times)
    median_time = sorted_times[len(sorted_times) // 2]
    print(f"Median time: {median_time:.2f} ms")


# Prompt user to enter the number of rounds
count = int(input("Enter the number of rounds: "))
test_mapping(count)
