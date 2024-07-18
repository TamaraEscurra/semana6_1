from ownable import Ownable
class Cart(Ownable):
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            return
        for item in self.items_list():
            item.owner.wallet.deposit(self.owner.wallet.withdraw(item.price))
            item.owner = self.owner
        self.items.clear()
            
        # requisitos
        #   - Contenido del carrito（Cart#items）El monto de la compra de todos los artículos del artículo se transferirá de la billetera del propietario del carrito a la billetera del propietario del artículo.
        #   - Contenido del carrito（Cart#items）La propiedad de todos los artículos del carrito se transfiere al propietario del carrito.
        #   - Contenido del carrito（Cart#items）estar vacío.
        # consejos
        #   - Cartera del propietario del carrito ==> self.owner.wallet
        #   - Cartera del propietario del artículo ==> item.owner.wallet
        #   - El dinero se transfiere ==> Esa cantidad se retira de la billetera de (?) y se deposita en la billetera de (?).
        #   - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir propietario (item.owner =?)
