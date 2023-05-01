# House_Price_Prediction_App
With this application, the house price is estimated by using regression and ensemble models in line with the information entered by the user.
********************************************
# Project Overview
* ** The goal of the Project**: I developed a model that finds the most suitable price for the house in line with the features entered by the user.With this model, the landlord does not sell his house at a high price. Thus, it does not reduce the probability of the house being sold.Also, the landlord does not sell his house at a low price. Thus, there is no loss.

* The variables in the dataset I use for this model are as follows (the dataset before the data cleaning phase):
    * Id: This column contains a unique ID number for each house.
    * MSSubClass: This column indicates the construction class of the house. For example, it indicates whether it is a single-family home or a multi-family home.
    * MSZoning: This column shows the zoning status of the house's location. For example, the home may be in a commercial, residential, or industrial area.
    * LotFrontage: This column measures the length of the road facing the front of the house parcel.
    * LotArea: This column measures the total area of the parcel of the house.
    * Street: This column indicates whether the house is on a street or street, or in a rural area.
    * Alley: This column indicates whether the house has an alleyway to access the backyard.
    * LotShape: This column indicates the shape of the parcel of the house (straight, corner, curved, etc.).
    * LandContour: This column indicates the surface shape of the parcel of the house (flat, curved, etc.).
    * Utilities: This column indicates whether the house has any essential services (water, electricity, gas, etc.).
    * LotConfig: This column indicates the position of the house parcel (corner, flat, etc.).
    * LandSlope: This column indicates the slope of the parcel of the house (none, light, medium, strong).
    * Neighborhood: This column indicates the neighborhood where the house is located.
    * Condition1 and Condition2: These columns indicate conditions around the house (main road, railroad, park, etc.).
    * BldgType: This column indicates the type of house (single-family house, multi-family house, etc.).
    * HouseStyle: This column indicates the architectural style of the house (ranch, two-story, three-story, etc.).
    * OverallQual: This column indicates the overall quality of the home on a scale of 1 to 10.
    * OverallCond: This column indicates the general condition of the house on a scale of 1 to 10.
    * YearBuilt: This column indicates the year the house was built.
    * YearRemodAdd: This column indicates the year the house was last renovated.
    * RoofStyle: This column indicates the roof type of the house (attic, hip, flat, etc.).
    * RoofMatl: This column indicates the material of the roof of the house (mostly cement etc.)
* For this project I used the LigthGBM model
*	I did the web integration using streamlit library


# RESOURCES AND LIBRARIES
* Python:3.10.9
* Libraries : pandas,numpy,seaborn,matplotlib,sklearn,stasmodels,lazypredict, warnings and pickle 

# DATA CLEANING
* I deleted columns with more than 45% null values in the dataset

![alt text](https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/null_percent.png "Null Percent")

 * I used get_dummies method for categorical variables
 # FEATURE SELECTION
 * I got the columns with a correlation "greater than 0.50" or "less than -0.50" with the dependent variable SalePrice
* The state of the dataset after the above process is applied is as follows
    * OverallQual
    * YearBuilt
    * YearRemodAdd
    * TotalBsmtSF
    * 1stFlrSF
    * GrLivArea
    * FullBath
    * TotRmsAbvGrd
    * GarageCars
    * GarageArea
    * SalePrice
    * ExterQual_TA
    * BsmtQual_Ex
    * KitchenQual_Ex
    * KitchenQual_TA
* For the categorical variables BsmtQual and ExterQual, I do not want to leave these variables alone because there is more than one category in the main data set. For this reason, I added 1 categorical variable with the highest correlation with SalePrice. These variables are: ExterQual_Ex and BsmtQual_TA

# EDA
* I visualized the correlation relationship between the data with a heatmap

![alt text](https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/heatmap.png "Heatmap")

* I drew a boxplot for OverQuall and SalePrice

![alt text](https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/overallqual_boxplot.png " OverQuall and SalePrice Boxplot")

* I created a variable named Century and plotted a boxplot to examine the distribution of house prices related to this variable.

![alt text](https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/century_boxplot.png "Century Boxplot")

* I listed the year values in the YearBuilt variable. Finally, I plotted the lineplot to examine the change in SalePrice values over the years.

![alt text]( https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/year_saleprice.png "YearBuilt and SalePrice Lineplot")

# MODEL SELECTOIN

* First, I created an OLS object to examine the significance of the variables for the model.

![alt text]( https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/OLS_r2.png "OLS_R2")

![alt text]( https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/OLS_p.png "OLS_Pvalue")

* I used the lazypredict library to find the most suitable model

![alt text](https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/lazypredict.png "LazyPredict")

* Finally, I decided to use the lightgbm model and the r2 value of my model was =0.89. To be sure of this value, I cross-validated and chose the cv value of 5. As a result, the r2 value I obtained is = 0.86

#APP

After saving my model and standard scaler values using the pickle library, I performed the web integration of my model with streamlit.

![alt text]( https://github.com/gamzeaslan/House_Price_Prediction_App/blob/main/year_saleprice.png "YearBuilt and SalePrice Lineplot")



