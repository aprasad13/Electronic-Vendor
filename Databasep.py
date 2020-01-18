import tkinter as tk
from tkinter import *
from tkinter import messagebox
import threading
import sqlite3
from sqlite3 import Error
import sql_queries
import pdb

def insert_in_transaction():
	for i in range(len(cart)):
		sql_queries.insertonlinetransaction(cart[i][0], cart[i][7])

conn = sql_queries.create_connection(r"/Users/amanprasad/Desktop/Vaibhav/pythonsqlite_2.db")
# print(type(conn))

conn.row_factory = lambda cursor, row: row[:]
c = sql_queries.create_cursor(conn)
ids = c.execute("select * from Customer").fetchall()
#pdb.set_trace()
# print(ids)

ids1 = c.execute("select * from cardcredit").fetchall()
# print(ids1)

email_id_list = [query_result[8] for query_result in ids]
global creditcard_list 
creditcard_list = [query_result[0] for query_result in ids1]
password_list = [query_result[9] for query_result in ids]
name_list = [query_result[1] for query_result in ids]
# print(email_id_list)
# print(password_list)
# print(creditcard_list)
user_id = ''

#ids = c.execute("select * from cardcredit").fetchall()
#print(ids)
#lt_card=len(ids)
#lst_card=[]
#for i in range(0,lt_card):
#   print(i , ' -->' , ids[i][0])

global payment_type
global order_type 
order_type = 'online'

global creditCard_number
global customer_id

 
username = ''
registration_password = ''
login_password = ''
category_selected = ''
user_selected_category = ''
acc_num_label = ''
first_name_label = ''
last_name_label = ''
email_label = ''
password_label = ''
line1_label = ''
line2_label = ''
zip_code_label = ''
city_label = ''
phone_number_label = ''
username_input = ''
logged_in_as = ''
extra_flag = False
flag = False
user_name = ''
labels = []
item_list = []
buttons = []
category_list = []
item_index = 0
item_name = ''
item_price = ''
cart_button = ''
cart = []
temporary = ''
cart_item_name = []
cart_item_price = []
remove_item_button = []
cart_list_box= []
item_quantity = []
item_price_box = []
delete_item_button = ''
cost_label = ''
order_address_line11 = ''
order_address_line21 = ''
order_address_city1 = ''
order_address_state1 = ''
order_zip_code1 = ''

class Order_page(tk.Frame):
	def __init__(self, parent, controller):
		global user_id
		tk.Frame.__init__(self, parent)

		view_ = sql_queries.orderviewtable(user_id)
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(search_page))
		back_button.grid(row = 0, column = 0)
		cells = {}
		# print("view")
		# print(view_)
		for i in range(len(view_)):
			for j in range(13):
				labels_ = Label(self, text = view_[i][j])
				labels_.grid(row = i + 1, column = j)
				cells[(i, j)] = labels_


class Inventory(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		view_ = sql_queries.storeinvent()
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(search_page))
		back_button.grid(row = 0, column = 0)
		cells = {}


		# scroll_bar_y = Scrollbar(self, orient=tk.VERTICAL, command = self.yview)
		# scroll_bar_x = Scrollbar(self, orient=tk.HORIZONTAL, command = self.xview)
		# scroll_bar_x.grid(row = 0, column = 3, sticky = 'ns')
		# scroll_bar_y.grid(row = 10, column = 0, sticky = 'se')
		# scroll_bar_y.configure(yscrollcommand = scroll_bar_y.set)
		# scroll_bar_x.configure(xscrollcommand = scroll_bar_x.set)
		# print("view")
		# print(view_)
		for i in range(len(view_)):
			for j in range(3):
				print()
				labels_ = Label(self, text = str(view_[i][j]))
				labels_.grid(row = i + 1, column = j)
				cells[(i, j)] = labels_


