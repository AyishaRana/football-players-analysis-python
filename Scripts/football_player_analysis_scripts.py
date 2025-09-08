{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28ee008d-d03d-4225-8113-09602b1defad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "df=pd.read_excel(r'C:\\Users\\AYISHA RANA K\\Desktop\\python data analyst duo\\football analysis case study.xlsx')\n",
    "df.head()\n",
    "type(df)\n",
    "df.columns\n",
    "df['Date']=pd.to_datetime(df['Date'],errors='coerce')\n",
    "unique_players_competition = df[['Player Name', 'Age','competition']].drop_duplicates()\n",
    "unique_players_competition\n",
    "age_cnt=df.groupby(df['Age'].apply(lambda x: '<25' if x<25 else '>25'))['Player Name'].nunique().reset_index(name='count')\n",
    "age_cnt\n",
    "result=df.groupby('competition')['Player Name'].nunique().reset_index(name='number of players')\n",
    "result\n",
    "goals_assists=df.groupby('Player Name')[['Goals','Assists']].sum()\n",
    "goals_assists=goals_assists.sort_values(by='Goals',ascending=False)\n",
    "goals_assists['Total contribution']=goals_assists['Goals'] + goals_assists['Assists']\n",
    "goals_assists\n",
    "avg=df.groupby('Player Name')[['Shots','PS%','AerialsWon','Rating']].mean().reset_index().round(0)\n",
    "avg.columns=['Player Name', 'Avg Shots', 'Avg PS%', 'Avg  AerialsWon', 'Avg Rating']\n",
    "avg=avg.sort_values(by=['Avg Shots', 'Avg PS%', 'Avg  AerialsWon', 'Avg Rating'],ascending=False).reset_index(drop=True)\n",
    "avg\n",
    "summary = df.groupby('Player Name')['Rating'].agg(mean='mean', median='median', mode=lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan).round(0).reset_index()\n",
    "summary.columns=['Player Name','mean Rating','median Rating','mode Rating']\n",
    "summary\n",
    "range=df.groupby('Player Name')['Rating'].agg(max='max',min='min',range=lambda x: x.max()-x.min()).round(0).reset_index()\n",
    "range.columns=['Player Name','Max of Rating','Min of Rating','Range']\n",
    "range=range.sort_values(by='Max of Rating',ascending=False).reset_index(drop=True)\n",
    "range\n",
    "iqr=df.groupby('Player Name')['Rating'].agg(Q1=lambda x: x.quantile(0.25),Q3=lambda x: x.quantile(0.75),IQR=lambda x: x.quantile(0.75)-x.quantile(0.25)).round(0)\n",
    "iqr\n",
    "var=df.groupby('Player Name')['Rating'].agg(variance='var',std_dev='std').round(2).reset_index()\n",
    "var.columns=['Player Name','Var. of Rating','StdDev. of Rating']\n",
    "var=var.sort_values(by=['Var. of Rating','StdDev. of Rating']).reset_index(drop=True)\n",
    "var\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
