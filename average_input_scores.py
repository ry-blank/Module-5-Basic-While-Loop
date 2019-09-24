def average(score_list):
    total_of_scores = 0
    items_in_list = len(score_list)
    for x in score_list:
        total_of_scores += x
    average = total_of_scores / items_in_list
    return round(float(average), 2)


if __name__ == '__main__':
    num_list = []
    average(num_list)
