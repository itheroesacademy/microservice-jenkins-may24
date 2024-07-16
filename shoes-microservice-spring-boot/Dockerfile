FROM maven:3-alpine
WORKDIR /app
COPY target/*.jar .
EXPOSE 1002
CMD ["java","-jar","/shoes-0.0.1-SNAPSHOT.jar"]
