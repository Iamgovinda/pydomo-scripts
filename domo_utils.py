import pandas
from pydomo import Domo, Column, ColumnType, Schema, DataSetRequest

from config.env import domo_client_id, domo_client_secret, domo_host_name


# GENERATE SCHEMA COLUMNS FOR DOMO DATASET
def generate_schema_columns(header_with_types):
    """Returns a list of schema columns based on the headers and their data types."""
    schema_columns = []
    for column_info in header_with_types:
        print(column_info)
        col_name = column_info['column']
        # col_type = column_info['type']

        schema_type = ColumnType.STRING
        schema_columns.append(Column(schema_type, col_name))
    return schema_columns


def get_csv_file_headers(file_path):
    """Returns the headers of a CSV file as a list."""
    dataframe = pandas.read_csv(file_path)
    # Create a list of dictionaries with column names and their types
    column_info = [{'column': col, 'type': dtype} for col, dtype in dataframe.dtypes.items()]
    return column_info


def update_dataset(domo, ds_id, update_headers):
    try:
        update = DataSetRequest()
        columns = generate_schema_columns(update_headers)
        print(columns)
        update.schema = Schema(columns)
        datasets = domo.datasets
        datasets.update(ds_id, update)
        print("DATASET UPDATED!")
    except Exception as e:
        print("UNABLE TO UPDATE DATASET " + e.__str__())


def upload_data_to_dataset(csv_file_path, ds_id, method="APPEND"):
    try:
        domo = Domo(domo_client_id, domo_client_secret, api_host=domo_host_name)
        dataframe = pandas.read_csv(csv_file_path)
        headers = [{'column': col, 'type': dtype} for col, dtype in dataframe.dtypes.items()]
        update_dataset(domo, ds_id, headers)
        datasets = domo.datasets
        datasets.data_import_from_file(ds_id, csv_file_path, update_method=method)
        print(f"DATA IMPORTED TO DOMO DATASET: {csv_file_path} to {ds_id}")
        return True
    except Exception as e:
        print("UNABLE TO UPLOAD DATA TO DATASET " + e.__str__())


if __name__ == "__main__":
    csv_file = "yourfile.csv"
    try:
        upload_data_to_dataset(csv_file, "dataset_id", "REPLACE")
    except Exception as exc:
        print(exc)
