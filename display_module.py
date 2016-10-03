import sys
import train_test_data_generator


def display_content():
    print("\n''''''''''''''''''''''  MACHINE LEARNING - ASSIGNMENT 1  '''''''''''''''''''''''''''''''''''\n")
    filename = input("Please enter the complete filename of the csv file in the folder (with extension): ")
    return filename


def display_train_test_data(train_test_split):
    """ Gets the train test dataset from the K-fold cross validation and displays it

    :param train_test_split:
        train_test_split - array[list[list]]: Contains k arrays of training and test data splices of dataset

            Example: [[[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ....] , .... ,
                    [[0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]]
    """
    index = 0
    for x in train_test_split:
        index += 1
        print("\n Size of the array no.{} is {}".format(index, len(x)))
        print("\n {} ".format(x))


def print_data(train_data, test_data):
    """ Gets the train and test dataset and displays it

    :param train_data:
        train_data - array[list]: Contains k arrays of train data of dataset

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ... , .... ,
                    [0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]

    :param test_data
    :
        test_data - array[list]: Contains k arrays of test data of dataset

            Example: [[0.23, 0.34, 0.33, 0.12, 0.45, 0.68], [0.13, 0.35, 0.01, 0.72, 0.25, 0.08], ... , .... ,
                    [0.12, 0.45, 0.23, 0.64, 0.67, 0.98], [0.20, 0.50, 0.23, 0.12, 0.32, 0.88], ....]
    """
    print("\n''''''''''''''''''''''''''''''''''''''''''TEST DATA''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    print(test_data)
    print("\nThe size of the testing dataset is {}".format(len(test_data)))
    print("\n''''''''''''''''''''''''''''''''''''''''''TRAIN DATA'''''''''''''''''''''''''''''''''''''''''''''''''''\n")
    print(train_data)
    print("\nThe size of the training dataset is {}".format(len(train_data)))


def display_options():
    print("\nPlease select any option listed below")
    print("\n 1. Print Feature set")
    print("\n 2. Print Class set")
    print("\n 3. Print Complete Class set")
    print("\n 4. Create train, test data set")
    print("\n 5. Print options ")
    print("\n 6. Exit program \n")


def switch(option, feature_set, class_attribute_set, class_set, train_test_split):
    if option == 1:
        print("\nFeatures set: {}".format(feature_set))
    elif option == 2:
        print("\nClass set: {}".format(class_attribute_set))
    elif option == 3:
        print("\nAll class data: {}".format(class_set))
    elif option == 4:
        train, test = train_test_data_generator.generate_data(train_test_split)
        print_data(train, test)
    elif option == 5:
        display_options()
    elif option == 6:
        sys.exit()
    else:
        print("\nPlease enter any one of the option above")
