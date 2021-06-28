# Lambda-APIGateway-with-Serverless

# Pre-Requisites
    Install Python
    Install PIP
    Install NPM
    Create Hosted Zone (Route53)
    Get certificate for domain (certificate manager)
# Install Python, PIP and NPM
  # Python-PIP
    yum install python-pip -y
  # NPM
    sudo yum install -y gcc-c++ make
    curl -sL https://rpm.nodesource.com/setup_13.x | sudo -E bash -
    sudo yum install -y nodejs
# Create Hosted Zone (Route53)
  ![image](https://user-images.githubusercontent.com/58024415/104114989-761bc880-5330-11eb-83c3-530b8d6db2ca.png)
# Get certificate for domain (certificate manager)
  ![image](https://user-images.githubusercontent.com/58024415/104115002-90ee3d00-5330-11eb-9ba6-f9e94d02984d.png)
# Install dependencies
    npm install
# create your custom domain with a single command:
    serverless create_domain
  Note: It may take 5 to 10min, for custom domain please go and check in API Gateway service
  
  ![image](https://user-images.githubusercontent.com/58024415/104114910-926b3580-532f-11eb-82f9-1e75016be6a7.png)
# Once your domain name is ready, deploy your service:
    serverless deploy --region us-east-1   
# Open web UI and check output using below URL's
  https://serverless.nareshtestdomain.tk/hello
  
  ![image](https://user-images.githubusercontent.com/58024415/104114980-5d131780-5330-11eb-8276-9faeefa79e77.png)
  
  https://serverless.nareshtestdomain.tk/goodbye
  
  ![image](https://user-images.githubusercontent.com/58024415/104114982-61d7cb80-5330-11eb-8b8c-9a5d5b52fdff.png)