class orderadd_page(tk.Frame):
	def __init__(self, parent, controller):
		global order_address_line1
		global order_address_line2
		global order_address_city
		global order_address_state
		global order_zip_code

		order_address_line1 = StringVar()
		order_address_line2 = StringVar()
		order_address_city = StringVar()
		order_address_state = StringVar()
		phone_number = StringVar()
		order_zip_code = StringVar()

		tk.Frame.__init__(self, parent)
		line1 = tk.StringVar()
		line2 = tk.StringVar()
		zip_code = tk.StringVar()
		city = tk.StringVar()
		phone_number = tk.StringVar()
		state = tk.StringVar()
		
		line1_label = Label(self, text = "Address Line 1")
		line2_label = Label(self, text = "Address Line 2")
		zip_code_label = Label(self, text = "Zip Code")
		city_label = Label(self, text = "City")
		state_lebel = Label(self, text = "State")
		

		line1_entry = Entry(self, textvariable = order_address_line1)
		line2_entry = Entry(self, textvariable = order_address_line2)
		zip_code_entry = Entry(self, textvariable = order_zip_code)
		city_entry = Entry(self, textvariable = order_address_city)
		address_button = Button(self, text = "Add Address", command = lambda: self.getinfo(controller))
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(CartPage))
		state_entry = Entry(self, textvariable =order_address_state)

		pay_credit_card_button = tk.Button(self, text="Pay Via Credit Card", command=lambda: [controller.show_frame(payment_credit_page), self.get_data(controller)])
		pay_credit_card_button.grid(row = 14, column = 0)
		pay_account_button = tk.Button(self, text="Pay Via Account Number", command=lambda: controller.show_frame(payment_account_page))
		pay_account_button.grid(row = 14, column = 1)
		
		

		line1_label.grid(row = 8, column = 1, sticky = "EW", pady = 2)
		line2_label.grid(row = 9, column = 1, sticky = "EW", pady = 2)
		zip_code_label.grid(row = 10, column = 1, sticky = "EW", pady = 2)
		city_label.grid(row = 11, column = 1, sticky = "EW", pady = 2)
		line1_entry.grid(row = 8, column = 2, sticky = "EW", pady = 2)
		line2_entry.grid(row = 9, column = 2, sticky = "EW", pady = 2)
		zip_code_entry.grid(row = 10, column = 2, sticky = "EW", pady = 2)
		city_entry.grid(row = 11, column = 2, sticky = "EW", pady = 2)
		back_button.grid(row = 1, column = 1, sticky = "EW", pady = 5, padx = 5)
		state_lebel.grid(row = 13, column = 1, sticky = "NESW", pady = 2)
		state_entry.grid(row = 13, column = 2, sticky = "NESW", pady = 2)

	def get_data(self, controller):
		global order_address_line1
		global order_address_line2
		global order_address_city
		global order_address_state
		global order_zip_code
		global order_address_line11
		global order_address_line21
		global order_address_city1
		global order_address_state1
		global order_zip_code1



		order_address_line11 = str(order_address_line1.get())
		order_address_line21 = str(order_address_line2.get())
		order_address_city1 = str(order_address_city.get())
		order_address_state1 = str(order_address_state.get())
		order_zip_code1 = int(order_zip_code.get())	

		# print(order_address_line21)




