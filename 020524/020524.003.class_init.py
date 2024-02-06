class Cellphone:

    #__init__ es un methood "magic" = constructor = es un metodo que obliga a inicializar atributos

    def __init__(self, brand, model, color):   
        self.brand = brand
        self.model = model
        self.color = color

    def start_on(self):
        return 'Device is on'
    
    def power_of(self):
        return 'Turning off device'
    
#instanciando el objeto
    
iphone = Cellphone('Apple', 'iPhone 15', 'Black')
print(iphone.brand)

samsung = Cellphone('Samsung', 'Galaxy', 'Silver')
print(samsung.color)
print(samsung.start_on())
