pipeline {
  agent {
    docker {
      args '3.5'
      image 'maven-3.5'
    }
    
  }
  stages {
    stage('stag3') {
      steps {
        input(message: 'Hello Ashwani', id: 'Name', ok: 'Working on Stage')
      }
    }
  }
}