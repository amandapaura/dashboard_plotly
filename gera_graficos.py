class GeradorGraficos:
    def __init__(self,grafico,template=None):
        self.grafico = grafico
        if template == None:
            self.template = "plotly_dark"
        else: 
            self.template = template

    def cria_graficos(self):
        fig = self.grafico.plot()
        fig.update_xaxes(
            dtick="M1",
            tickformat="%b\n%Y")

        fig.update_layout(
        template=self.template
        #plot_bgcolor=colors['background'],
        #paper_bgcolor=colors['background'],
        #font_color=colors['text']
        )
        return fig