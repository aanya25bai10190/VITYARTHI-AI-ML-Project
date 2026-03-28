from sklearn.model_selection import train_test_split

def preprocess_data(df):
    df = df.drop('id', axis=1)

    X = df.drop('cardio', axis=1)
    y = df['cardio']

    return train_test_split(X, y, test_size=0.2, random_state=42)