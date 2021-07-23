from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	to_ret = list(range(number))

	random.seed(seed)
	random.shuffle(to_ret)
	return to_ret

# print(gen_random_int(10,100))

def generate():
	global array

	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	
	pass

	array = gen_random_int(number, seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	pass

	array_str = (',').join([str(s) for s in array]) + '.'

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	

	document.getElementById("generate").innerHTML = array_str


def my_sort(array):
	for i in range(1, len(array)):
		for j in range(i-1, -1, -1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
			else:
				break
			

	return array

# print(my_sort([2,31,1,5,6,9]))

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_new = array[:]
	
	array_new = my_sort(array_new)

	array_str = (','.join([str(s) for s in array_new])) + '.'
	
	document.getElementById("sorted").innerHTML = array_str
	print(array_new)


def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str

	number_list = value.split(',')
	
	try:
		number_list = [int(num) for num in number_list]
		
	except:
		window.alert("Please input numbers only")
		return
	
	array_str = (',').join([str(s) for s in my_sort(number_list)])


	document.getElementById("sorted").innerHTML = array_str


