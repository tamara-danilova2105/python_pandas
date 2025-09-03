from app.features.build_features import build_features
from app.features.company_analysis import company_analysis
from app.features.data_cleaning import data_cleaning
from app.features.visualization import visualization
from app.features.time_series import time_series
from app.features.io_operations import io_operations

def main():
    build_features()
    company_analysis()
    data_cleaning()
    visualization()
    time_series()
    io_operations()

if __name__ == "__main__":
    main()
