from customer import Customer
from item import Item
from seller import Seller

seller = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Mother board", 28980, seller)
    Item("Power supply unit", 8980, seller)
    Item("PCcase", 8727, seller)
    Item("3.5inchHDD", 10980, seller)
    Item("2.5inchSSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU Cooler", 13400, seller)
    Item("Graphic board", 23800, seller)

print("🤖 Por favor dime tu nombre")
customer = Customer(input())

print("🏧 Por favor ingresa el monto a cargar a tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ empieza a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor ingrese el número de producto")
    number = int(input())

    print("⛏ Por favor ingrese la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 cantidad total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres terminar de comprar? (si/no)")
    end_shopping = input() == "si"

print("💸 ¿Confirmar tu compra? (si/no)")
if input() == "si":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name} propiedad de")
customer.show_items()
print(f"😱👛 {customer.name} saldo de billetera de: {customer.wallet.balance}")

print(f"📦 {seller.name} estado del inventario")
seller.show_items()
print(f"😻👛 {seller.name} saldo de billetera de: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 cantidad total: {customer.cart.total_amount()}")

print("🎉 fin")