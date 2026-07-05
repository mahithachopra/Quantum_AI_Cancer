from config import BATCH_SIZE


def chunks(dataframe):

    total = len(dataframe)

    for start in range(0, total, BATCH_SIZE):

        yield dataframe.iloc[start:start + BATCH_SIZE]