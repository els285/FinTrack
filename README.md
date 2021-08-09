# FinTrack
For my own financial tracking

## Analysing Transaction Data

The `Transaction` object is a wrapper for a Pandas dataframe which contains all the transactions contained in an input csv. Generalised functionality for slicing this dataframe to look at total expenditure, BACS transfers etc.

## Generating Data

To avoid making personal finances public on this git, this script generates fake data in the correct TSB csv format. Run simply by:

```python
import Random_Transaction_CSV 
Random_Transaction_CSV(100,"./output_csv_file.csv")
```
which generates the file `output_csv_file.csv` with 100 different transactions.
