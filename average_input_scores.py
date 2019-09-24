def average(score_list):
    total_of_scores = 0
    items_in_list = len(score_list)
    for s in score_list:
        total_of_scores += s
    average = total_of_scores / items_in_list
    return round(float(average), 2)


if __name__ == '__main__':
    last_name = input("Please enter your last name: ")
    first_name = input("Please enter your first name: ")
    num_list = []
    scores = 0
    sentinel_value = -1
    while scores >= 0:
        try:
            scores = float(input("Enter your score(s) or enter -1 when finished: "))
        except ValueError:
            print("Please enter numbers only.")
        else:
            if scores == sentinel_value:
                break
            else:
                num_list.append(scores)
    score = average(num_list)
    print(last_name + ', ' + first_name + ' ' 'grade:' '% 5.2f' % score)
