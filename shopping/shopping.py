import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    #ST

    file=open(filename)
    csvreader=csv.reader(file)
    header=[]
    header=next(csvreader)

    print(header)

    users=[]
    for user in csvreader:
        users.append(user)
    file.close()

    evidence=[]
    labels=[]

    months=["jan","feb","mar","apr","may","june","jul","aug","sep","oct","nov","dec"]
    visitors=["new_visitor","returning_visitor"]
    bools=["false","true",]
    
    for user in users:
        evi=[]
        evi.append(int(user[header.index("Administrative")]))
        evi.append(float(user[header.index("Administrative_Duration")]))
        evi.append(int(user[header.index("Informational")]))
        evi.append(float(user[header.index("Informational_Duration")]))
        evi.append(int(user[header.index("ProductRelated")]))
        evi.append(float(user[header.index("ProductRelated_Duration")]))
        
        evi.append(float(user[header.index("BounceRates")]))
        evi.append(float(user[header.index("ExitRates")]))
        evi.append(float(user[header.index("PageValues")]))
        evi.append(float(user[header.index("SpecialDay")]))

        evi.append(months.index(user[header.index("Month")].lower()))

        evi.append(int(user[header.index("OperatingSystems")]))
        evi.append(int(user[header.index("Browser")]))
        evi.append(int(user[header.index("Region")]))
        evi.append(int(user[header.index("TrafficType")]))

        evi.append(1) if user[header.index("VisitorType")].lower()=="new_visitor" else evi.append(0)

        evi.append(bools.index(user[header.index("Weekend")].lower()))

        evidence.append(evi)

        labels.append(bools.index(user[-1].lower()))

    return (evidence,labels)
    
        
    #/ST


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    #ST

    model=KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence,labels)

    return model

    #/ST


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    #ST

    all_true=0
    all_false=0

    pred_true=0
    pred_false=0

    for i in range (len(labels)):
        if labels[i]==1:
            all_true+=1
            if labels[i]==predictions[i]:
                pred_true+=1
        else:
            all_false+=1
            if labels[i]==predictions[i]:
                pred_false+=1
        
            
    sensitivity=float(pred_true)/all_true
    specificity=float(pred_false)/all_false

    return (sensitivity,specificity)

    #/ST


if __name__ == "__main__":
    main()
