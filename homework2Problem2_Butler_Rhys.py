#this is a comment.


class SalesPerson:

	totalSales = 0
	salesCommission = 0
	weeklyEarnings = 0

	def add_item(self, _item_num):

		if _item_num == 1:
			self.totalSales = self.totalSales + 239.99
		if _item_num == 2:
			self.totalSales = self.totalSales + 129.75
		if _item_num == 3:
			self.totalSales = self.totalSales + 99.95
		if _item_num == 4:
			self.totalSales = self.totalSales + 350.89

	def input_weekly_sales(self):

		user_choice = 'y'

		while user_choice == 'y' or 'Y':
			print("Please enter item #:")
			print("Would you like to continue?\n")
			user_choice = input("Please enter 'Y' or 'N'")





	def calculate_sales_commission(self):

		self.salesCommission = self.totalSales * .09
		print(f'The Sales commission is: {self.salesCommission:.2f}')


sales = SalesPerson()

sales.add_item(1)

sales.calculate_sales_commission()













