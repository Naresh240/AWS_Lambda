pipeline{
    agent any
    stages{
        stage("SCM"){
            steps{
                git branch: 'main', 
                url: 'https://github.com/Naresh240/Lambda-APIGateway-with-Serverless.git'
            }
        }
        stage('install serverless'){
            steps{
                sh 'sudo npm install'
            }
        }
        stage('create custom domain and deploy'){
            steps{
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', 
                                  accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                                  credentialsId: 'aws-credentials', 
                                  secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh '''
                        export SLS_DEBUG=*
                        sudo serverless create_domain
                        serverless deploy --stage dev --region us-east-1
                    '''
                }
            }
        }
    }
}
