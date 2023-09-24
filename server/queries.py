#queries to gather the relevant information for the memo

product_query = '''SELECT Product.ProductName, Product.unitprice, Supplier.suppliername 
FROM Product 
LEFT JOIN SupplierProduct 
ON Product.productid = SupplierProduct.productid 
LEFT JOIN Supplier 
ON SupplierProduct.supplierID = Supplier.supplierid;'''

customer_query = '''SELECT
    Customer.CustomerName,
    Customer.ContactName,
    Customer.ContactEmail,
    Customer.Phone,
    Orders.OrderID,
    Orders.OrderDate,
    Orders.ShipDate,
    Orders.TotalAmount,
    OrderItem.Quantity,
    Product.ProductName,
    Product.UnitPrice
FROM
    Customer AS Customer
LEFT JOIN
    Orders AS Orders
ON
    Customer.CustomerID = Orders.CustomerID
LEFT JOIN
    OrderItem AS OrderItem
ON
    Orders.OrderID = OrderItem.OrderID
LEFT JOIN
    Product AS Product
ON
    OrderItem.ProductID = Product.ProductID;
'''

supply_query = ''' SELECT
Inventory.QuantityInStock,
Inventory.LastStockUpdateDate,

Product.ProductID,
Product.ProductName

FROM Inventory 
LEFT JOIN Product
ON Inventory.ProductID = Product.ProductID;
'''