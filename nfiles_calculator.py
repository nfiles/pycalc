###############################################################################
# Nathan Files
# COMP 443
# Final Exam Take Home
# Scientific Calculator
###############################################################################

from tkinter import *
from math import log

# enumerated type
# source: http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
def enum(**enums):
    return type('Enum', (), enums)

# operators
OPERATOR = enum(
	NULL = 0,
	ADD  = 1,
	SUB  = 2,
	MUL  = 3,
	DIV  = 4,
	SIN  = 5,
	COS  = 6,
	TAN  = 7,
	POW  = 8,
	ROOT = 9,
	LOG  = 10,
	LN   = 11)

# it's a calculator!
class Calculator:
	TITLE = "Calculator"
	left  = None
	right = None
	op    = OPERATOR.NULL

	should_reprint = 1
	did_read       = 0

	def __init__(self, master):
		#--------------------------------------------------
		# Frame
		frame = Frame(master, width=200, height=300)
		frame.grid()

		#--------------------------------------------------
		# Text Field
		row = 0
		self.input_field = Entry(frame)
		self.input_field.grid(row = row, column = 0, columnspan = 4, sticky = W+E)
		self.input_field.insert(0, "0")
		#--------------------------------------------------
		# Row 1
		row += 1
		self.power_button = Button(frame, text = "y^x", command = self.power)
		self.power_button.grid(row = row, column = 0, sticky = W+E)
		self.natural_log_button = Button(frame, text = "ln", command = self.natural_log)
		self.natural_log_button.grid(row = row, column = 1, sticky = W+E)
		self.common_log_button = Button(frame, text = "log", command = self.common_log)
		self.common_log_button.grid(row = row, column = 2, sticky = W+E)
		self.clear_button = Button(frame, text = "AC", command = self.clear)
		self.clear_button.grid(row = row, column = 3, sticky = W+E)
		#--------------------------------------------------
		# Row 2
		row += 1
		self.seven_button = Button(frame, text = "7", command = self.seven)
		self.seven_button.grid(row = row, column = 0, sticky = W+E)
		self.eight_button = Button(frame, text = "8", command = self.eight)
		self.eight_button.grid(row = row, column = 1, sticky = W+E)
		self.nine_button = Button(frame, text = "9", command = self.nine)
		self.nine_button.grid(row = row, column = 2, sticky = W+E)
		self.divide_button = Button(frame, text = "/", command = self.divide)
		self.divide_button.grid(row = row, column = 3, sticky = W+E)
		#--------------------------------------------------
		# Row 3
		row += 1
		self.four_button = Button(frame, text = "4", command = self.four)
		self.four_button.grid(row = row, column = 0, sticky = W+E)
		self.five_button = Button(frame, text = "5", command = self.five)
		self.five_button.grid(row = row, column = 1, sticky = W+E)
		self.six_button = Button(frame, text = "6", command = self.six)
		self.six_button.grid(row = row, column = 2, sticky = W+E)
		self.multiply_button = Button(frame, text = "*", command = self.multiply)
		self.multiply_button.grid(row = row, column = 3, sticky = W+E)
		#--------------------------------------------------
		# Row 4
		row += 1
		self.one_button = Button(frame, text = "1", command = self.one)
		self.one_button.grid(row = row, column = 0, sticky = W+E)
		self.two_button = Button(frame, text = "2", command = self.two)
		self.two_button.grid(row = row, column = 1, sticky = W+E)
		self.three_button = Button(frame, text = "3", command = self.three)
		self.three_button.grid(row = row, column = 2, sticky = W+E)
		self.subtract_button = Button(frame, text = "-", command = self.subtract)
		self.subtract_button.grid(row = row, column = 3, sticky = W+E)
		#--------------------------------------------------
		# Row 5
		row += 1
		self.zero_button = Button(frame, text = "0", command = self.zero)
		self.zero_button.grid(row = row, column = 0, sticky = W+E)
		self.decimal_button = Button(frame, text = ".", command = self.decimal)
		self.decimal_button.grid(row = row, column = 1, sticky = W+E)
		self.equals_button = Button(frame, text = "=", command = self.equals)
		self.equals_button.grid(row = row, column = 2, sticky = W+E)
		self.addition_button = Button(frame, text = "+", command = self.addition)
		self.addition_button.grid(row = row, column = 3, sticky = W+E)

	# Numerical entry
	def zero(self):
		self.type_number("0")
	def one(self):
		self.type_number("1")
	def two(self):
		self.type_number("2")
	def three(self):
		self.type_number("3")
	def four(self):
		self.type_number("4")
	def five(self):
		self.type_number("5")
	def six(self):
		self.type_number("6")
	def seven(self):
		self.type_number("7")
	def eight(self):
		self.type_number("8")
	def nine(self):
		self.type_number("9")
	def decimal(self):
		self.type_number(".")
	def type_number(self, character):
		self.did_read = 0

		if (self.should_reprint == 1):
			self.left = float(self.input_field.get())
			self.input_field.delete(0, END)
			self.should_reprint = 0
		
		if (character == "."):
			if (self.input_field.get().find(".") == -1):
				self.input_field.insert(END, character)
		else:
			self.input_field.insert(END, character)

	# unary operators
	def natural_log(self):
		self.should_reprint = 1
		self.op = OPERATOR.LN
		self.iterate()
	def common_log(self):
		self.should_reprint = 1
		self.op = OPERATOR.LOG
		self.iterate()
	# binary operators
	def power(self):
		self.should_reprint = 1
		self.op = OPERATOR.POW
	def divide(self):
		self.should_reprint = 1
		self.op = OPERATOR.DIV
		if (self.did_read):
			self.iterate()
	def multiply(self):
		self.should_reprint = 1
		self.op = OPERATOR.MUL
		if (self.did_read):
			self.iterate()
	def subtract(self):
		self.should_reprint = 1
		self.op = OPERATOR.SUB
		if(self.op != OPERATOR.SUB):
			self.op = OPERATOR.SUB
		if (self.did_read):
			self.iterate()
	def addition(self):
		self.should_reprint = 1
		if (self.op != OPERATOR.ADD):
			self.op = OPERATOR.ADD
		elif (self.did_read):
			self.iterate()
	def clear(self):
		# if (self.left != 0):
		# 	if (self.left != 0.0):
		# 		self.input_field.delete(0, END)
		# 		self.input_field.insert(0, "0")
		# else:
		# 	self.left  = 0
		# 	self.right = 0
		# 	self.op    = OPERATOR.NULL
		self.left = None
		self.right = None
		self.update_input_field()
		self.did_read = 1
		self.should_reprint = 1

	# binary operations
	def equals(self):
		# if (len(self.input_field.get()) > 0):
			# print("equals")
		self.iterate()

	def read(self):
		if (self.did_read != 1):
			self.right = float(self.input_field.get())
			self.did_read = 1

	# writes left operand to text field
	def update_input_field(self):
		self.input_field.delete(0, END)
		text = ""
		if (self.left is not None):
			if (str(self.left).find(".") == -1):
				text = str(int(self.left))
			else:
				text = str(float(self.left))
		else:
			text = "0"
		self.input_field.insert(0, text)

	def iterate(self):
		# iterate (changes left and right operands)
		# 	result stored in left
		# 	right remains the same
		# 	operator remains the same
		self.read()
		# binary operations
		if (self.left is not None and self.right is not None):
			if   (self.op == OPERATOR.ADD): self.left = self.left  + self.right
			elif (self.op == OPERATOR.SUB): self.left = self.left  - self.right
			elif (self.op == OPERATOR.MUL): self.left = self.left  * self.right
			elif (self.op == OPERATOR.DIV and self.right != 0):
					self.left = self.left  / self.right
			elif (self.op == OPERATOR.POW): self.left = self.left ** self.right
		# unary operations
		elif (self.right is not None):
			if (self.op == OPERATOR.LOG): self.left = log(self.right, 10)
			elif (self.op == OPERATOR.LN ): self.left = log(self.right)

		self.update_input_field()
		self.should_reprint = 1

# run the calculator
root = Tk()
calc = Calculator(root)
root.title(calc.TITLE)
root.mainloop()
