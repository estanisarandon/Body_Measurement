import math
import pandas as pd
from KNN import KNN


def main():
    # Weight input
    weight = input("Please, enter your weight(kg): ")
    # Height input
    height = input("Enter your height (cm): ")
    # Gender input
    gender = input("Are you male or female? ")
    print("Thank you for your input.")
    print("Please, wait while we process your request...")

    test_input = [float(height), float(weight)]

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
    print("Based on a K-Nearest Neighbour analysis I predict that you will need:")
    print(f"A tshirt size {predicted_tshirt[0][0]} with a {predicted_tshirt[0][1]}% accuracy.")
    print(f"And pants size {predicted_pants[0][0]} with a {predicted_pants[0][1]}% accuracy.")


if __name__ == '__main__':
    main()

