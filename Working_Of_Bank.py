class Bank():

    def __init__(self, Owner, Current_Amount):

        self.Owner = Owner
        self.Current_Amount = Current_Amount

    def info(self):
        print(
            f"This account belongs to {self.Owner} and current balence is {self.Current_Amount}")

    def withdraw(self, n):

        self.n = n

        if n > self.Current_Amount:
            print("Do not have sufficient funds")

        elif 0 <= n <= self.Current_Amount:
            print("Money withdrawed successfully")
            self.Current_Amount = self.Current_Amount - self.n

    def deposit(self, m):

        self.m = m
        self.Current_Amount = self.Current_Amount + self.m
        print("Money deposited succesfully")


if __name__ == "__main__":

    a = Bank("Shivam", 500)
    a.info()
    a.withdraw(250)
    a.info()
    a.deposit(2000)
    a.info()
