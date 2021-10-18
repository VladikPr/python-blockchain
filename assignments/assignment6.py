import pickle
# 1) Write a short Python script which queries the user for input(infinite loop with exit possibility) and writes the input to a file
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
def save_data(data):
   with open('db.txt', 'a') as f:
      f.write(data)
      f.write('\n')

def load_data():
   file_content = None
   with open('db.txt', 'r') as f:
      file_content = f.readlines()
   return file_content

is_running = True
while is_running:
   print('{:*^40}'.format('Programm is running'))
   print('''Options:\n 1: Add text to file\n 2: Print data from the file\n q: Quit ''')
   user_choise = input('Please enter your choice: ')

   if user_choise == '1':
      user_text = input('Enter the text you want to save: ')
      save_data(user_text)
   elif user_choise == '2':
      get_data = load_data()
      for line in get_data:
         print(line)
   elif user_choise == 'q':
      is_running = False
   else:
      print('Invalid value! Please choose from the options.')
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
# 4) Adjust the logic to load the file content to work with pickled/ json data.
def save_data(data):
   with open('db.p', 'wb') as f:
      f.write(pickle.dumps(data))

def load_data():
   file_content = None
   with open('db.p', 'rb') as f:
      file_content = pickle.loads(f.read())
   return file_content

is_running = True
user_list = []
while is_running:
   print('{:*^40}'.format('Programm is running'))
   print('''Options:\n 1: Add text to file\n 2: Print data from the file\n q: Quit ''')
   user_choise = input('Please enter your choice: ')
   if user_choise == '1':
      user_text = input('Enter the text you want to save: ')
      user_list.append(user_text)
      save_data(user_list)
   elif user_choise == '2':
      get_data = load_data()
      for line in get_data:
         print(line)
   elif user_choise == 'q':
      is_running = False
   else:
      print('Invalid value! Please choose from the options.')
