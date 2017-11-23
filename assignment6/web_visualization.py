from flask import Flask, render_template, request
from temperature_cO2_plotter import plot_temperature, plot_CO2
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def plotting():
    if request.method == 'POST':
        # Acces the form data:
        #plot_CO2
        fromyear = request.form["fromyear"]
        toyear = request.form["toyear"]
        #plot_temperature
        ymin = request.form["ymin"]
        ymax = request.form["ymax"]
        fromyear2 = request.form["fromyear2"]
        toyear2 = request.form["toyear2"]
        month = request.form["month"]

        plot_temp = plot_temperature(month, fromyear2, toyear2, ymin, ymax)
        plot_co2 = plot_CO2(fromyear,toyear)
        return render_template('plot.html', co2=plot_co2, temp=plot_temp )

    if request.method == 'GET':
        plot_co2 = plot_CO2(1755,2012)
        plot_temp = plot_temperature('September')
        return render_template('plot.html', co2=plot_co2, temp=plot_temp )




if __name__ == "__main__":
    app.run(debug=True)
