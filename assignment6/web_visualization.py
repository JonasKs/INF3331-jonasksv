from flask import Flask, render_template, request
from temperature_cO2_plotter import plot_temperature, plot_CO2, plot_co2_by_country
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def plotting():
    """Plot the histograms through the website. Please note that not passing
    ymin and ymax values will not work.

    """
    if request.method == 'POST':
        # Acces the form data:
        #plot_CO2
        fromyear = request.form["fromyear"]
        toyear = request.form["toyear"]
        #plot_temperature
        #Check if ymin is empty, and if it is, make it None instead.
        if request.form["ymin"] or request.form["ymax"] is "":
            ymin = None
            ymax = None
        else: #If not empty, make it an int to prevent a crash.
            ymin = (int(request.form["ymin"]))
            ymax = (int(request.form["ymax"]))
        #We assume everything else is filled out, to not over complicate things.
        fromyear2 = request.form["fromyear2"]
        toyear2 = request.form["toyear2"]
        month = request.form["month"]
        year = int(request.form["year"])
        lower = int(request.form["lower"])
        upper = int(request.form["upper"])

        plot_country = plot_co2_by_country(year,lower,upper)
        plot_temp = plot_temperature(month, fromyear2, toyear2, ymin, ymax)
        plot_co2 = plot_CO2(fromyear,toyear)
        return render_template('plot.html', co2=plot_co2, temp=plot_temp, country=plot_country)

    if request.method == 'GET':
        plot_co2 = plot_CO2(1755,2012)
        plot_temp = plot_temperature('January')
        plot_country = plot_co2_by_country(1960,6,10)
        return render_template('plot.html', co2=plot_co2, temp=plot_temp, country=plot_country )




if __name__ == "__main__":
    app.run(debug=True)
