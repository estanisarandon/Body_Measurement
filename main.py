import math
import pandas as pd
from KNN import KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def main():
    # Weight input
    weight = input("Please, enter your weight(kg): ")
    # Height input
    height = input("Enter your height (cm): ")
    # Gender input
    gender = input("Are you male or female? ")
    print("Thank you for your input.")
    print("Please, wait while we process your request...")

    test_input = [[float(height), float(weight)]]

    # Load Tshirt Dataframe
    df_tshirt = pd.read_csv(f'{gender}_tshirt.csv')
    X_tshirt =list(zip(df_tshirt.Height.tolist(), df_tshirt.Weight.tolist()))
    y_tshirt = list(df_tshirt.Size.tolist())

    # Load Pants Dataframe
    df_pants = pd.read_csv(f'{gender}_pants.csv')
    X_pants = list(zip(df_pants.Height.tolist(), df_pants.Weight.tolist()))
    y_pants = list(df_pants.Size.tolist())

    # Start KNN & define K
    K = round(math.sqrt(len(y_tshirt)))
    clf = KNN(k=K)

    # Run KNN for T-shir
    clf.fit(X_tshirt, y_tshirt)
    predicted_tshirt = clf.predict(test_input)

    # Run KNN for Pants
    clf.fit(X_pants, y_pants)
    predicted_pants = clf.predict(test_input)

    # Print results
    print("")
    print("-------------------------------------------")
    print("Based on a K-Nearest Neighbour analysis I predict that you will need:")
    print(f"A tshirt size {predicted_tshirt[0][0]} with a {predicted_tshirt[0][1]}% accuracy.")
    print(f"And pants size {predicted_pants[0][0]} with a {predicted_pants[0][1]}% accuracy.")
    print("")
    input("Pres Enter to validate these data with Sklearn KNN")

    # Start Sklearn KNN and define K
    clf = KNeighborsClassifier(n_neighbors=K, weights='uniform')

    # Sklearn KNN T-shirt
    clf.fit(X_tshirt, y_tshirt)
    Sklearn_size_tshirt = clf.predict(test_input)

    # Sklearn KNN Pants
    clf.fit(X_pants, y_pants)
    Sklearn_size_pants = clf.predict(test_input)

    # Print results
    print("")
    print("-------------------------------------------")
    print("Based on the Sklearn KNN your sizes are:")
    print(f"For tshirt, computer says {Sklearn_size_tshirt[0]}.")
    print(f"And for pants, computer says {Sklearn_size_pants[0]}.")

    print("")
    input("Pres Enter to validate these data with Sklearn SVM")

    # Sklearn SVM T-shirt
    svclassifier = SVC(kernel="linear")
    svclassifier.fit(X_tshirt, y_tshirt)
    SVM_predicted_tshirt = svclassifier.predict(test_input)

    # Sklearn SVM Pants
    svclassifier.fit(X_pants, y_pants)
    SVM_predicted_pants = svclassifier.predict(test_input)

    # Print results
    print("")
    print("-------------------------------------------")
    print("Based on the Sklearn SVM your sizes are:")
    print(f"For tshirt, computer says {SVM_predicted_tshirt[0]}.")
    print(f"And for pants, computer says {SVM_predicted_pants[0]}.")


if __name__ == '__main__':
    main()