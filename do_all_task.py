def show_image_size_survey():
    """
    task 1 : show result of survey image size
    """
    import os 
    import cv2
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    import sys


    def show_graph(d:dict):
        """
        this function read data from a python dict
        then draw a graph to visualize data in dict
        """
        x = []
        y = []
        for key, value in d.items():
            x.append(str(key))
            y.append(value)

        x_pos = [i for i, _ in enumerate(x)]
        plt.figure()
        plt.bar(x_pos, y, color='green')
        plt.xlabel("Size")
        plt.ylabel("Number of images")
        plt.title("Count by size = width + height ")
        plt.xticks(x_pos, x)

    ## this is result of photo attack
    # size_train= {'<100': 1077, '100-200': 17298, '200-300': 36400, '300-400': 42121, '400-500': 39558, '500-600': 34338, '600-700': 19799, '>700': 33470}
    # size_test = {'0-100': 219, '100-200': 3483,'200-300': 6772, '300-400': 6289, '400-500': 7343, '500-600': 5800, '600-700': 4109, '>700': 10378}

    # replay attack - not done yet

    show_graph(size_train)
    show_graph(size_test)
    plt.show()


def show_tpr_fpr_graph(spoof_score_txt):
    """
    spoof_score_txt is a file being generated by run evaluate
    this function take the path as input, and show result to screen
    """
    import numpy as np
    import os
    from eer_calculation import cal_metric
    with open(spoof_score_txt, 'r') as f:
        spoof_score = np.array(f.read().splitlines(), dtype=np.float)
    # print(spoof_score.shape)

    # test set has number live sample : 20955
    # test set has number spoof sample : 23438
    count_live = 31667
    count_spoof = 66838

    labels = np.array([0]*count_live + [1]*count_spoof, dtype=np.float)

    result_spoof = cal_metric(labels, spoof_score)
    print('eer spoof is : ' + str(result_spoof[0]) )
    print('tpr spoof is : ' + str(result_spoof[1]) )
    print('auc spoof is : ' + str(result_spoof[2]) )
    print('threshold for eer is : ' + str(result_spoof[4]) )

    # class_predcit = np.round(spoof_score)
    threshold_spoof = result_spoof[4]
    # threshold = 0.5
    class_predict = np.array(np.where(spoof_score < threshold_spoof, 0, 1))

    temp = 0
    for i in range(labels.shape[0]):
        if class_predict[i] == labels[i]:
            temp += 1

    acc = round(temp/labels.shape[0], 4)
    print(f"acc of model at threshold {threshold_spoof} is {acc}: ")


def get_input_shape_model():
    from keras.models import load_model
    import numpy as np
    model_path = '/home/duong/project/pyimage_research/result_model/version_2/result_new_b0_ver4/cp_01.h5'
    my_model = load_model(model_path)
    input_model = my_model.input_shape
    width , height = input_model[1], input_model[2]
    print(width, height)
    # print(input_model.shape)


if __name__ == '__main__':
    # task 1: survey in image size
    # show_image_size_survey()

    # task 2: show fnr, tpr, threshold graph
    result_all = '/home/duong/project/pyimage_research/result_model/version_3/result_replay_attack_project_f19'

    # model_name = 'b0_ver_1'
    # list_cp_index = ['cp_01.h5', 'cp_03.h5','cp_04.h5','cp_06.h5']
    # for cp_index in list_cp_index:
    #     spoof_score_txt = result_all + '/' + model_name + '/test_' + cp_index[:-3] + '/score_prediction.txt' 
    #     show_tpr_fpr_graph(spoof_score_txt)
    model_name = 'b4_ver_1'
    list_cp_index = ['cp_01.h5', 'cp_03.h5','cp_04.h5','cp_06.h5', 'cp_08.h5']
    for cp_index in list_cp_index:
        spoof_score_txt = result_all + '/' + model_name + '/test_' + cp_index[:-3] + '/score_prediction.txt' 
        show_tpr_fpr_graph(spoof_score_txt)


    ## task 3: load model and get input shape of model
    # get_input_shape_model()
    
    ## u dont know shit
    # {"installed":{"client_id":"617384173899-lhsd59eokdd9aj4f7h8g60ch4v215c6u.apps.googleusercontent.com","project_id":"movefile-10122020","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"SWDgjfo66O7gkj0OS-zHfhJs","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}