class Cafe:
    def __init__(self):
        self.customers = []
        self.orders = {}

    def add_customer(self, name):
        if name not in self.customers:
            self.customers.append(name)
            self.orders[name] = []
            print(f"{name} isimli müşteri başarıyla eklendi.")
        else:
            print(f"{name} isimli müşteri zaten mevcut.")

    def add_order(self, customer_name, order_amount):
        if customer_name in self.customers:
            self.orders[customer_name].append(order_amount)
            print(f"{customer_name} isimli müşterinin siparişi başarıyla eklendi.")
        else:
            print(f"{customer_name} isimli müşteri bulunamadı.")

    def pay_bill(self, customer_name, payment_amount):
        if customer_name in self.customers:
            total_amount = sum(self.orders[customer_name])
            if payment_amount >= total_amount:
                change = payment_amount - total_amount
                self.orders[customer_name] = []
                print(f"{customer_name} isimli müşterinin hesabı başarıyla ödendi. Para üstü: {change:.2f}")
            else:
                remaining_balance = total_amount - payment_amount
                print(f"{customer_name} isimli müşterinin hesabı {remaining_balance:.2f} TL kadar ödenmedi.")
        else:
            print(f"{customer_name} isimli müşteri bulunamadı.")
    
    def get_unpaid_bills(self):
        unpaid_customers = []
        for customer_name in self.customers:
            total_amount = sum(self.orders[customer_name])
            if total_amount > 0:
                unpaid_customers.append(customer_name)
        
        if len(unpaid_customers) > 0:
            print("Aşağıdaki müşterilerin ödenmemiş hesapları bulunmaktadır:")
            for customer_name in unpaid_customers:
                total_amount = sum(self.orders[customer_name])
                print(f"{customer_name}: {total_amount:.2f} TL")
        else:
            print("Ödenmemiş hesap bulunmamaktadır.")

# Örnek kullanım
cafe = Cafe()

while True:
    print("1. Müşteri Ekle")
    print("2. Sipariş Ekle")
    print("3. Ödeme Ekle")
    print("4. Ödenmeyenler")
    print("5. Çıkış")
    selection = input("Lütfen bir işlem seçiniz: ")
    if selection == "1":
        customer_name = input("Lütfen müşteri adını giriniz: ")
        cafe.add_customer(customer_name)
    elif selection == "2":
        customer_name = input("Lütfen müşteri adını giriniz: ")
        order_amount = float(input("Lütfen sipariş tutarını giriniz: "))
        cafe.add_order(customer_name, order_amount)
    elif selection == "3":
        customer_name = input("Lütfen müşteri adını giriniz: ")
        payment_amount = float(input("Lütfen ödeme miktarını giriniz: "))
        cafe.pay_bill(customer_name, payment_amount)
    elif selection == "4":
        cafe.get_unpaid_bills()
    elif selection == "5":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")