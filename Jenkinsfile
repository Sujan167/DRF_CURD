pipeline{
    agent any
    
    stages{
        stage("Clone Code"){
            steps{
                echo "Cloning the code"
                git url: "https://github.com/Sujan167/DRF_CURD.git", branch:"main"
            }
            
        }
        stage("build"){
            steps{
                echo "Building the image"
                sh "docker build -t DRF_CURD ."
            }
        }
        stage("Push to docker hub"){
            steps{
                echo "Pushing image to docker hub"
                withCredentials([usernamePassword(credentialsId:"dockerhub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker tag DRF_CRUD ${env.dockerHubUser}/DRF_CURD:latest"
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker push ${env.dockerHubUser}/DRF_CURD:latest"
                }
            }
        }
        stage("Deploy"){
            steps{
                echo "Deploying the container"
                sh "docker run -d -p 8000:8000 itssujan/DRF_CURD:latest"
            }
        }
    }
}
