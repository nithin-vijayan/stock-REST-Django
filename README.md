# stock-REST-Django
REST framework helps in maintaining uniform interoperability between two applications or system regardless of the architecture they are built on.
The project demonstrate a Stock Market app using django REST Framework, which can retrieve data using GET request as well as update data at server side using POST request.


### Running the server :
Use python manage.py runserver



### For Adding a Stock to database navigate to /stocks/create/

![Alt text](/readme_images/create_url.jpg?raw=true "Url for adding stock to Database")

### Fill in stock details on browsable API for adding stocks

![Alt text](/readme_images/create.jpg?raw=true "Adding stocks to Database")




### For getting a particular stock details navigate to /stocks/<stock_id>

![Alt text](/readme_images/retrieve_one_url.jpg?raw=true "REtrieve URL")

### Response will list the particular stock fields

![Alt text](/readme_images/retrieve_one.jpg?raw=true "Retrieve One stock from database based ok PK")




### For getting the list of stocks in database navigate to /stocks/

![Alt text](/readme_images/url.jpg?raw=true "List all stocks in Database")

### Response list will contain all the stocks in app database with related fields

![Alt text](/readme_images/get.jpg?raw=true "Url to List stocks")




### For updating a particular stock in database navigate to /stocks/<stock_id>/edit/

![Alt text](/readme_images/update_url.jpg?raw=true "Updating a single stock")

### Fill in stock details on browsable API for Updating stock

![Alt text](/readme_images/update.jpg?raw=true "Stock Update Url")




### For Deleting a particular stock based on id in database navigate to /stocks/<stock_id>/delete/

![Alt text](/readme_images/delete_url.jpg?raw=true "Stock Delete Url")

### Confirm delete on browsable api for deleting the stock

![Alt text](/readme_images/delete.jpg?raw=true "Delete a single Stock")



#### At any time, to get response in json plain text, suffix the url with '.json'
