# FlightPricePrediction
A repository to fulfill the AIS DSP Group Project. Composed of Martin Sejas, Younes Chaik, Marie Thérèse Feuijo

You can find the dataset  [here.](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

<hr></hr>

## Important: Steps to load the dataset for this project: 

For storage reasons the dataset is not uploaded into the repository. 

Additionally the data has been split in two, half for ingestion and the other half for training.

To correctly run this project please follow the following steps:

<i>


1. Clone this repository from Github into your local machine.

2. Create a folder called 'data' at the root of your repository. E.g The path should be "FlightPricePrediction/data"

3. Download the csv file called 'Clean_Dataset.csv' into the folder 'data' from the Kaggle link above. 

4. Making sure your terminal's working directory is on the repository and not any subfolders, run the splitting data script '0.0-splitting-data.py' under "/model/industralized-scripts"

5. The script will automatically split the data into ingestion data and training in their respective folders, '/airflow-data/ ' and 'model/raw_data/
</i>

<hr></hr>

## Running the Streamlit App

After cloning this repository. To run the Streamlit app locally follow these steps: 



1. Open your terminal on the root of this repository

2. Install all the packages in requirements.txt in your terminal by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the following command: 
    ```bash
    streamlit run frontend/Make_Predictions.py
    ```

4. Copy paste the URL on your terminal into your browser

5. RUN FOR API

```bash
uvicorn Fastapi_endpoints_copy:app --port 5000