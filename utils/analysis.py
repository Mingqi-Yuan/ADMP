"""
Encoding = UTF-8
By Mingqi, Yuan, 2019/3/18
Usage: Parse the output from the utils.detection()
"""
import numpy as np

def analysis(input, label_num):
    """
    Analyse the output from the function: detection()
    :param input: The output from the function: detection()
    :param label_num: Total number of labels
    :return: A dict
    """
    quantity = input['num_detections']
    classes = []
    scores = []
    data = np.zeros([label_num, 2])
    # Get the type of each box
    for i in range(quantity):
        item = input['detection_classes'][i]
        classes.append(item)
    # Get the score for each box
    for i in range(quantity):
        item = input['detection_scores'][i]
        scores.append(round(item, 4))
    # Get the number and maximum score of each category.
    for i in range(label_num):
        num = 0
        rate = []
        for j in range(input['num_detections']):
            if classes[j] == i+1:
                num = num + 1
                rate.append(scores[j])
        if rate != []:
            max_rate = max(rate)
            data[i, 1] = round(max_rate * 100, 2)
        data[i, 0] = num
    data_dict = {'number': data[:,0],
                'max_score': data[:,1],
                 'address': []}

    return data_dict

