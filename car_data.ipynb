{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Graphs to Construct:\n",
    "- hp over time\n",
    "- engine cylinders vs. hp\n",
    "- time vs. highway MPG, city MPG\n",
    "- time vs. #engine cylinder\n",
    "- engine cylinders vs. MSRP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the data\n",
    "df = pd.read_csv('car_data.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color = 'blue'>Look at your data initially to see if the range of it</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Make</th>\n",
       "      <th>Model</th>\n",
       "      <th>Year</th>\n",
       "      <th>Engine Fuel Type</th>\n",
       "      <th>Engine HP</th>\n",
       "      <th>Engine Cylinders</th>\n",
       "      <th>Transmission Type</th>\n",
       "      <th>Driven_Wheels</th>\n",
       "      <th>Number of Doors</th>\n",
       "      <th>Market Category</th>\n",
       "      <th>Vehicle Size</th>\n",
       "      <th>Vehicle Style</th>\n",
       "      <th>highway MPG</th>\n",
       "      <th>city mpg</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>MSRP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>BMW</td>\n",
       "      <td>1 Series M</td>\n",
       "      <td>2011</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>335.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>rear wheel drive</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Factory Tuner,Luxury,High-Performance</td>\n",
       "      <td>Compact</td>\n",
       "      <td>Coupe</td>\n",
       "      <td>26</td>\n",
       "      <td>19</td>\n",
       "      <td>3916</td>\n",
       "      <td>46135</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>BMW</td>\n",
       "      <td>1 Series</td>\n",
       "      <td>2011</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>300.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>rear wheel drive</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Luxury,Performance</td>\n",
       "      <td>Compact</td>\n",
       "      <td>Convertible</td>\n",
       "      <td>28</td>\n",
       "      <td>19</td>\n",
       "      <td>3916</td>\n",
       "      <td>40650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>BMW</td>\n",
       "      <td>1 Series</td>\n",
       "      <td>2011</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>300.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>rear wheel drive</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Luxury,High-Performance</td>\n",
       "      <td>Compact</td>\n",
       "      <td>Coupe</td>\n",
       "      <td>28</td>\n",
       "      <td>20</td>\n",
       "      <td>3916</td>\n",
       "      <td>36350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>BMW</td>\n",
       "      <td>1 Series</td>\n",
       "      <td>2011</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>230.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>rear wheel drive</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Luxury,Performance</td>\n",
       "      <td>Compact</td>\n",
       "      <td>Coupe</td>\n",
       "      <td>28</td>\n",
       "      <td>18</td>\n",
       "      <td>3916</td>\n",
       "      <td>29450</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>BMW</td>\n",
       "      <td>1 Series</td>\n",
       "      <td>2011</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>230.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>MANUAL</td>\n",
       "      <td>rear wheel drive</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Luxury</td>\n",
       "      <td>Compact</td>\n",
       "      <td>Convertible</td>\n",
       "      <td>28</td>\n",
       "      <td>18</td>\n",
       "      <td>3916</td>\n",
       "      <td>34500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Make       Model  Year             Engine Fuel Type  Engine HP  \\\n",
       "0  BMW  1 Series M  2011  premium unleaded (required)      335.0   \n",
       "1  BMW    1 Series  2011  premium unleaded (required)      300.0   \n",
       "2  BMW    1 Series  2011  premium unleaded (required)      300.0   \n",
       "3  BMW    1 Series  2011  premium unleaded (required)      230.0   \n",
       "4  BMW    1 Series  2011  premium unleaded (required)      230.0   \n",
       "\n",
       "   Engine Cylinders Transmission Type     Driven_Wheels  Number of Doors  \\\n",
       "0               6.0            MANUAL  rear wheel drive              2.0   \n",
       "1               6.0            MANUAL  rear wheel drive              2.0   \n",
       "2               6.0            MANUAL  rear wheel drive              2.0   \n",
       "3               6.0            MANUAL  rear wheel drive              2.0   \n",
       "4               6.0            MANUAL  rear wheel drive              2.0   \n",
       "\n",
       "                         Market Category Vehicle Size Vehicle Style  \\\n",
       "0  Factory Tuner,Luxury,High-Performance      Compact         Coupe   \n",
       "1                     Luxury,Performance      Compact   Convertible   \n",
       "2                Luxury,High-Performance      Compact         Coupe   \n",
       "3                     Luxury,Performance      Compact         Coupe   \n",
       "4                                 Luxury      Compact   Convertible   \n",
       "\n",
       "   highway MPG  city mpg  Popularity   MSRP  \n",
       "0           26        19        3916  46135  \n",
       "1           28        19        3916  40650  \n",
       "2           28        20        3916  36350  \n",
       "3           28        18        3916  29450  \n",
       "4           28        18        3916  34500  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# look at the data\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Make</th>\n",
       "      <th>Model</th>\n",
       "      <th>Year</th>\n",
       "      <th>Engine Fuel Type</th>\n",
       "      <th>Engine HP</th>\n",
       "      <th>Engine Cylinders</th>\n",
       "      <th>Transmission Type</th>\n",
       "      <th>Driven_Wheels</th>\n",
       "      <th>Number of Doors</th>\n",
       "      <th>Market Category</th>\n",
       "      <th>Vehicle Size</th>\n",
       "      <th>Vehicle Style</th>\n",
       "      <th>highway MPG</th>\n",
       "      <th>city mpg</th>\n",
       "      <th>Popularity</th>\n",
       "      <th>MSRP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11909</th>\n",
       "      <td>Acura</td>\n",
       "      <td>ZDX</td>\n",
       "      <td>2012</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>300.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>all wheel drive</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Crossover,Hatchback,Luxury</td>\n",
       "      <td>Midsize</td>\n",
       "      <td>4dr Hatchback</td>\n",
       "      <td>23</td>\n",
       "      <td>16</td>\n",
       "      <td>204</td>\n",
       "      <td>46120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11910</th>\n",
       "      <td>Acura</td>\n",
       "      <td>ZDX</td>\n",
       "      <td>2012</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>300.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>all wheel drive</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Crossover,Hatchback,Luxury</td>\n",
       "      <td>Midsize</td>\n",
       "      <td>4dr Hatchback</td>\n",
       "      <td>23</td>\n",
       "      <td>16</td>\n",
       "      <td>204</td>\n",
       "      <td>56670</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11911</th>\n",
       "      <td>Acura</td>\n",
       "      <td>ZDX</td>\n",
       "      <td>2012</td>\n",
       "      <td>premium unleaded (required)</td>\n",
       "      <td>300.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>all wheel drive</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Crossover,Hatchback,Luxury</td>\n",
       "      <td>Midsize</td>\n",
       "      <td>4dr Hatchback</td>\n",
       "      <td>23</td>\n",
       "      <td>16</td>\n",
       "      <td>204</td>\n",
       "      <td>50620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11912</th>\n",
       "      <td>Acura</td>\n",
       "      <td>ZDX</td>\n",
       "      <td>2013</td>\n",
       "      <td>premium unleaded (recommended)</td>\n",
       "      <td>300.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>all wheel drive</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Crossover,Hatchback,Luxury</td>\n",
       "      <td>Midsize</td>\n",
       "      <td>4dr Hatchback</td>\n",
       "      <td>23</td>\n",
       "      <td>16</td>\n",
       "      <td>204</td>\n",
       "      <td>50920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11913</th>\n",
       "      <td>Lincoln</td>\n",
       "      <td>Zephyr</td>\n",
       "      <td>2006</td>\n",
       "      <td>regular unleaded</td>\n",
       "      <td>221.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>AUTOMATIC</td>\n",
       "      <td>front wheel drive</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Luxury</td>\n",
       "      <td>Midsize</td>\n",
       "      <td>Sedan</td>\n",
       "      <td>26</td>\n",
       "      <td>17</td>\n",
       "      <td>61</td>\n",
       "      <td>28995</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Make   Model  Year                Engine Fuel Type  Engine HP  \\\n",
       "11909    Acura     ZDX  2012     premium unleaded (required)      300.0   \n",
       "11910    Acura     ZDX  2012     premium unleaded (required)      300.0   \n",
       "11911    Acura     ZDX  2012     premium unleaded (required)      300.0   \n",
       "11912    Acura     ZDX  2013  premium unleaded (recommended)      300.0   \n",
       "11913  Lincoln  Zephyr  2006                regular unleaded      221.0   \n",
       "\n",
       "       Engine Cylinders Transmission Type      Driven_Wheels  Number of Doors  \\\n",
       "11909               6.0         AUTOMATIC    all wheel drive              4.0   \n",
       "11910               6.0         AUTOMATIC    all wheel drive              4.0   \n",
       "11911               6.0         AUTOMATIC    all wheel drive              4.0   \n",
       "11912               6.0         AUTOMATIC    all wheel drive              4.0   \n",
       "11913               6.0         AUTOMATIC  front wheel drive              4.0   \n",
       "\n",
       "                  Market Category Vehicle Size  Vehicle Style  highway MPG  \\\n",
       "11909  Crossover,Hatchback,Luxury      Midsize  4dr Hatchback           23   \n",
       "11910  Crossover,Hatchback,Luxury      Midsize  4dr Hatchback           23   \n",
       "11911  Crossover,Hatchback,Luxury      Midsize  4dr Hatchback           23   \n",
       "11912  Crossover,Hatchback,Luxury      Midsize  4dr Hatchback           23   \n",
       "11913                      Luxury      Midsize          Sedan           26   \n",
       "\n",
       "       city mpg  Popularity   MSRP  \n",
       "11909        16         204  46120  \n",
       "11910        16         204  56670  \n",
       "11911        16         204  50620  \n",
       "11912        16         204  50920  \n",
       "11913        17          61  28995  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color = 'blue'> Ensure data frame as no missing value, names are callable, and the values make sense for each column</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# change the columns names so their easy to call\n",
    "df.columns = [name.lower().replace(' ', '_') for name in (list(df.columns))]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11914, 16)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head() # ensure the column names are lowercased and contain no spaces\n",
    "df.shape #11,914 rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n",
      "Consecutive\n"
     ]
    }
   ],
   "source": [
    "# Check to see if years are consecutive\n",
    "list_years = list(sorted(list(df['year'].unique())))\n",
    "for index in range(0,(len(list_years))):\n",
    "    try:\n",
    "        if list_years[index+1] == (list_years[index] +1):\n",
    "            print('Consecutive')\n",
    "    except IndexError:\n",
    "        break\n",
    "# consecutive years\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check the columns of interest to see if there are missing values\n",
    "df['year'].isna().sum() # 0\n",
    "df['engine_hp'].isna().sum() # 69\n",
    "df['engine_cylinders'].isna().sum() # 30\n",
    "df['highway_mpg'].isna().sum() # 0\n",
    "df['city_mpg'].isna().sum() # 0\n",
    "df['msrp'].isna().sum() # 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11816, 16)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get rid of rows where there is a NaN value in the following columns\n",
    "df = df.dropna(axis= 0, subset=['engine_hp','engine_cylinders'])\n",
    "df.shape #11,816 rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['premium unleaded (required)', 'regular unleaded',\n",
       "       'premium unleaded (recommended)', 'flex-fuel (unleaded/E85)',\n",
       "       'diesel', 'flex-fuel (premium unleaded recommended/E85)',\n",
       "       'electric', 'natural gas',\n",
       "       'flex-fuel (premium unleaded required/E85)', nan], dtype=object)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check if the columns of interest have reasonable data\n",
    "df['engine_hp'].describe() # this looks reasonable\n",
    "df['engine_cylinders'].describe() # there is a min of 0 cylinders, which doesn't make sense\n",
    "df['highway_mpg'].describe() # there is a max value of 354 miles per gallon, this doesn't necessarily make sense\n",
    "df['city_mpg'].describe() # max 137, this doesn't make sense\n",
    "df['msrp'].describe() # makes sense\n",
    "\n",
    "# because there are values that seem extreme such as the MPG and engine cylinder count of 0, \n",
    "# I suspect there are electric vehicles in this data frame, so I'll be taking those out.\n",
    "df['engine_fuel_type'].unique() # there are electric vehicles in this df. plot to see how much outliers will affect my data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[df.engine_fuel_type != 'electric']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11803, 16)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color = 'blue'>OLS with Linear Algebra</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our linear regression equation can be represented as:\n",
    "\n",
    "$ y = Xb + error $\n",
    "\n",
    "to begin with, we are going to assume that on average, the error is equal to 0. (We can assume this due our assumptions for linear algebra)\n",
    "\n",
    "$ y = Xb  + 0 $ --> $ y = Xb $\n",
    "\n",
    "We want to solve for b. That means we need to isolate it on one side of the equation therefore we can take the inverse of this function. Let's multily by the inverse. Let's calculate it:\n",
    "\n",
    "$ X^{-1} $"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "We can only calculate an inverse of a square matrix. We can make accomplish this be multiplying the matrix by its transpose.\n",
    "\n",
    "$X^{T} y = X^{T} X b $\n",
    "\n",
    "Now we can take the inverse of the new square matrix $X^{T}X$ and multiply it to both sides to isolate with b vector\n",
    "\n",
    "$ (X^{T}X)^{-1} X^{T}y = (X^{T}X)^{-1} (X^{T}X)b$ \n",
    "- <font color = 'blue'>**You have to multiply by the tranpose first to get a sqaure matrix to then multiply by the inverse, because as we know, a matrix, multiplied by its inverse is identity matrix. If you didn't take the transposition, you couldn't do X{T}X if your X wasn't sqaured to begin with**</font>\n",
    "\n",
    "$(X^{T}X)^{-1}X^{T}y = I b$\n",
    "\n",
    "We are left with the identity matrix multiplied by b, which is simply equal to b\n",
    "\n",
    "$b = (X^{T}X)^{-1}X^{T}y  $\n",
    "\n",
    "Now, solve for b!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df['msrp']\n",
    "x_df = df[['engine_hp','engine_cylinders','highway_mpg', 'city_mpg']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/PB/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "x_df['constant'] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_matrix = x_df.values # put it in array/matrix form"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5,)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_transposed = x_matrix.T\n",
    "xt_x = x_transposed.dot(x_matrix) # need to multiple by transpose to get a square matrix \n",
    "xt_x.shape # need square matrix to take inverse (5,5)\n",
    "xtx_inv = np.linalg.inv(xt_x) # (5,5)\n",
    "xtx_inv.shape\n",
    "xty = x_transposed.dot(y)\n",
    "xty.shape #(5,)\n",
    "x_hat = xtx_inv.dot(xty) \n",
    "x_hat.shape # (5,)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "lr = LinearRegression()\n",
    "\n",
    "skl_x = x_df.drop(columns = 'constant')\n",
    "lr.fit(skl_x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 327.47, 7997.16,  391.06, 1873.62])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.round(lr.coef_,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-132656.27"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.round(lr.intercept_,2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$$ MSRP = 327.47(hp) + 7997.16(cylinders) + 391.06(highwayMPG) + 1873.62(cityMPG) - 132656.27$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.46430105834029933"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lr.score(skl_x,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### <font color = 'blue'> The R-sqaured is 0.46, which is not good. So my linear regression model is not very predictive </font>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <font color = 'blue'>Plot some features </font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_ = list((df.groupby('year').mean())['engine_hp']) # find the average hp for a given year\n",
    "x_ = list(df['year'].unique())\n",
    "fig, ax = plt.subplots(figsize=(15,5))\n",
    "ax.set_xlabel('Year')\n",
    "ax.set_ylabel('Average hp')\n",
    "sns.barplot(ax= ax, x = x_, y = y_ ).set_title('Average hp over time');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_ = list((df.groupby('vehicle_style').mean())['engine_cylinders']) # find the average hp for a given year\n",
    "x_ = list(df['vehicle_style'].unique())\n",
    "fig, ax = plt.subplots(figsize=(20,5))\n",
    "ax.set_xlabel('Vehicle Type')\n",
    "ax.set_ylabel('Average # of cylinders')\n",
    "sns.barplot(ax= ax, x = x_, y = y_ ).set_title('Average # cylinders by vehicle type');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_ = list(df['engine_cylinders'].unique())\n",
    "y_ = list((df.groupby('engine_cylinders').mean())['engine_hp'])\n",
    "fig, ax = plt.subplots(figsize=(15,5))\n",
    "ax.set_xlabel('# of cylinders')\n",
    "ax.set_ylabel('Average hp')\n",
    "sns.barplot(ax= ax, x = x_, y = y_).set_title('# of cylinders vs. average hp');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABI8AAAFACAYAAAA1c1zEAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzt3Xm4XXV9L/73x0AIQ0SEqCCBaEEcQCJEWlRSBAfk3qLQKuAUEEXqiLZ68bb1h3rVaLFX0P6weGW49yKj4DxUBSpWpQQNGkRqsCiRFAEnoqUS+N4/9g4eICvDOfucvZO8Xs+zn7P3Gt9n7XXWXuezvt+1q7UWAAAAAFidhww7AAAAAACjS/EIAAAAgE6KRwAAAAB0UjwCAAAAoJPiEQAAAACdFI8AAAAA6KR4BAAAAEAnxSMAAAAAOikeAQAAANBps2EHWBc77LBDmzNnzrBjAAAAAGw0rrnmmttba7PWNt0GUTyaM2dOFi1aNOwYAAAAABuNqvrxukyn2xoAAAAAnRSPAAAAAOikeAQAAABApw3inkcAAADA6Lr77ruzbNmy3HXXXcOOwmrMmDEjO++8czbffPNxza94BAAAAEzIsmXLMnPmzMyZMydVNew4jNFayx133JFly5blMY95zLiWodsaAAAAMCF33XVXtt9+e4WjEVRV2X777SfUKkzxCAAAAJgwhaPRNdH3RvEIAAAAgE7ueQQAAAAM1CU3LB/o8o7YY8e1TrPNNttkxYoV970+++yzs2jRonz4wx/ORz7ykWy11VZ5+ctf3jn/2Omn0jHHHJMLL7wwt956a2bOnJkkeeMb35jTTjstt912W3bYYYdMmzYte+21V1auXJknPOEJOeecc7LVVlvl1ltvzZve9KZ861vfynbbbZfp06fnrW99aw4//PCBZtTyCAAAANionXDCCWssHA3bbrvtlk996lNJknvvvTeXX355Hv3oR983fsstt8zixYuzZMmSTJ8+PR/5yEfSWssLXvCCzJ8/Pz/60Y9yzTXX5Pzzz8+yZcsGnk/xCAAAANionXzyyTnllFOSJFdffXWe/OQnZ//9989b3vKW7LnnnvdNd8stt+SQQw7J7rvvnre+9a1JkgsvvDBvfvObkySnnnpqHvvYxyZJbrzxxjzjGc9Ikrzzne/MU5/61Oy55545/vjj01rLjTfemH322ee+Zf/whz/Mvvvuu9p8Rx99dC644IIkyRVXXJGnP/3p2Wyz1XcWO+CAA7J06dJcdtllmT59ek444YT7xu266655/etfP65ttCa6rQFAh0E3t14X69IkGybCfg3Axuo//uM/Mnfu3Pte//znP89hhx32oOmOPfbYnHHGGXna056Wk0466X7jFi9enO985zvZYostsscee+T1r3995s+fn7/9279Nklx55ZXZfvvt89Of/jRf//rXc8ABByRJXve61+Xtb397kuRlL3tZPvvZz+ZP/uRPsu2222bx4sWZO3duzjrrrBxzzDGrzb777rvnU5/6VH7xi1/kvPPOy0tf+tJ84QtfeNB0K1euzBe+8IUccsghue666+5XnJpMWh4BAAAAG7xVXbtWPd75znc+aJpf/vKXufPOO/O0pz0tSfLiF7/4fuMPPvjgbLvttpkxY0ae+MQn5sc//nEe9ahHZcWKFbnzzjtz880358UvfnG+9rWv5corr7yveHT55ZfnD//wD7PXXnvlsssuy3XXXZckeeUrX5mzzjor99xzTy644IIHrW+sI444Iueff36uuuqq+5a7yqrC2Lx587LLLrvkuOOOe9D8r33ta7P33nvnqU996vptuHWg5REAAEOlNRQAU6W1tsbxW2yxxX3Pp02blpUrVyZJ9t9//5x11lnZY489csABB+TMM8/MN7/5zXzgAx/IXXfdlde85jVZtGhRZs+enZNPPjl33XVXkuRP//RP8453vCMHHXRQ9t1332y//fad6z7qqKOyzz77ZMGCBXnIQ+7f1mdVYWysJz3pSfnEJz5x3+u///u/z+2335558+at28ZYD1oeAQAAAJuE7bbbLjNnzsy3vvWtJMn555+/TvPNnz8/p5xySubPn5+nPOUpufzyy7PFFltk2223va9QtMMOO2TFihW5+OKL75tvxowZee5zn5s///M/z7HHHrvGdeyyyy5597vfnde85jXrlOmggw7KXXfdldNPP/2+Yb/97W/Xad71peURAAAAMFCj3MLzYx/7WF71qldl6623zoEHHphtt912rfMccMABufnmmzN//vxMmzYts2fPzuMf//gkycMe9rC86lWvyl577ZU5c+Y8qNvYS17yklxyySV5znOes9b1vPrVr17n36Oq8slPfjJvetOb8v73vz+zZs3K1ltvnfe9733rvIx1XtfammyNgnnz5rVFixYNOwYAmxhdadgYjeJ+PYqZAFg/119/fZ7whCcMO8Y6WbFiRbbZZpskycKFC7N8+fKceuqpk7a+U045Jb/61a/yrne9a9LWsS5W9x5V1TWttbX2c9PyCAAAANhkfO5zn8t73/verFy5MrvuumvOPvvsSVvX4YcfnhtvvDGXXXbZpK1jKigeAQAAAJuMI488MkceeeSUrOvSSy+dkvVMNjfMBgAAAKCTlkcAsIFwXxgAAIZByyMAAAAAOikeAQAAANBJtzUAAABgsD5eg13ei9taJ/n3f//3nHjiibn66quzxRZbZM6cOfngBz+YbbbZJm94wxty8cUXZ/Hixbnlllty6KGHrvOqzz777Bx77LH5yle+koMPPjhJ70bYRxxxRC666KL82Z/9WQ488MAsX748M2bMyDbbbJMzzzwze+yxR1auXJm3v/3tueiii7L11lsnSV74whfmr/7qr8a3HYZEyyMAAABgg9Zay+GHH54DDzwwN954Y77//e/nPe95T2699dbstNNOufjii5Mkixcvzuc///n1Xv5ee+2V8847777X559/fvbee+/7TXPuuefm2muvzYIFC/KWt7wlSfLXf/3XueWWW/K9730vixcvzpVXXpm77757Ar/pcCgeAQAAABu0yy+/PJtvvnlOOOGE+4bNnTs3BxxwQG666absueee+d3vfpe3v/3tueCCCzJ37txccMEF2X333XPbbbclSe69997stttuuf322x+0/AMOOCD/8i//krvvvjsrVqzI0qVLM3fu3NVmmT9/fpYuXZrf/va3+ehHP5oPfehDmTFjRpJk5syZOfnkkwe/ASaZbmsAAADABm3JkiXZd9991zjN9OnT8853vjOLFi3Khz/84STJD37wg5x77rk58cQT85WvfCV77713dthhhwfNW1V51rOelS996Uv51a9+lcMOOyz/9m//ttr1fOYzn8lee+2VpUuXZpdddsnMmTMn/gsOmeIRAACwwbvkhuVTvs4j9thxytcJDNYrXvGKPP/5z8+JJ56YM888M8cee2zntEcddVROO+20/OpXv8oHPvCBvOc977nf+Je85CXZcsstM2fOnHzoQx/KL37xi/uNP+uss3LqqafmjjvuyDe+8Y3Mnj17Un6nyaDbGgAAALBBe9KTnpRrrrlmveebPXt2HvnIR+ayyy7LVVddlec973md0+63335ZsmRJbr/99jzucY970Phzzz03ixcvzic/+cnMnj07u+22W37yk5/kzjvvTJIce+yxWbx4cbbddtvcc8896511mBSPAAAAgA3aQQcdlP/8z//MRz/60fuGXX311fmnf/qn+003c+bM+4o5q7zyla/MS1/60rzoRS/KtGnT1rie9773vQ9qcdRlq622ynHHHZfXve51ueuuu5Ik99xzT373u9+t0/yjRLc1AABgvegiBqzVi9uUrq6qcumll+bEE0/MwoULM2PGjMyZMycf/OAH7zfdM5/5zCxcuDBz587N2972thx55JE57LDDcuyxx66xy9oqa2qZtDrvfve78zd/8zfZc889M3PmzGy55ZZZsGBBdtppp/VazrApHgEAAAAbvJ122ikXXnjhasctWbIkSfLwhz88V1999f3GXXvttdl7773z+Mc/frXzHnPMMTnmmGMeNPzss8++7/kVV1yx2nk333zzLFy4MAsXLlz7LzDCFI8AAACATdLChQtz+umn59xzzx12lJHmnkcAAADAJumkk07Kj3/84zzjGc8YdpSRpngEAAAATFhrU3ufI9bdRN8bxSMAAABgQmbMmJE77rhDAWkEtdZyxx13ZMaMGeNehnseAQAAABOy8847Z9myZbntttuGHYXVmDFjRnbeeedxz694BAAAAEzI5ptvnsc85jHDjsEk0W0NAAAAgE6TVjyqqtlVdXlVXV9V11XVG/vDT66qn1bV4v7j0MnKAAAAAMDETGa3tZVJ/qK19u2qmpnkmqr6cn/c/2ytnTKJ6wYAgI3GJTcsn/J1HrHHjlO+TgBG06QVj1pry5Ms7z+/s6quT/LoyVofAAAAAIM3Jfc8qqo5SZ6S5Kr+oNdV1Xer6syq2q5jnuOralFVLXK3dgAAAIDhmPTiUVVtk+QTSU5srf06yelJ/iDJ3PRaJn1gdfO11s5orc1rrc2bNWvWZMcEAAAAYDUmtXhUVZunVzg6t7V2SZK01m5trd3TWrs3yUeT7DeZGQAAAAAYv8n8trVK8rEk17fW/m7M8LF33js8yZLJygAAAADAxEzmt609PcnLknyvqhb3h/33JEdX1dwkLclNSV49iRkAAAAAmIDJ/La1ryep1Yz6/GStEwAAAIDBmpJvWwMAAABgwzSZ3dZgXC65YfmU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\n",
      "text/plain": [
       "<Figure size 1440x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_ = list(df['year'].unique())\n",
    "y1_ = list((df.groupby('year').mean())['highway_mpg'])\n",
    "y2_ = list((df.groupby('year').mean())['city_mpg'])\n",
    "fig, ax = plt.subplots(figsize=(20,5))\n",
    "plt.bar(x_,y1_,color = 'lightblue');\n",
    "plt.bar(x_,y2_, color = 'orange');\n",
    "plt.xlabel('Year')\n",
    "plt.ylabel('MPG')\n",
    "plt.gca().legend(('Highway MPG','City MPG'))\n",
    "plt.xticks(x_);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_ = list(df['year'].unique())\n",
    "y_ = list((df.groupby('year').mean())['engine_cylinders'])\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(15,5))\n",
    "ax = plt.gca()\n",
    "ax.grid(which='major', axis='both', linestyle='--')\n",
    "\n",
    "plt.xlabel('Year')\n",
    "plt.xticks(x_)\n",
    "plt.ylabel('Average # of Cylinders')\n",
    "sns.pointplot(x = x_, y = y_, color='red').set_title('Average # of Cylinders per Year');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_ = list(df['engine_cylinders'].unique())\n",
    "y_ = list((df.groupby('engine_cylinders').mean())['msrp'])\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(15,5))\n",
    "ax = plt.gca()\n",
    "ax.grid(which='major', axis='both', linestyle='--')\n",
    "\n",
    "plt.xlabel('# of Engine Cylinders')\n",
    "plt.xticks(x_)\n",
    "plt.ylabel('MSRP')\n",
    "sns.pointplot(x = x_, y = y_, color='red').set_title('MSRP by # of engine cylinders');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
