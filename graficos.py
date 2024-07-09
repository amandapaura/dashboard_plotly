import plotly
import plotly.express as px

class Dados:
    def __init__(self, df, x='Date',y=None):
        self.df = df
        self.x = x
        if y == None:
            self.y = df.columns
        else:
            self.y = y

class Linha(Dados):
    def __init__(self, title,df, x='Date',y=None):
        super().__init__(df, x='Date',y=None)
        self.title = title

    def plot(self):
        if self.x == 'Date':
            fig = px.line(self.df, x=self.x, y=self.y,
                        hover_data={"Date": "|%B %d, %Y"},
                        title=self.title)
        else:
            fig = px.line(self.df, x=self.x, y=self.y,
                         title=self.title)
        
        return fig

class Scatter(Dados): 
    def __init__(self, title, df, x='Date',y=None):
        super().__init__(df, x='Date',y=None)
        self.title = title
                
    def plot(self):
        if self.x == 'Date':
            fig = px.scatter(self.df, x=self.x, y=self.y,
                            hover_data={"Date": "|%B %d, %Y"},
                            title=self.title)
        else:
            fig = px.scatter(self.df, x=self.x, y=self.y,
                            title=self.title)

        return fig


