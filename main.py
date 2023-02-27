import openai
from os import getenv
import tkinter as tk
from tkinter import messagebox
import spacy

def initialise_window():
	"""
	This initialises all of the GUI compontents, displays them, 
	and returns a master window so that the main loop can be executed.
	
	:returns: The main window. 
	"""
	openai.api_key = getenv("GPT-3_Key")
	GUI = tk.Tk()
	GUI.title("GPT-3 Communicator")
	GUI.geometry("800x600")

	input_label = tk.Label(master=GUI, text="Input")
	input_entry = tk.Entry(GUI, width=400)
	output_label = tk.Label(GUI, text="Answer will display here", wraplength=800)
	send_button = tk.Button(GUI, text="Send")
	send_button.bind("<Button-1>", lambda a: submit_clicked(input_entry.get(), output_label))

	input_label.pack()
	input_entry.pack()
	output_label.pack()
	send_button.pack()
		
	return GUI


def submit_clicked(question, answer_display):
	"""
	This takes in a question, submits it to GPT-3, and provides an output
	label with the answer. This also handles any errors on GPT-3's end
	by providing an error message.

	:question: The question which is submitted by the user.
	:answer_display: The reference to the output label to be updated with
	GPT-3's answer.
	"""
	try:
		GPT_resp = openai.Completion.create(
			engine="text-davinci-003",
			prompt=question,
			temperature=0.5,
			max_tokens=250,
			top_p=0.1, #Only considering the top 10% most probable answers
			frequency_penalty=0.0,
			presence_penalty=0.0
		)
		answer = GPT_resp['choices'][0]['text']
		answer_display.config(text = answer)
	except Exception as e:
		messagebox.showerror("Error", e)
	
GUI = initialise_window()

GUI.mainloop()
