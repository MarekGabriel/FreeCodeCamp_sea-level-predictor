import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np 
import seaborn as sns

def draw_plot():
    # Read data from file
    df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/refs/heads/main/epa-sea-level.csv', 
                     header = 0, index_col = 0)


    # Create scatter plot
    # Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.

    #ustawiam tło wykresu na białe z czarną siatką
    sns.set_style('whitegrid')
    #zdefiniowanie obiektów: figury oraz pojedynczego układu osi
    fig, axis = plt.subplots(nrows = 1, ncols = 1, figsize = (12,6))
    
    ### matplotlib.pyplot.scatter() służy do tworzenia wykresów punktowych rozrzutu (scatter plot), czyli takich, gdzie dane są reprezentowane 
    ### jako pojedyncze punkty na płaszczyźnie. Lepszy niż plot(), bo pozwala sterować wyglądem każdego punktu osobno.
    ### Składnia: plt.scatter(x = None, y = None, s = None, c = None, alpha = None, cmap = None, marker = string, data = )
    ### Parametry:
    ### x, y - np. kolumny z ramki danych
    ### s - rozmiar rysowanych punktów (może być liczbą lub tablicą np. kolumną z ramki danych i wówczas punkty mają różny rozmiar)
    ### c - definiowany jako string (np. 'red'), ale może też być tablicą np. kolumną z ramki danych
    ### cmap - mapa kolorów (np. 'viridis', 'plasma'); generalnie colormap mówi jak zamienić liczby z parametru 'c' na kolory, czyli
    ###        działa tylko wtedy gdy 'c' jest tablicą
    ### alpha - przezroczystość od 0 (przezroczyste) do 1 (pełne)
    ### marker - kształt rysowanych punktów np. 'o' – kółko (domyślne), 'x' – krzyżyk, '^' – trójkąt, 'd' - diament
    ### data - źródło danych np. pandas.DataFrame
    
    ### UWAGA - styl pyplot vs. styl obiektowy [tj.: 'fig, axis = plt.subplots()']
    ### 1. plt.scatter() - oś ukryta (aktualna tj. Python sam "zgaduje" gdzie rysować wykres)
    ### 2. axis.scatter() - oś jawnie podana (nie trzeba już podawać '.plt', bo axis jest obiektem zdefiniowanym wg biblioteki plt)
    
    # przykład:
    # plt.scatter(x = df.index, y = 'CSIRO Adjusted Sea Level', s = 15, c = 'Lower Error Bound', alpha = 0.3, 
    #            cmap = 'viridis', marker = 'd', data = df);

    #na obiekcie układu osi rysujemy wykres rozrzutu
    axis.scatter(x = df.index, y = 'CSIRO Adjusted Sea Level', s = 15, c = 'green', alpha = 0.3, data = df);


    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
    # Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 
    # to predict the sea level rise in 2050.
    
    ### Funkcja scipy.stats.linregress() wspomaga wykonanie prostej regresji liniowej między dwiema zmiennymi x i y (tj. znajduje parametry
    ### dla y = a * x + b), gdzie a → nachylenie (slope) oraz b → punkt przecięcia z osią Y (intercept). Ponadto zwraca również:
    ### result.rvalue - korelacja (R)
    ### result.pvalue - istotność statystyczna
    ### result.stderr - błąd nachylenia
    ### result.intercept_stderr - błąd standardowy wyrazu wolnego

    #regresja liniowa zależności y (poziomu mórz) od x (lat od 1880r.)
    lin_reg = linregress(x = df.index, y = df['CSIRO Adjusted Sea Level'])
    #lin_reg.slope

    #indeks lat zamieniam na tablicę nd-array
    years = np.array(df.index)
    #wyznaczam ostatni rok, za który mamy dane
    max_years = years.max()
    #wyznaczam dodatkową tablicę z latami powyżej ostatniego roku, za który mamy dane, aż do 2050r.
    additional = np.arange(max_years + 1, 2051)
    #print(additional)
    #złączenie lat w jedną tablicę aż do 2050r.
    x1 = np.concatenate((years, additional), axis = 0)

    #wyznaczenie wartości regresji liniowej y = ax + b (poziomu mórz) od x (lat od 1880r. do 2050r.)
    y1 = lin_reg.slope * x1 + lin_reg.intercept
    #print(x1, '\n', y1)
    #y1.shape

    #rysowanie linii regresji (first line of best fit) na ustalonym układzie osi
    axis.plot(x1, y1, 'blue')

    
    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line 
    # also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.

    #ustalenie nr pozycji roku 2000 w indeksie ramki danych
    pozycja2000 = df.index.get_loc(2000)
    #wycinek lat od 2000r.
    years_cut = df.index[pozycja2000:]
    #wycinek poziomu mórz od 2000r.
    CSIRO_Adj_Sea_Level_cut = df['CSIRO Adjusted Sea Level'].iloc[pozycja2000:]

    #regresja liniowa zależności y (poziomu mórz) od x (lat od 2000r.)
    lin_reg2 = linregress(x = years_cut, y = CSIRO_Adj_Sea_Level_cut)
    #lin_reg2

    #indeks wycinka lat zamieniam na tablicę nd-array
    years_cut = np.array(years_cut)
    #złączenie wycinka lat w jedną tablicę aż do 2050r.
    x2 = np.concatenate((years_cut, additional), axis = 0)
    
    #wyznaczenie wartości regresji liniowej y = ax + b (poziomu mórz) od x (lat od 2000r. do 2050r.)
    y2 = lin_reg2.slope * x2 + lin_reg2.intercept
    #y2.shape

    #rysowanie linii regresji (second line of best fit) na ustalonym układzie osi
    axis.plot(x2, y2, 'red')


    # Add labels and title
    # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

    #nadanie nazwy osi X
    axis.set_xlabel(df.index.name)
    #nadanie nazwy osi Y
    axis.set_ylabel('Sea Level (inches)')
    #nadanie tytułu wykresu
    axis.set_title('Rise in Sea Level')


    
    # Metoda matplotlib.pyplot.gca() to "Get Current Axes" czyli „daj mi aktualną oś (Axes), na której rysuję”. 
    # Zwraca ona domyślną oś, na której wykonywano ostatnio operacje.
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()