class main_window(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		main_container = tk.Frame(self)
		main_container.pack(side="top", fill="both", expand = True)
		main_container.grid_rowconfigure(0, weight=1)
		main_container.grid_columnconfigure(0, weight=1)
		self.frames = {}

		for F in (LoginPage, StartPage, search_page, registration_page, result_page, CartPage, payment_credit_page, payment_account_page, orderadd_page, Order_page, Inventory):
			frame = F(main_container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Start Page")
		label.pack(pady=10,padx=10)

		button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(LoginPage))
		button.pack()

class CartPage(tk.Frame):

	
	def __init__(self, parent, controller):
		global cart_item_price
		global cart_item_name
		global remove_item_button
		global cart_list_box
		global item_quantity
		global item_price_box
		global cost_label


		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Cart Page")
		
		label.grid(row = 0, column = 1)

		
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(search_page))
		item_cart = Label(self, text = 'Item')
		item_cart_quantity = Label(self, text = 'Item Quantity')
		cost_label = Label(self, text = 'Total Cost')

		
		back_button.grid(row = 0, column = 0)
		item_cart.grid(row = 1, column = 0)
		item_cart_quantity.grid(row = 1, column = 1)
		cost_label.grid(row = 12, column = 2)

		pay_button = Button(self, text = "Finalize", command = lambda: controller.show_frame(orderadd_page))
		pay_button.grid(row = 13, column = 0)

		temporary = self

		delete_item_button = Button(self, )

		cart_item_name = []
		cart_item_price = []
		remove_item_button = []

		cart_list_box = Listbox(self)
		cart_list_box.bind('List', self.print_items)
		cart_list_box.grid(row = 1, column = 0)
		
		item_quantity = Listbox(self)
		item_quantity.bind('List', self.print_items)
		item_quantity.grid(row = 1, column = 1)

		item_price_box = Listbox(self)
		item_price_box.bind('List', self.print_items)
		item_price_box.grid(row = 1, column = 2)

		# for i in range(10):
		#   cart_item_name.append(Label(self, text = ''))
		#   cart_item_price.append(Label(self, text = ''))
		#   remove_item_button.append(Button(self, text = 'Remove from Cart'))

		#   cart_item_name[i].grid(row = i + 1, column = 0)
		#   cart_item_price[i].grid(row = i + 1, column = 1)
		#   remove_item_button[i].grid(row = i + 1, column = 2)

		
		# cart_thread = threading.Thread(target = self.set_item, args = (controller,))
		# cart_thread.start()
		# cart_thread.join()
		# self.set_item(controller)


	def print_items():
		# print('ok')
		global flag
		global temporary
		global cart
		global item_index
		global item_list
		global flag
		global temporary
		global cart_item_price
		global cart_item_name
		global remove_item_button
		global item_price_box
		global total_cost
		global cost_label

		# print(len(cart))

		# for i in range(len(cart)):
		#   cart_item_name[i]['text'] = cart[i][0]
		#   cart_item_price[i]['text'] = cart[i][5]

		# for i in range(len(item_list) - 1, 10):
		#   remove_item_button[i].destroy()

		name_list = [in_cart[1] for in_cart in cart]
		item_number = [in_cart[7] for in_cart in cart]

		cart_list_box.delete(0, 'end')
		item_quantity.delete(0, 'end')
		item_price_box.delete(0, 'end')

		total_cost = 0

		for i in range(len(name_list)):
			cart_list_box.insert(END, name_list[i])
			item_quantity.insert(END, item_number[i])
			item_price_box.insert(END, item_number[i] * cart[i][6])
			total_cost += item_number[i] * cart[i][6]
		cost_label['text'] = 'Total Cost: '+ str(total_cost)
			

	def set_item(self, controller):
		global cart
		global item_index
		global item_list
		global flag
		global temporary

		cart_item_name = []
		cart_item_price = []
		remove_item_button = []

		while True:
			if flag:
				for item in cart:
					cart_item_name.append(Label(self, text = item_list[item_index][1]))
					cart_item_price.append(Label(self, text = str(item_list[item_index][6])))
					remove_item_button.append(Button(self, text = 'Remove from Cart'))

					cart_item_name[i].grid(row = i + 1, column = 0)
					cart_item_price[i].grid(row = i + 1, column = 1)
					remove_item_button[i].grid(row = i + 1, column = 2)

					flag = False
					break

			


class payment_account_page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		global account_number
		
		account_number = tk.StringVar()

		account_number_label = tk.Label(self, text = "Account Number")
		payment_title = tk.Label(self, text = "Payment via account number")

		self.account_number_entry = tk.Entry(self, textvariable = account_number)
		pay_button = tk.Button(self, text = "Pay", command = lambda: [controller.show_frame(search_page), insert_in_transaction(), self.get_payment_credentials(controller)])

		account_number_label.place(relx = 0.25, rely = 0.4)
		self.account_number_entry.place(relx = 0.4, rely = 0.4)
		pay_button.place(relx = 0.35, rely = 0.5)

	def get_payment_credentials(self, controller):
		global account_number

		insert_in_transaction()

		account_number_input = account_number_entry.get()
		# print('ho raha hai')

		self.account_number_entry.delete(0, END)




class payment_credit_page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		global creditCard_number
		global total_cost
		
		creditCard_number = tk.StringVar()

		creditCard_label = tk.Label(self, text = "Credit Card Number")
		payment_title = tk.Label(self, text = "Payment")

		self.creditCard_entry = tk.Entry(self, textvariable = creditCard_number)
		pay_button = tk.Button(self, text = "Pay", command = lambda: self.get_payment_credentials(controller))

		creditCard_label.place(relx = 0.25, rely = 0.4)
		self.creditCard_entry.place(relx = 0.4, rely = 0.4)
		pay_button.place(relx = 0.35, rely = 0.5)
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(orderadd_page))
		back_button.grid(row = 0, column = 0)

	def get_payment_credentials(self, controller):
		global creditCard_number
		global order_address_line11
		global order_address_line21
		global order_address_city1
		global order_address_state1
		global order_zip_code1
		global user_id

		extra_flag = True

		creditCard_input = int(creditCard_number.get())
		#for i in range(len(creditcard_list)):
		# print(creditcard_list)
		


		if creditCard_input :
			# print(creditCard_input)
			if creditCard_input in creditcard_list:
				# print(creditCard_input)
				print('Card is verified successfully')
				if sql_queries.cardcredit(creditCard_input) > total_cost:
					sql_queries.insert_order(total_cost, 'online', order_address_line11, order_address_line21, order_address_city1, order_address_state1, order_zip_code1, 'card', creditCard_input)
					insert_in_transaction()
					sql_queries.insert_shipment(user_id)
					messagebox.showinfo("Order Placed", 'Your Order was placed successfully')
					controller.show_frame(search_page)
				else:
					messagebox.showinfo('Insufficient Credit')
			else:
				messagebox.showinfo('Invalid card')
		else: 
			messagebox.showinfo('enter card details')


		self.creditCard_entry.delete(0, END)


