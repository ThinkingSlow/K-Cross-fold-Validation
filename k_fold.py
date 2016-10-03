import k_fold
import normalizer
import parser
import train_test_data_generator
import display_module


def assignment_1():
    # Print welcome screen
    filename = display_module.display_content()

    # Read data fom the given csv file and return the complete dataset(attributes, class)
    feature_attribute_set, dataset = parser.read_file(filename)

    # Separate the attribute and class set
    feature_set, class_set = parser.create_feature_class_set(dataset)

    # Creating class set
    class_attribute_set = set(class_set)

    # Find the maximum and minimum for the attributes
    maximum, minimum = normalizer.maximum_minimum_features(feature_set)

    # Create new normalized feature set
    normalized_feature_set = normalizer.new_feature_set(feature_set, maximum, minimum)

    # Create new normalized data set
    normalized_data_set = parser.create_dataset(normalized_feature_set, class_set)

    # K-Fold data set splitting
    k = eval(input("\nEnter the value of 'K' for K Fold cross validation: "))
    while type(k) != int:
        k = eval(input("\nPlease enter an integer values for K: "))
    train_test_split = k_fold.create_kfolds(normalized_data_set, k)

    # Display the result
    option = 0
    display_module.display_options()
    while option != 7:
        option = eval(input("\nEnter Option: "))
        display_module.switch(option, feature_attribute_set, class_attribute_set, class_set, train_test_split)


assignment_1()
