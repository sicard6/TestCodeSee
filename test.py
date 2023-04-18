import pandas as pd
import ingestion.test_inner as bd
import curated.test_inner_curated as db


if __name__ == "__main__":

    print(bd.test())
    print(db.testCurated())