class LoginPage(tk.Frame):

	username_entry = ''
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		global username
		global login_password
		global flag

		username = tk.StringVar()
		login_password = tk.StringVar()
		
		username_label = tk.Label(self, text = "Username")
		password_label = tk.Label(self, text = "Password")
		self.username_entry = tk.Entry(self, textvariable = username)
		self.password_entry = tk.Entry(self, textvariable = login_password, show = '*')
		login_button = tk.Button(self, text = "Login", command = lambda: self.get_login_credentials(controller, parent))
		guest_button = tk.Button(self, text = "Login as Guest", command = lambda: self.next_page(controller, parent))
		register_button = tk.Button(self, text = "Register", command = lambda: controller.show_frame(registration_page))

		username_label.place(relx = 0.25, rely = 0.4)
		self.username_entry.place(relx = 0.4, rely = 0.4)
		password_label.place(relx = 0.25, rely = 0.45)
		self.password_entry.place(relx = 0.4, rely = 0.45)
		login_button.place(relx = 0.35, rely = 0.5)
		guest_button.place(relx = 0.25, rely = 0.6)
		register_button.place(relx = 0.5, rely = 0.6)

	def get_login_credentials(self, controller, parent):
		global username
		global login_password
		global flag
		global username_input
		global extra_flag
		global email_id_list
		global password_list
		global logged_in_as
		global user_id

		extra_flag = True

		ids = c.execute("select * from Customer").fetchall()
		email_id_list = [query_result[8] for query_result in ids]
		global creditcard_list 
		creditcard_list = [query_result[0] for query_result in ids1]
		password_list = [query_result[9] for query_result in ids]
		name_list = [query_result[1] for query_result in ids]

		username_input = username.get()
		password_input = login_password.get()

		self.username_entry.delete(0, END)
		self.password_entry.delete(0, END)

		if username_input and password_input:
			# print(username_input, password_input)
			if username_input in email_id_list:
				user_index = email_id_list.index(username_input)
				if password_input == password_list[user_index]:
					user_id = sql_queries.get_cid(username_input, password_input)

					# print("OK")
					logged_in_as = name_list[user_index]
					self.next_page(controller, parent)
					
				else:
					messagebox.showinfo("Incorrect Password", "Incorrect Password")
			else:
				messagebox.showinfo("User not found", "User not found")
			
			
		elif not username_input:
			messagebox.showinfo("Username field empty", "No Username entered!")
		else:
			messagebox.showinfo("Password field empty", "No Password entered!")

	def next_page(self, controller, parent):
		global username_input
		global logged_in_as
		global user_id

		global user_name

		if not username_input:
			logged_in_as = 'Guest'
			user_id = 0
			
		search_page.extra_fun()
		controller.show_frame(search_page)




