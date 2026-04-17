def calculate_mean(num_list):
    if not num_list:
        raise ValueError("List is empty.")
    return sum(num_list) / len(num_list)


def find_maximum(num_list):
    if not num_list:
        raise ValueError("List is empty.")
    return max(num_list)


def find_minimum(num_list):
    if not num_list:
        raise ValueError("List is empty.")
    return min(num_list)