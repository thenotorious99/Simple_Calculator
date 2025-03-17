import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED

sg.theme("BlueMono")

label1 = sg.Text("Enter first number: ")
input1 = sg.Input(key="num1")

label2 = sg.Text("Enter second number: ")
input2 = sg.Input(key="num2")

result = sg.Text("Result:", key="result")

exit_button = sg.Button("Exit")
plus_button = sg.Button("+")
mines_button = sg.Button("-")
divison_button = sg.Button("/")
multiplication_button = sg.Button("*")


window = sg.Window("Simple Calculator", layout=[[label1, input1],
                                                [label2, input2],
                                                [plus_button, mines_button, divison_button, multiplication_button],
                                                [result],
                                                [exit_button]])

while True:
    event, value = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    try:
        num1 = float(value["num1"])
        num2 = float(value["num2"])

        if event == "+":
            result = num1 + num2
        elif event == "-":
            result = num1 - num2
        elif event == "*":
            result = num1 * num2
        elif event == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Wrong: You cannot devision on zero!"

        window["result"].update(result)

    except ValueError:
        window["result"].update("Wrong: Invalid input")


window.close()