
# Declare a class named SalesPerson


class SalesPerson:

	totalSales = 0
	salesCommission = 0
	weeklyEarnings = 0

	# This function allows the user to enter an item number.
	# The item number's cost will be added to the totalSales of the
	# SalesPerson object.
	def add_item(self, _item_num):

		if _item_num == 1:
			self.totalSales = self.totalSales + 239.99
		if _item_num == 2:
			self.totalSales = self.totalSales + 129.75
		if _item_num == 3:
			self.totalSales = self.totalSales + 99.95
		if _item_num == 4:
			self.totalSales = self.totalSales + 350.89

	# This function allows a user to input any number of items they choose
	# the program only allows the user to input a one through a four.
	def input_weekly_sales(self):

		user_choice = 1

		while user_choice != 0:

			num_items = int(input("How many items would you like to enter?"))
			for i in range(num_items):
				print(f"i is:", i)
				item_number = int(input("Please enter item #:"))
				while item_number < 1 or item_number > 4:
					print("Please enter an integer between 1 and 4 for the item number\n")
				self.add_item(item_number)

			print("Would you like to enter more items?\n")
			user_choice = int(input("Please enter '1' to continue or '0' to stop."))

	# Calculate_sales_comission() calculates the sales commission of the object based on the
	# current values of the SalesPerson object's attributes.
	def calculate_sales_commission(self):
		# The sales commission will be equal to 200 plus 9% of the SalesPerson's weekly sales.
		self.salesCommission = self.totalSales * .09 + 200
		print(f'The Sales commission is: {self.salesCommission:.2f}')


print("This program allows you to enter in items for a Salesperson's weekly sales\n")
print("It will allow you to enter as many items as you choose.\n")
print("The cost of each item follows:\n")

# Print the cost of each item to the user.
for i in range(4):
	if i == 0:
		print(f"Item", i+1, ": 239.99")
	if i == 1:
		print(f"Item", i+1, ": 129.75")
	if i == 2:
		print(f"Item", i+1, ": 99.95")
	if i == 3:
		print(f"Item", i+1, ": 350.89\n")

print("When you are done entering items it will print the Salesperson's total weekly sales,")
print("their weekly commission, and their total earnings.\n")

sales = SalesPerson()

sales.input_weekly_sales()

sales.calculate_sales_commission()

print("Please come by anytime you would like to calculate your commission!!")




