class search_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		demo_options = ["mobile phone", "Televisions", "Laptops"]
		demo_brand_options = ["Please Select Category first"]

		global category_selected
		global username_input
		global logged_in_as
		global user_name
		global cart_button
		global temporary

		category_list = sql_queries.totalcategory(conn)

		category_selected = tk.StringVar()
		category_selected.set(category_list[0])

		logged_in = "Logged in as " + logged_in_as

		category_menu = OptionMenu(self, category_selected, *category_list)
		category_button = Button(self, text = "Search", command = lambda:  self.get_category(controller))
		back_button = Button(self, text = "Back", command = lambda: self.go_back(controller))
		category_label = Label(self, text = "Select Category to search")
		user_name = Label(self, text = 'ok')
		cart_button = Button(self, text = 'Cart', command = lambda: [controller.show_frame(CartPage), CartPage.print_items()])
		my_orders = Button(self, text = 'My Orders', command = lambda: controller.show_frame(Order_page))
		inventory_button = Button(self, text = 'Inventory', command = lambda: controller.show_frame(Inventory))

		category_menu.grid(row = 2, column = 0)
		category_button.grid(row = 2, column = 1)
		back_button.grid(row = 0, column = 0)
		category_label.grid(row = 1, column = 0)
		# user_name.grid(row = 0, column = 4, sticky = 'e')
		cart_button.grid(row = 0, column = 3)
		my_orders.grid(row = 0, column = 4)
		inventory_button.grid(row = 0, column = 5)

	def get_category(self, controller):
		global category_selected
		global user_selected_category
		global labels
		global buttons
		global item_list
		global category_list

		
		# print(user_selected_category)

		if labels or buttons:
			for i in range(len(labels)):
				labels[i].destroy()
				buttons[i].destroy()

		user_selected_category = category_selected.get()

		labels = []

		category_list = sql_queries.totalcategory(conn)
		# print(category_list)

		item_list = sql_queries.get_item(user_selected_category)
		# print(item_list)
		buttons = []


		for i in range(len(item_list)):
			labels.append(Label(self, text = item_list[i][1]))
			buttons.append(Button(self, text = "View",command = lambda m = i: self.view_item(controller, m)))
			labels[i].grid(row = 3 + i, column = 0)
			# buttons[i].bind('View', self.view_item(controller, buttons[i]))
			buttons[i].grid(row = 3 + i, column = 1)

		


	def view_item(self, controller, i):
		global item_index
		global buttons
		item_index = i

		# for j in range(len(buttons)):
		#   if i == buttons[j]:
		#       print(j)

		result_page.get_details()
		controller.show_frame(result_page)

	def go_back(self, controller):
		global username_input
		username_input = ''
		if labels:
			for i in range(len(labels)):
				labels[i].destroy()
				buttons[i].destroy()
		controller.show_frame(LoginPage)

	def extra_fun():
		global user_name
		global logged_in_as

		user_name['text'] = 'Logged in as ' + logged_in_as
		cart_button['text'] = logged_in_as + '\'s Cart'
		category_list = sql_queries.totalcategory(conn)

