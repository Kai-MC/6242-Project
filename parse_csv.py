import pandas as pd


def parse_csv(file_path, year=2021):
    df = pd.read_csv(file_path)
    time_col = "Start_Time"
    df = df[df[time_col].str.contains(str(year))]
    df[time_col] = pd.to_datetime(df[time_col])
    df = df.set_index(time_col)

    return df

def create_landscape(file_path):
    landscapes = ['Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway',
       'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop']
    df = pd.read_csv(file_path)
    # for all landscape columns, create a new column named Landscape whose value is a list that contains the namen of landscape columns whose value is true
    df['Landscape'] = df[landscapes].apply(lambda x: [landscape for landscape in landscapes if x[landscape]], axis=1)
    # drop all landscape columns
    df = df.drop(columns=landscapes)
    
    return df

if __name__ == "__main__":
    file_path = "us_accident_2020.csv"
    print("Columns in the file:", pd.read_csv(file_path).columns)
    # df = create_landscape(file_path)
    
    # df.to_csv("us_accident_2020.csv")

