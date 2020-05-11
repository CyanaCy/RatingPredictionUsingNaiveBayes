# Rating-Prediction-Using-Naive-Bayes

This project implement a small prediction model for predicting the rating based on the review. It uses Kaggle dataset **BoardGameGeek Review**.

## Libraries Needed:
pip json<br>
pip re<br>
pip random<br>
pip math<br>
pip sklearn<br>
pip nltk<br>
nltk.download("stopwords")<br>
pip install jupyter notebook

## Deploy Flask Implementation Using Pythonanywhere
0. Download this repo.
1. Download dataset ***bgg-13m-reviews.csv*** from https://www.kaggle.com/jvanelteren/boardgamegeek-reviews and put it in the mysite file.
2. Run Jypyter notebook ***RatingPredictionUsingBayes.ipynb*** to get 3 json files.
3. Register in https://www.pythonanywhere.com
4. Select **"Web"** in the upper right corner and click **"Add a new web app"**.
5. In **"Select a Python Web Frameword"** list, select **"Flask"**.
6. In **"Select Python Version"** list, select the python version you like.
7. Select the path and place the Flash App code, the default file is **flash_app.py**.
8. Uploads codes and data.
9. Go to **"Web"** page and click **"Reload {yourusername}.pythonanywhere.com"**.
10. You can open **https://{yourusername}.pythonanywhere.com** to see application.
