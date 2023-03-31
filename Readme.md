
# Score Predictor ML Model

Score Predictor ML Model Predicts The Final Score that can be Achieved by the batting team in the first innings on the basis of current situation.
  


## Screenshots

![App Screenshot](https://github.com/Suyash9422/tp/blob/main/Screenshot%20(764).png?raw=true)

![App Screenshot](https://github.com/Suyash9422/tp/blob/main/Screenshot%20(765).png?raw=true)











r2 Score of the model => 0.988   
Mean_Absolute_error => 1.623
## Requiremnets

IDE

```bash
 You must have any IDE install on your system (for eg VS CODE, Pycharm,etc)
```


DataSet


```bash
 DataSet link => https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket
```



List of required libraries

```bash
 pip install pandas
 pip install numpy
 pip insatll pickle
 pip install streamlit
 pip install tqdm
 pip install -u scikit-learn
 pip install xgboost
```
 
## Deployment

To deploy this project follow the following steps :

```bash
  Download the folder containing all the required files in the zip format from my github repo
  link=> https://github.com/Suyash9422/Machine_learning/tree/main/T20_Score%20_predictor  
```  



After downloading the zip file extact it and then open extracted folder and open Data_extract.ipynb file and find the cell cointaing following code:
```bash
  filenames = []
for file in os.listdir('F:/ML/T20 Score Predicter/Dataset/Data'):
    filenames.append(os.path.join('F:/ML/T20 Score Predicter/Dataset/Data',file))
```
Replace the ( location_part according to your location )

```bash
  Execute All the cells one by one from Data_extract.ipynb file
```

After that 

```bash
  Execute All the cells one by one from Feature_extract.ipynb file
```

Lastly

```bash
  Run app.py file and after execution type streamlit run app.py on terminal of IDE (For eg)
```




## Screenshot

![App Screenshot](https://github.com/Suyash9422/tp/blob/main/Screenshot%20(767).png?raw=true)








You Will Be Redirected to the website And It's All !!!

```bash
Hope it Helps You . And there is a video also in the folder for running app.py you can also watch that  
``` 