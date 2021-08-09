# FinTrack
For my own financial tracking

## Analysing Transaction Data

The `Transaction` object is a wrapper for a Pandas dataframe which contains all the transactions contained in an input csv. Generalised functionality for slicing this dataframe to look at total expenditure, BACS transfers etc.

```python
from Trans import Transactions_FromCSV as From_CSV
July   = From_CSV("./july_exported.csv")
August = From_CSV("./august_exported.csv")
```

The `Transaction` wrappers can be combined such that the methods can be applied to larger sets of transactions than were (or can be) included in the CSV files

```python
from Trans import Transactions_Combined as Combine
Combine(July,August)
```

Transactions are sorted by date.


## Generating Data

To avoid making personal finances public on this git, this script generates fake data in the correct TSB csv format. Run simply by:

```python
from Data_Generation import Random_Transaction_CSV 
Random_Transaction_CSV(100,"./output_csv_file.csv")
```
which generates the file `output_csv_file.csv` with 100 different transactions.
