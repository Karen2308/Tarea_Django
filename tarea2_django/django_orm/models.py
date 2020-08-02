from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)


#Ingresar
#Producto
#P = Producto(descripcion='Aceite Girazol',precio=1.50,stock=2000)
#P.save()
#Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000)

#Cliente
#clt = Cliente(ruc='0999764566001',nombre='Karen',direccion='Av. Quito')
#clt.save()
#clt.producto.add(1)
#Cliente.objects.create(ruc='1308765433001',nombre='Javier Castro',direccion='Atahualpa')
#clt2 = Cliente.objects.get(nombre='Javier Castro')
#clt2.producto.add(2)

#Factura
#factu1 = Factura(cliente=clt,fecha='2020-01-01',total=30.50)
#factu1.save()
#Factura.objects.create(cliente=clt2,fecha='2020-02-02',total=22.37)
#factu2=Factura.objects.get(cliente__nombre='Javier Castro')

#Detalle Factura
#Deta = DetalleFactura(factura=factu1,producto=P,cantidad=2,precio=9,subtotal=18)
#Deta.save()
#DetalleFactura.objects.create(factura=factu1,producto=Producto.objects.get(descripcion='Coca Cola'),cantidad=3,precio=4.17,subtotal=12.5)

#Modificar
#Producto y Cliente
#p = Producto.objects.get(id=1)
#p.precio=1.13
#p.save()
#Producto.objects.filter(id=1).update(precio=1.7)

#modcli = Cliente.objects.get(id=1)
#modcli.producto.add(2)
#modcli.save()
#Cliente.objects.filter(id=2).update(producto=1)

#Factura y Detalle Factura

#factu = Factura.objects.get(id=1)
#factu.total=23.90
#factu.save()
#Factura.objects.filter(id=2).update(total=55.88)

#DetalleFactura.objects.filter(id=2).update(subtotal=22.80)

#Eliminar

#Producto y CLiente
#elipro = Producto.objects.get(id=1)
#elipro.delete()
#Producto.objects.filter(id=2).delete()

#elimcli = Cliente.objects.get(id=1)
#elimcli.delete()
#Cliente.objects.filter(id=2).delete()


#Factura y Detalle Factura
#elimfact = Factura.objects.get(id=3)
#elimfact.delete()
#Factura.objects.filter(id=4).delete()


#elimdeta= DetalleFactura.objects.get(id=3)
#elimdeta.delete()
#DetalleFactura.objects.filter(id=4).delete()

#Query de un Modelo
#p=Producto.objects.all()
#p=Producto.objects.get(id=4)
#Producto.objects.filter(id__lte=4)
#Producto.objects.exclude(descripcion__icontains='Cola')
#Producto.objects.filter(id__gte=4)
#Producto.objects.filter(id__gt=4).values('id','descripcion')
#Producto.objects.filter(id__lt=4).values('id','descripcion')
#Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')

#Query de varios modelos relacionados
#Factura.objects.filter(cliente__nombre='Karen')
#c= Cliente.objects.get(nombre='Karen')
#c.factura_set.all()
#c.factura_set.filter(id=4)
#Factura.objects.select_related('cliente').filter(cliente__nombre='Karen')
#Cliente.objects.prefetch_related('producto').filter(nombre='Karen').values('nombre','producto__descripcion')

