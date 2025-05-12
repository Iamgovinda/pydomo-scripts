from pydomo import DataSetRequest, Column, ColumnType, Schema, Domo

from config.env import domo_client_id, domo_client_secret, domo_api_host
from domo_utils import get_csv_file_headers


def create_dataset(csv_file_path, dataset_name):
    try:
        headers = get_csv_file_headers(csv_file_path)
        # print(headers)
        domo = Domo(domo_client_id, domo_client_secret, api_host=domo_api_host)
        ds = domo.datasets
        dsr = DataSetRequest()
        dsr.name = dataset_name
        columns = [Column(ColumnType.STRING, col.get("column")) for col in headers]
        print(columns)
        dsr.schema = Schema(columns)
        dataset = ds.create(dsr)
        print("DATASET CREATED WITH ID: ", dataset['id'])
    except Exception as e:
        print("EXCEPTION OCCURRED DURING DATASET CREATION: ", e)


if __name__ == '__main__':
    create_dataset("yourfile.csv", "dataset name")
