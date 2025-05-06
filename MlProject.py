{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6d43b4f4-78a0-4e78-afc4-572898eca78d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: numpy in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (1.5.1)\n",
      "Requirement already satisfied: xgboost in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (3.0.0)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (3.9.2)\n",
      "Requirement already satisfied: seaborn in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (0.13.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: scipy>=1.6.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from scikit-learn) (1.13.1)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from scikit-learn) (1.4.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (1.2.0)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (4.51.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (1.4.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (24.1)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (10.4.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (3.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.3.1 -> 25.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install pandas numpy scikit-learn xgboost matplotlib se+++aborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4f7226de-4dfe-4693-bff1-1393551f225e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: numpy in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (1.5.1)\n",
      "Requirement already satisfied: xgboost in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (3.0.0)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (3.9.2)\n",
      "Requirement already satisfied: seaborn in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (0.13.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: scipy>=1.6.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from scikit-learn) (1.13.1)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from scikit-learn) (1.4.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (1.2.0)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (4.51.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (1.4.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (24.1)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (10.4.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from matplotlib) (3.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\abhishek kr singh\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.3.1 -> 25.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install pandas numpy scikit-learn xgboost matplotlib seaborn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5d62ecf4-7b71-4702-a374-a24436f6538f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape (2480690871.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[6], line 3\u001b[1;36m\u001b[0m\n\u001b[1;33m    data = pd.read_csv('C:\\Users\\ABHISHEK KR SINGH\\Desktop\\ml project\\AirQualityUCI.csv', sep=';', decimal=',')\u001b[0m\n\u001b[1;37m                       ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "# Load the dataset (replace 'AirQualityUCI.csv' with the actual file path)\n",
    "data = pd.read_csv('C:\\Users\\ABHISHEK KR SINGH\\Desktop\\ml project\\AirQualityUCI.csv', sep=';', decimal=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d52f9ad-11ff-4ef0-b7b6-08b7c906446f",
   "metadata": {},
   "outputs": [],
   "source": [
    "++"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
