def create_new_account():
	while True:
		create_new_acc = input(' Input "Y" for create or "N" for quit. \n If u want come back enter "B".')
		if create_new_acc.lower() == 'y':
			n_log = input(" What's your new login?: ")
			n_pas = input(" What's your new pas?: ")
			with open ('logs.txt', 'a') as txt:
				w_content = n_log.lower() + ' ' + n_pas.lower() + ';\n'
				txt.write(w_content)
			log_in()
		elif create_new_acc.lower() == 'b': 
			log_in()
		elif create_new_acc == 'n': 
			break
		else:
			print(' Uncorrect value!')
			continue



def log_in():
	have_or_create = input(' Welcom! Have u account or u want create new?\n Enter "1" if u have or enter "2" if u want create.\n Enter "Q" if u want quit. ')
	if have_or_create == '1':
		enter_log_pas()
	if have_or_create == "2":
		create_new_account()
	if have_or_create.lower() == 'q':
		print('Good bye!')



def chat():
	print('<<<Welcome to chat!>>>')



def enter_log_pas():
	while True:
		print(' <<<Enter your login and pasword>>>')
		log = input(' Login: ')
		pas = input(' Password: ')
		lp = log.strip().lower() + ' ' + pas.strip().lower() +';\n'
		with open ('logs.txt', 'r') as txt:
			r_content = txt.readlines()
		if lp in r_content:
			chat()
		else:
			print(' Sorry, password or login uncorrect :(')
			try_or_create = input(' If u want try again enter "T", or enter "C" for create new account: ')
			if try_or_create.lower() == 'c':
				create_new_account()
			if try_or_create.lower == 't':
				continue


log_in()
