# 📄 Deep Question Answering [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple Q&A webapp to process text built using RoBerTa Model from Huggingface Transformers 🤗.

![plain_text](https://user-images.githubusercontent.com/29462447/152040979-3746ce6e-fbd5-4c00-8b6b-50b526a9ba6b.gif)

![pdf](https://user-images.githubusercontent.com/29462447/152040990-2fc3645a-4a7b-4a1b-a308-4b3ceae85407.gif)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Simply run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading documents, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

## Results:
1. Perform Q&A on random text on the fly!
![plain_text](https://user-images.githubusercontent.com/29462447/152040979-3746ce6e-fbd5-4c00-8b6b-50b526a9ba6b.gif)


2. Upload your document ***(supports PDFs, Word Files, Text files)*** and perform Q&A:

![docx](https://user-images.githubusercontent.com/29462447/152041322-1ed4e76f-614c-40ec-b9e6-b2274f77ff87.gif)
![pdf](https://user-images.githubusercontent.com/29462447/152040990-2fc3645a-4a7b-4a1b-a308-4b3ceae85407.gif)

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
