from asyncore import read
from locale import currency
import PySimpleGUI as sg
from forex_python.converter import CurrencyRates

c = CurrencyRates()

compatiblecurrencies = ["American Dollar","British Pound","European Euro","Indian Rupee", "Austrailian Dollar", "Chinese Renminbi", "Japanese Yen", "Canadian Dollar", "Swiss Franc"]
currencycodes = ["USD","GBP","EUR","INR", "AUD", "CNY", "JPY", "CAD", "CHF"]


layout = [
    [sg.Text("Enter the two currencies to convert in the two boxes below.")],
    [sg.Text("Currency to convert from:")],[sg.Combo(compatiblecurrencies, default_value="American Dollar", readonly=True, key="-FIRSTCURR-")],
    [sg.Text("Currency to convert to:")],
    [sg.Combo(compatiblecurrencies, default_value="Indian Rupee",readonly=True, key="-SECCURR-")],
    [sg.Button("Convert", key="-CONVERT-")],
    [sg.Text("", key="-VALUESAYER-")]
]

window = sg.Window("Currency Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        firstcurr = values["-FIRSTCURR-"]
        seccurr = values["-SECCURR-"]

        firstindex = compatiblecurrencies.index(firstcurr)
        secindex = compatiblecurrencies.index(seccurr)

        convertedcurr = c.get_rate(currencycodes[firstindex], currencycodes[secindex])
        if convertedcurr != 1:
            window["-VALUESAYER-"].Update("1 "+firstcurr+" is equal to "+str(convertedcurr)+" "+seccurr+"s")

        else:
            window["-VALUESAYER-"].Update("1 "+firstcurr+" is equal to "+str(convertedcurr)+" "+seccurr)

window.close()