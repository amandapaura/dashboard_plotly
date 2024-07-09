# dashboard_plotly
## <font color='lime'> Codes to create a Dashboard with Plotly - Stock Price Data </font>

![alt text](https://github.com/amandapaura/dashboard_plotly/blob/main/imagem%20dash.png?raw=true)

In this project, I created a sample dashboard using *Plotly Dash* with financial data from *Yahoo Finance*.

The project contains 4 modules:

1. The *"findata.py"* module generates the financial data we will display in the graphs. It contains a class that fetches asset data from the Yahoo Finance API, with methods that perform financial calculations and return a dataframe.

2. The *"graficos.py"* and *"gera_graficos.py"* modules are an abstract factory for different types of graphs. The first module generates the graphs (in this work, I included line and scatter plots), and the second creates the layout of the graphs ready to be displayed in Dash.

3. The *"app.py"* module is the construction of the Dash app. We need to insert the financial data, create and generate the graphs, texts, and everything we want, and use Plotly Dash to assemble the dashboard. The main function generates the graph on localhost.

To run the graph, just open the terminal in the directory and run the command: python app.py

The idea is for you to use the structure to experiment and create different dashboard layouts.

=)


