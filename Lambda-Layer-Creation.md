# lambda-layer

# Pre-Requisites:
    - Install python
    - Install pip
    - Install 7-zip
# Create folder "python/lib/python3.8/site-packages"
    mkdir -p python/lib/python3.8/site-packages
# Install mysql-connector module using "pip"
    pip install mysql-connector -t python/lib/python3.8/site-packages
# Zip python folder
  ![image](https://user-images.githubusercontent.com/58024415/105275412-52c10b00-5bc5-11eb-8ee2-ceac7fda294c.png)
# Upload zip file as Lambda Layer by open Lambda service and then select Layers
  
 ![image](https://user-images.githubusercontent.com/58024415/105275525-8f8d0200-5bc5-11eb-9419-204433e54024.png)
  
# Click on Create Layer
  
 ![image](https://user-images.githubusercontent.com/58024415/105275623-c8c57200-5bc5-11eb-8c04-4102230075b4.png)
  
# Provide details and click on create
  
 ![image](https://user-images.githubusercontent.com/58024415/105276103-a08a4300-5bc6-11eb-9ea7-c42aeb46d06e.png)