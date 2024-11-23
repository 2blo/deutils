import pandas as pd
def example_function(dataframe: pd.DataFrame) -> pd.DataFrame:
    len_df = len(dataframe)
    dataframe["new_column"] = pd.Series([i for i in range(len_df)])
    return dataframe
