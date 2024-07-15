FROM openjdk:11-jre-slim
WORKDIR /app
COPY target/*.jar .
EXPOSE 1001
CMD ["java", "-jar", "/offers-0.0.1-SNAPSHOT.jar"]