class registration_page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		global first_name
		global last_name
		global email
		global registration_password
		global line1
		global line2
		global zip_code
		global city
		global phone_number
		global state
		global acc_num

		first_name = tk.StringVar()
		last_name = tk.StringVar()
		email = tk.StringVar()
		registration_password = tk.StringVar()
		line1 = tk.StringVar()
		line2 = tk.StringVar()
		zip_code = tk.StringVar()
		city = tk.StringVar()
		phone_number = tk.StringVar()
		state = tk.StringVar()
		acc_num = tk.StringVar()

		first_name_label = Label(self, text = "First Name")
		last_name_label = Label(self, text = "Last Name")
		email_label = Label(self, text = "Email ID")
		password_label = Label(self, text = "Password")
		line1_label = Label(self, text = "Address Line 1")
		line2_label = Label(self, text = "Address Line 2")
		zip_code_label = Label(self, text = "Zip Code")
		city_label = Label(self, text = "City")
		phone_number_label = Label(self, text = "Phone Number")
		state_lebel = Label(self, text = "State")
		acc_num_label = Label(self, text = "Account Number")

		first_name_entry = Entry(self, textvariable = first_name)
		last_name_entry = Entry(self, textvariable = last_name)
		email_entry = Entry(self, textvariable = email)
		password_entry = Entry(self, textvariable = registration_password, show = '*')
		line1_entry = Entry(self, textvariable = line1)
		line2_entry = Entry(self, textvariable = line2)
		zip_code_entry = Entry(self, textvariable = zip_code)
		city_entry = Entry(self, textvariable = city)
		phone_number_entry = Entry(self, textvariable = phone_number)
		register_button = Button(self, text = "Register", command = lambda: self.getinfo(controller))
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(LoginPage))
		state_entry = Entry(self, textvariable = state)
		acc_num_entry = Entry(self, textvariable = acc_num)

		first_name_label.grid(row = 4, column = 1, sticky = "NESW", pady = 2)
		last_name_label.grid(row = 5, column = 1, sticky = "EW", pady = 2)
		email_label.grid(row = 6, column = 1, sticky = "EW", pady = 2)
		password_label.grid(row = 7, column = 1, sticky = "EW", pady = 2)
		line1_label.grid(row = 8, column = 1, sticky = "EW", pady = 2)
		line2_label.grid(row = 9, column = 1, sticky = "EW", pady = 2)
		zip_code_label.grid(row = 10, column = 1, sticky = "EW", pady = 2)
		city_label.grid(row = 11, column = 1, sticky = "EW", pady = 2)
		phone_number_label.grid(row = 12, column = 1, sticky = "EW", pady = 2)
		first_name_entry.grid(row = 4, column = 2, sticky = "EW", pady = 2)
		last_name_entry.grid(row = 5, column = 2, sticky = "EW", pady = 2)
		email_entry.grid(row = 6, column = 2, sticky = "EW", pady = 2)
		password_entry.grid(row = 7, column = 2, sticky = "EW", pady = 2)
		line1_entry.grid(row = 8, column = 2, sticky = "EW", pady = 2)
		line2_entry.grid(row = 9, column = 2, sticky = "EW", pady = 2)
		zip_code_entry.grid(row = 10, column = 2, sticky = "EW", pady = 2)
		city_entry.grid(row = 11, column = 2, sticky = "EW", pady = 2)
		phone_number_entry.grid(row = 12, column = 2, sticky = "EW", pady = 2)
		register_button.grid(row = 15, column = 1, sticky = "WE", pady = 5, padx = 5)
		back_button.grid(row = 1, column = 1, sticky = "EW", pady = 5, padx = 5)
		
		#print (type(ip_code_entry.get()))
		
		state_lebel.grid(row = 13, column = 1, sticky = "NESW", pady = 2)
		state_entry.grid(row = 13, column = 2, sticky = "NESW", pady = 2)
		acc_num_entry.grid(row = 14, column = 2, sticky = "NESW", pady = 2)
		acc_num_label.grid(row = 14, column = 1, sticky = "NESW", pady = 2)

	def getinfo(self, controller):
		global first_name
		global last_name
		global email
		global registration_password
		global line1
		global line2
		global zip_code
		global city
		global phone_number
		global state
		global acc_num

		user_first_name = first_name.get()
		user_last_name = last_name.get()
		user_email = email.get()
		user_password = registration_password.get()
		user_line1 = line1.get()
		user_line2 = line2.get()
		user_zip_code = zip_code.get()
		user_city = city.get()
		user_phone_number = phone_number.get()
		user_acc_num = acc_num.get()
		state1 = state.get()
		print (user_acc_num)
		print (type(user_acc_num))
		#pdb.set_trace()
		#print (state.get())


		#print(user_first_name, user_last_name, user_email, user_password, user_line1, user_line2, user_zip_code, user_city, user_phone_number)
		#pdb.set_trace()
		#print (first_name)
		#sql_queries.insertcustomer(first_name,last_name,line1, line2,city,state,int(zip_code_entry.get()),int(phone_number_entry.get()), registration_password, int(acc_num_entry.get()))
		sql_queries.insertcustomer(user_first_name,user_line1, user_line2,user_city,state1,int(user_zip_code),int(user_phone_number), user_email, user_password,int(user_acc_num))
		messagebox.showinfo("User Registered", 'User Registered successfully')
		controller.show_frame(LoginPage)

class result_page(tk.Frame):
	def __init__(self, parent, controller):
		global item_name
		global item_price

		tk.Frame.__init__(self, parent)
		back_button = Button(self, text = "Back", command = lambda: controller.show_frame(search_page))
		item_name = Label(self, text = 'item name')
		item_price = Label(self, text = 'price')
		add_to_cart_button = Button(self, text = 'Add To Cart', command = lambda: self.add_to_cart(controller))

		back_button.grid(row = 1, column = 1, sticky = "EW", pady = 5, padx = 5)
		item_name.grid(row = 2, column= 1)
		item_price.grid(row = 2, column = 2)
		add_to_cart_button.grid(row = 3, column = 2)

	def get_details():
		global item_index
		global item_list
		global item_name
		global item_price
		

		item_name['text'] = item_list[item_index][1]
		item_price['text'] = item_list[item_index][6]

	def add_to_cart(self, controller):
		global cart
		global item_index
		global item_list
		flag = True

		if cart:
			print(item_list[item_index][1], cart[0])
			for i in range(len(cart)):
				if item_list[item_index][1] == cart[i][1]:
					# print('not ok')
					cart[i][7] += 1
					flag = False
		if flag:
			item_added = list(item_list[item_index])
			item_added.append(1)
			cart.append(item_added)
		# print(f'index {item_index}')

		# print(item_list)
		# print(cart)

		controller.show_frame(search_page)


		



applet = main_window()
applet.title("Best Buy")
applet.geometry("500x500")
applet.mainloop()


"""
sam123@gmail.com
kdhdjdkd
"""