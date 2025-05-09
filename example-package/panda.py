import pandas as pd


def main():
    data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}

    df = pd.DataFrame(data)
    print(df)


if __name__ == "__main__":
    main()
