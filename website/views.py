from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def add(request):
	from random import randint
	num_1 = randint(0, 10)
	num_2 = randint(0, 10)

	if request.method == "POST":
		answer = request.POST['answer']

		# error handling- if no form fillout
		if not answer:
			my_answer = 'Hey, you forgot to answer!'
			color = 'warning'
			return render(request, 'add.html', {
			'num_1': num_1,
			'num_2': num_2,
			'answer': answer,
			'my_answer': my_answer,
			'color': color,
			})

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = f'Correct, {old_num_1} + {old_num_2} = {answer}'
			color = 'primary'
		else:
			my_answer = f'Incorrect, {old_num_1} + {old_num_2} is not {answer}'
			color = 'danger'

		return render(request, 'add.html', {
			'answer': answer,
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'old_num_1': old_num_1,
			'old_num_2': old_num_2,
			'correct_answer': correct_answer,
			'color': color,
			})

	return render(request, 'add.html', {
		'num_1': num_1,
		'num_2': num_2,
		})


def subtract(request):
	from random import randint
	num_1 = randint(0, 10)
	num_2 = randint(0, 10)

	if request.method == 'POST':
		answer = request.POST['answer']

		# error handling- if no form fillout
		if not answer:
			my_answer = 'Hey, you forgot to answer!'
			color = 'warning'
			return render(request, 'subtract.html', {
			'num_1': num_1,
			'num_2': num_2,
			'answer': answer,
			'my_answer': my_answer,
			'color': color,
			})

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(old_num_1) - int(old_num_2)

		if int(answer) == int(correct_answer):
			my_answer = f'Correct, {old_num_1} - {old_num_2} = {answer}'
			color = 'primary'
		else:
			my_answer = f'Incorrect, {old_num_1} - {old_num_2} is not {answer}'
			color = 'danger'
		return render(request, 'subtract.html', {
					'my_answer': my_answer,
		'old_num_1': old_num_1,
		'old_num_2': old_num_2,
		'my_answer': my_answer,
		'answer': answer,
		'num_1': num_1,
		'num_2': num_2,
		'color': color,

			})

	return render(request, 'subtract.html', {
		'num_1': num_1,
		'num_2': num_2,
		})

def multiply(request):
	from random import randint
	num_1 = randint(0, 10)
	num_2 = randint(0, 10)
	if request.method == 'POST':
		answer = request.POST['answer']

		# error handling- if no form fillout
		if not answer:
			my_answer = 'Hey, you forgot to answer!'
			color = 'warning'
			return render(request, 'multiply.html', {
			'num_1': num_1,
			'num_2': num_2,
			'answer': answer,
			'my_answer': my_answer,
			'color': color,
			})

		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = f'Correct, {old_num_1} * {old_num_2} = {answer}'
			color = 'primary'
		else:
			my_answer = f'Incorrect, {old_num_1} * {old_num_2} != {answer}'
			color = 'danger'

		return render(request, 'multiply.html', {
			'num_1': num_1,
			'num_2': num_2,
			'old_num_1': old_num_1,
			'old_num_2': old_num_2,
			'answer': answer,
			'color': color,
			'my_answer': my_answer,

			})

	return render(request, 'multiply.html', {
		'num_1': num_1,
		'num_2': num_2,
		})

def devide(request):
	from random import randint
	num_1 = randint(0, 10)
	num_2 = randint(1, 10)

	if request.method == 'POST':
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		answer = request.POST['answer']

		# error handling- if no form fillout
		if not answer:
			my_answer = 'Hey, you forgot to answer!'
			color = 'warning'
			return render(request, 'devide.html', {
			'num_1': num_1,
			'num_2': num_2,
			'answer': answer,
			'my_answer': my_answer,
			'color': color,
			})

		correct_answer = int(old_num_1) / int(old_num_2)

		if float(answer) == correct_answer:
			my_answer = f'Correct, {old_num_1} / {old_num_2} = {answer}'
			color = 'primary'
		else:
			my_answer = f'Incorrect, {old_num_1} / {old_num_2} is not {answer}'
			color = 'danger'

		return render(request, 'devide.html', {
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'old_num_1': old_num_1,
			'old_num_2': old_num_2,
			'answer': answer,
			'color': color,
			})

	return render(request, 'devide.html', {
		'num_1': num_1,
		'num_2': num_2,
		})