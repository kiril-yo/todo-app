import PySimpleGUI as sg

label_ft = sg.Text("Enter feet:")
input_ft = sg.Input()

label_in = sg.Text("Enter inches:")
input_in = sg.Input()

btn_convert = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label_ft, input_ft],[label_in,input_in],[btn_convert]])

window.read()
window.close()