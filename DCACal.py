def my_avg_price():
    # Input kanggo ngitung avg price
    avg_price_1 = float(input("\nTuku ing rega (1): "))
    avg_price_2 = float(input("Tuku ing rega (2): "))
    amount_1 = float(input("Jumlah tuku (1): "))
    amount_2 = float(input("Jumlah tuku (2): "))

    # Ngitung avg saiki (harga rata-rata sawisé penjumlahan)
    total_amount = amount_1 + amount_2
    total_value = (amount_1 / avg_price_1) + (amount_2 / avg_price_2)
    avg_now = total_amount / total_value 

    # Nampilaké hasil avg_now
    print(f"Avg Saiki: {avg_now:.2f}")
    print(f"Total Jumlah: ${total_amount:.2f}")
    print(f"Total token : {total_value:.2f} Token")
    
    # Opsi pilihan
    ulangi = input("\nApa sampeyan pengin ngulang perhitungan My Avg Price? (y/n): ").strip().lower()
    if ulangi == 'y':
        my_avg_price()
    else:
        return

def dca_target():
    # Input kanggo DCA Target
    avg_price_1 = float(input("\nTuku ing rega (1): : "))
    avg_price_2 = float(input("Tuku ing rega (2): "))
    amount_1 = float(input("Jumlah tuku (1): "))
    amount_2 = float(input("Jumlah tuku (2): "))

    # Ngitung avg saiki
    total_amount = amount_1 + amount_2
    total_value = (avg_price_1 * amount_1) + (avg_price_2 * amount_2)
    avg_now = total_value / total_amount

    # Input tambahan kanggo target avg price lan tuku ing rega
    target_avg_price = float(input("\nHarga target rata-rata: "))
    buy_at = float(input("Tuku ing rega (kanggo DCA): "))

    # Ngitung jumlah sing perlu dituku (tuku kanthi ... $)
    target_value = target_avg_price * total_amount
    buy_with_amount = target_value - total_value
    buy_with_quantity = buy_with_amount / buy_at

    # Output hasil perhitungan
    print(f"Target Avg Price: {target_avg_price}")
    print(f"Tuku ing rega: {buy_at}")
    print(f"Tuku nganggo {buy_with_amount:.2f}$")

    # Opsi pilihan
    ulangi = input("\nApa sampeyan pengin ngulang perhitungan DCA Target? (y/n): ").strip().lower()
    if ulangi == 'y':
        dca_target()
    else:
        return

def all_count():
    # Nindakake perhitungan My Avg Price
    my_avg_price()

    # Nanya apa pengguna pengin nerusake ke perhitungan DCA Target
    proceed = input("\nApa sampeyan pengin nerusake perhitungan DCA Target? (y/n): ").strip().lower()
    if proceed == 'y':
        dca_target()

    # Opsi pilihan setelah selesai
    ulangi = input("\nApa sampeyan pengin ngulang perhitungan All Count? (y/n): ").strip().lower()
    if ulangi == 'y':
        all_count()
    else:
        return

def main_menu():
    while True:
        # Nampilaké menu
        print("\n===== Menu Kalkulator DCA =====")
        print("1. My Avg Price")
        print("2. DCA Target")
        print("3. All Count (My Avg Price & DCA Target)")
        print("4. Exit")
        
        # Milih menu
        choice = input("Pilihan (1/2/3/4): ").strip()

        if choice == '1':
            my_avg_price()
        elif choice == '2':
            dca_target()
        elif choice == '3':
            all_count()
        elif choice == '4':
            print("Ditutup!")
            break  # Metu saka loop lan mandhegake program
        else:
            print("Pilihan ora ditemokake")
        
        # Opsi pilihan setelah perhitungan selesai
        proceed_back = input("\nBalik menyang menu utama? (y/n): ").strip().lower()
        if proceed_back == 'n':
            print("Ditutup!")
            break  # Metu saka loop lan mandhegake program

# Njalanke menu utama
main_menu()
